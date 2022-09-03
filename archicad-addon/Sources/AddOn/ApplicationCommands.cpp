#include "ApplicationCommands.hpp"
#include "ObjectState.hpp"
#include "FileSystem.hpp"

GS::String GetArchicadLocationCommand::GetName () const
{
    return "GetArchicadLocation";
}

GS::Optional<GS::UniString> GetArchicadLocationCommand::GetResponseSchema () const
{
    return R"({
        "type": "object",
        "properties": {
            "archicadLocation": {
                "type": "string",
                "description": "The location of the Archicad executable in the filesystem.",
                "minLength": 1
            }
        },
        "additionalProperties": false,
        "required": [
            "archicadLocation"
        ]
    })";
}

GS::ObjectState GetArchicadLocationCommand::Execute (const GS::ObjectState& /*parameters*/, GS::ProcessControl& /*processControl*/) const
{
    IO::Location applicationFileLocation;
    GSErrCode error = IO::fileSystem.GetSpecialLocation (IO::FileSystem::ApplicationFile, &applicationFileLocation);
    if (error != NoError) {
        return CreateErrorResponse (APIERR_GENERAL, "Failed to get the location of the Archicad application!");
    }
    return GS::ObjectState ("archicadLocation", applicationFileLocation.ToDisplayText ());
}

GS::String QuitArchicadCommand::GetName () const
{
    return "QuitArchicad";
}

GS::ObjectState QuitArchicadCommand::Execute (const GS::ObjectState& /*parameters*/, GS::ProcessControl& /*processControl*/) const
{
    Int64 magicCode = 1234;
    GSErrCode err = ACAPI_Automate (APIDo_QuitID, reinterpret_cast<void*> (magicCode));

    if (err != NoError) {
        return CreateErrorResponse (APIERR_COMMANDFAILED, "Failed to quit Archicad!");
    }

    return {};
}
