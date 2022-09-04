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
    let nameElement = CreateElement (parentElement, 'div', 'command_name', command.name);
    CreateElement (nameElement, 'span', 'command_version', command.version);
    let commandContent = CreateElement (parentElement, 'div', 'command_content', null);
    commandContent.style.display = 'none';
    
    let isGenerated = false;
    parentElement.addEventListener ('click', () => {
        if (!isGenerated) {
            CreateElement (commandContent, 'div', 'command_description', command.description);
            CreateSchemaElement (commandContent, 'Input parameters', command.inputScheme);
            CreateSchemaElement (commandContent, 'Output parameters', command.outputScheme);
            isGenerated = true;
        }
        if (commandContent.style.display === 'block') {
            commandContent.style.display = 'none';
        } else {
            commandContent.style.display = 'block';
        }
    });
}

function RenderCommands (parentElement, commands)
{
    for (let command of commands) {
        let commandContainer = CreateElement (parentElement, 'div', 'command_container', null);
        RenderCommand (commandContainer, command);
    }
}
