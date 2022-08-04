
ghenv.Component.Name = 'Set Classification Of Elements'
ghenv.Component.NickName = 'SetClassificationOfElements'
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

#https://archicadapi.graphisoft.com/JSONInterfaceDocumentation/#SetClassificationsOfElements

import  api2 as api 
ports = api.get_active_port()
port = ports[0]
run = api.get_global_toggle()

if len(ports)>0 and ElementsID is not None and ClassSystemID is not None and ClassGUID is not None:
	_elementsID = api.unpack(ElementsID)

	json_def = api.SetClassificationsOfElements(port,_elementsID,ClassSystemID,ClassGUID)

	result = api.connect(json_def,port)
	printToPanel = result['succeeded']
else: 
	printToPanel = 'Connect all INPUT wires'