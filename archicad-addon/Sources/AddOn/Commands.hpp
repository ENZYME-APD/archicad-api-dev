#pragma once

#include "CommandBase.hpp"

class PublishCommand : public CommandBase
{
public:
    virtual GS::String GetName () const override;
    virtual GS::Optional<GS::UniString> GetInputParametersSchema () const override;
    virtual GS::ObjectState Execute (const GS::ObjectState& parameters, GS::ProcessControl& processControl) const override;
};

class TeamworkReceiveCommand : public CommandBase
{
public:
    virtual GS::String GetName () const override;
    virtual GS::ObjectState Execute (const GS::ObjectState& parameters, GS::ProcessControl& processControl) const override;
};

class ReloadLibrariesCommand : public CommandBase
{
public:
    virtual GS::String GetName () const override;
    virtual GS::ObjectState Execute (const GS::ObjectState& parameters, GS::ProcessControl& processControl) const override;
};

class MoveElementsCommand : public CommandBase
{
public:
    virtual GS::String GetName () const override;
    virtual GS::Optional<GS::UniString> GetInputParametersSchema () const override;
    virtual GS::ObjectState Execute (const GS::ObjectState& parameters, GS::ProcessControl& processControl) const override;
};

class CreateColumnsCommand : public CommandBase
{
public:
    virtual GS::String GetName () const override;
    virtual GS::Optional<GS::UniString> GetInputParametersSchema () const override;
    virtual GS::ObjectState Execute (const GS::ObjectState& parameters, GS::ProcessControl& processControl) const override;
};
