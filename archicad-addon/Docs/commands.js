var commands = [
    {
        name : 'GetArchicadLocation',
        description : 'Retrieves the location of the currently running Archicad executable.',
        inputScheme : null,
        outputScheme : {
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
        }
    },
    {
        name : 'QuitArchicad',
        description : 'Performs a quit operation on the currently running Archicad instance.',
        inputScheme : null,
        outputScheme : null
    },
    {
        name : 'GetProjectInfo',
        description : 'Retrieves information about the currently loaded project.',
        inputScheme : null,
        outputScheme : {
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
        }
    }
];
