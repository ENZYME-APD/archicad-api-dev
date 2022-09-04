var commands = [
    {
        name : "GetAddOnVersion",
        version : "0.1.0",
        description : "Retrieves the version of the Tapir Additional JSON Commands Add-On.",
        inputScheme : null,
        outputScheme : {
            "type": "object",
            "properties": {
                "version": {
                    "type": "string",
                    "description": "Version number in the form of \"1.1.1\".",
                    "minLength": 1
                }
            },
            "additionalProperties": false,
            "required": [
                "version"
            ]
        }
    },
    {
        name : "GetArchicadLocation",
        version : "0.1.0",
        description : "Retrieves the location of the currently running Archicad executable.",
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
        name : "QuitArchicad",
        version : "0.1.0",
        description : "Performs a quit operation on the currently running Archicad instance.",
        inputScheme : null,
        outputScheme : null
    },
    {
        name : "GetProjectInfo",
        version : "0.1.0",
        description : "Retrieves information about the currently loaded project.",
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
    },
    {
        name : "GetHotlinks",
        version : "0.1.0",
        description : "Gets the file system locations (path) of the hotlink modules. The hotlinks can have tree hierarchy in the project.",
        inputScheme : null,
        outputScheme : {
            "Hotlinks": {
              "type": "array",
              "description": "A list of hotlink nodes.",
              "items": {
                "$ref": "#/Hotlink"
              }
            },
            "Hotlink": {
              "type": "object",
              "description": "The details of a hotlink node.",
              "properties": {
                "location": {
                  "type": "string",
                  "description": "The path of the hotlink file."
                },
                "children": {
                  "$ref": "#/Hotlinks",
                  "description": "The children of the hotlink node if it has any."
                }
              },
              "additionalProperties": false,
              "required": [
                "location"
              ]
            },
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
        }
    },
];
