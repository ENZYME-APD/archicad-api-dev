function CreateElement (parentElement, elementType, className, innerHTML)
{
    let element = document.createElement (elementType);
    if (className) {
        element.className = className;
    }
    if (innerHTML) {
        element.innerHTML = innerHTML;
    }
    parentElement.appendChild (element);
    return element;
}

function CreateSchemaElement (parentElement, title, schema)
{
    if (schema === null) {
        return;
    }
    CreateElement (parentElement, 'div', 'scheme_title', title);    
    let schemeContainer = CreateElement (parentElement, 'div', 'scheme_container', null);
    let view = new JSONSchemaView (schema, 1);
    schemeContainer.appendChild (view.render ());
}

function RenderCommand (parentElement, command)
{
    CreateElement (parentElement, 'div', 'command_name', command.name);
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
