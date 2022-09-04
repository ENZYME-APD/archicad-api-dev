#include "CommandBase.hpp"

constexpr const char* CommandNamespace = "TapirCommand";
constexpr const char* ErrorResponseField = "error";
constexpr const char* ErrorCodeResponseField = "code";
constexpr const char* ErrorMessageResponseField = "message";

GS::String CommandBase::GetNamespace () const
{
    return CommandNamespace;
}

GS::Optional<GS::UniString> CommandBase::GetSchemaDefinitions () const
{
    return {};
}

GS::Optional<GS::UniString> CommandBase::GetInputParametersSchema () const
{
    return {};
}

GS::Optional<GS::UniString> CommandBase::GetResponseSchema () const
{
    return GS::UniString::Printf (R"({
        "type": "object",
        "properties": {
            "%s": {
                "$ref": "APITypes.json#/definitions/Error"
            }
        },
        "additionalProperties": false,
        "required": []
    })",
    ErrorResponseField);
}

void CommandBase::OnResponseValidationFailed (const GS::ObjectState& /*response*/) const
{

}

API_AddOnCommandExecutionPolicy CommandBase::GetExecutionPolicy () const
{
    return API_AddOnCommandExecutionPolicy::ScheduleForExecutionOnMainThread;
}

#ifdef ServerMainVers_2600
bool CommandBase::IsProcessWindowVisible () const
{
    return false;
}
#endif

GS::ObjectState CreateErrorResponse (APIErrCodes errorCode, const char* errorMessage)
{
    GS::ObjectState error;
    error.Add (ErrorCodeResponseField, errorCode);
    error.Add (ErrorMessageResponseField, errorMessage);
    return GS::ObjectState (ErrorResponseField, error);
}
