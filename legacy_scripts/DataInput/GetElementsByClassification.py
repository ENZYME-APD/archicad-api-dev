
ghenv.Component.Name = 'Get Elements by Classification'
ghenv.Component.NickName = 'GetElementsByClassification'
ghenv.Component.Message = '0.1'
ghenv.Component.Category = 'ARCHICAD_API'
ghenv.Component.SubCategory = 'Classification'
ghenv.Component.Description = '''
Collects all classifications systems
INPUT:
	PickSystem    : int  		: Picks Property group
						  

OUTPUT:
	ClassificationSystems 	    : Message 	 
	Name 						: String
	Name 						: String
'''

# https://archicadapi.graphisoft.com/JSONInterfaceDocumentation/#GetElementsByClassification

import  api2 as api 
ports = api.get_active_port()
port = ports[0]
run = api.get_global_toggle()


if len(ports)>0 and ClassGUID is not None:
    
	_elementsID = api.GetElementsByClassification(port,ClassGUID)

	if SerializeElements:   
		ElementsID = _elementsID
	else:
		ElementsID = api.unpack(_elementsID)
		
else:
	printToPanel = 'Connect all inputs'