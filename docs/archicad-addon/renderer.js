function CreateElement (parentElement, elementType, className, innerHTML)
{
    let elem = document.createElement (elementType);
    if (className) {
        elem.className = className;
    }
    if (innerHTML) {
        elem.innerHTML = innerHTML;
    }
    parentElement.appendChild (elem);
    return elem;
}

function ResolveReferences (schema, parentNode, parentKey, resolvedKeys)
{
    let node = parentNode[parentKey];
    for (let key in node) {
        if (!node.hasOwnProperty (key)) {
            continue;
        }
        let childNode = node[key];
        if (typeof childNode === 'object') {
            ResolveReferences (schema, node, key, resolvedKeys);
        } else if (typeof childNode === 'string' && key == '$ref') {
            let refKey = childNode.substr (2);
            let refValue = schema[refKey];
            if (resolvedKeys.has (refKey)) {
                parentNode[parentKey] = {
                    type : refKey
                };
            } else {
                parentNode[parentKey] = refValue;
                parentNode[parentKey].title = refKey;
                resolvedKeys.add (refKey);
                ResolveReferences (schema, parentNode, parentKey, resolvedKeys);
                resolvedKeys.delete (refKey)
            }
        }
    }
}

function CreateCommandNameElement (parentElement, commandName, commandVersion)
{
    CreateElement (parentElement, 'div', 'command_name', commandName);
    CreateElement (parentElement, 'div', 'command_version', 'From version ' + commandVersion);
}

function CreateSchemaElement (parentElement, title, schema)
{
    if (schema === null) {
        return;
    }
    CreateElement (parentElement, 'div', 'scheme_title', title);    
    let schemeContainer = CreateElement (parentElement, 'div', 'scheme_container', null);
    ResolveReferences (schema, schema, 'properties', new Set ());
    let view = new JSONSchemaView (schema, 1);
    schemeContainer.appendChild (view.render ());
}

function RenderCommand (parentElement, command)
{
    CreateCommandNameElement (parentElement, command.name, command.version);
    let commandContainer = CreateElement (parentElement, 'div', 'command_container', null);
    CreateElement (commandContainer, 'div', 'command_description', command.description);
    CreateSchemaElement (commandContainer, 'Input parameters', command.inputScheme);
    CreateSchemaElement (commandContainer, 'Output parameters', command.outputScheme);
}

function RenderCommands (parentElement, commands)
{
    for (let command of commands) {
        RenderCommand (parentElement, command);
    }
}
