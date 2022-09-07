#include "ProjectCommands.hpp"
#include "SchemaDefinitions.hpp"
#include "ObjectState.hpp"

GS::String GetProjectInfoCommand::GetName () const
{
    return "GetProjectInfo";
}

GS::Optional<GS::UniString> GetProjectInfoCommand::GetResponseSchema () const
{
    return R"({
        "type": "object",
        "properties": {
            "isUntitled": {
                "type": "boolean",
                "description": "True, if the project is not saved yet."
            },
            "isTeamwork": {
                "type": "boolean",
                "description": "True, if the project is a Teamwork (BIMcloud) project."
            },
            "projectLocation": {
                "type": "string",
                "description": "The location of the project in the filesystem or a BIMcloud project reference.",
                "minLength": 1
            },
            "projectPath": {
                "type": "string",
                "description": "The path of the project. A filesystem path or a BIMcloud server relative path.",
                "minLength": 1
            },
            "projectName": {
                "type": "string",
                "description": "The name of the project.",
                "minLength": 1
            }
        },
        "additionalProperties": false,
        "required": [
            "isUntitled",
            "isTeamwork"
        ]
    })";
}

GS::ObjectState GetProjectInfoCommand::Execute (const GS::ObjectState& /*parameters*/, GS::ProcessControl& /*processControl*/) const
{
    API_ProjectInfo projectInfo = {};
    GSErrCode err = ACAPI_Environment (APIEnv_ProjectID, &projectInfo);

    if (err != NoError) {
        return CreateErrorResponse (APIERR_NOPLAN, "Failed to retrieve project information. Check the opened project!");
    }

    GS::ObjectState response;
    response.Add ("isUntitled", projectInfo.untitled);
    response.Add ("isTeamwork", projectInfo.teamwork);
    if (!projectInfo.untitled) {
        if (projectInfo.location) {
            response.Add ("projectLocation", projectInfo.location->ToDisplayText ());
        }
        if (projectInfo.projectPath) {
            response.Add ("projectPath", *projectInfo.projectPath);
        }
        if (projectInfo.projectName) {
            response.Add ("projectName", *projectInfo.projectName);
        }
    }

    return response;
}

GS::String GetHotlinksCommand::GetName () const
{
    return "GetHotlinks";
}

GS::Optional<GS::UniString> GetHotlinksCommand::GetSchemaDefinitions () const
{
    return GetCommonSchemaDefinitions ();
}

GS::Optional<GS::UniString> GetHotlinksCommand::GetResponseSchema () const
{
    return R"({
        "type": "object",
        "properties": {
            "hotlinks": {
                "$ref": "#/Hotlinks"
            }
        },
        "additionalProperties": false,
        "required": [
            "hotlinks"
        ]
    })";
}

static GS::Optional<GS::UniString>    GetLocationOfHotlink (const API_Guid& hotlinkGuid)
{
    API_HotlinkNode hotlinkNode = {};
    hotlinkNode.guid = hotlinkGuid;

    ACAPI_Database (APIDb_GetHotlinkNodeID, &hotlinkNode);

    if (hotlinkNode.sourceLocation == nullptr) {
        return GS::NoValue;
    }

    return hotlinkNode.sourceLocation->ToDisplayText ();
}

static GS::ObjectState DumpHotlinkWithChildren (const API_Guid& hotlinkGuid,
                                                 GS::HashTable<API_Guid, GS::Array<API_Guid>>& hotlinkTree)
{
    GS::ObjectState hotlinkNodeOS;

    const auto& location = GetLocationOfHotlink (hotlinkGuid);
    if (location.HasValue ()) {
        hotlinkNodeOS.Add ("location", location.Get ());
    }

    const auto& children = hotlinkTree.Retrieve (hotlinkGuid);
    if (!children.IsEmpty ()) {
        const auto& listAdder = hotlinkNodeOS.AddList<GS::ObjectState> ("children");
        for (const API_Guid& childNodeGuid : hotlinkTree.Retrieve (hotlinkGuid)) {
            listAdder (DumpHotlinkWithChildren (childNodeGuid, hotlinkTree));
        }
    }

    return hotlinkNodeOS;
}

GS::ObjectState GetHotlinksCommand::Execute (const GS::ObjectState& /*parameters*/, GS::ProcessControl& /*processControl*/) const
{
    GS::ObjectState response;
    const auto& listAdder = response.AddList<GS::ObjectState> ("hotlinks");

    for (API_HotlinkTypeID type : {APIHotlink_Module, APIHotlink_XRef}) {
        API_Guid hotlinkRootNodeGuid = APINULLGuid;
        if (ACAPI_Database (APIDb_GetHotlinkRootNodeGuidID, &type, &hotlinkRootNodeGuid) == NoError) {
            GS::HashTable<API_Guid, GS::Array<API_Guid>> hotlinkTree;
            if (ACAPI_Database (APIDb_GetHotlinkNodeTreeID, &hotlinkRootNodeGuid, &hotlinkTree) == NoError) {
                for (const API_Guid& childNodeGuid : hotlinkTree.Retrieve (hotlinkRootNodeGuid)) {
                    listAdder (DumpHotlinkWithChildren (childNodeGuid, hotlinkTree));
                }
            }
        }
    }

    return response;
}
