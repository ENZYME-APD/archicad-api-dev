
ghenv.Component.Name = 'Get All Classification Systems'
ghenv.Component.NickName = 'GetAllClassificationSystems'
ghenv.Component.Message = '0.1'
ghenv.Component.Category = 'ARCHICAD'
ghenv.Component.SubCategory = 'API3'
ghenv.Component.Description = '''
Collects all classifications systems
INPUT:
	PickSystem    : int  		: Picks Property group
						  

OUTPUT:
	ClassificationSystems 	    : Message 	 
	Name 						: String
	Name 						: String
'''



import  api2 as api 


ports = api.get_active_port()

_systems=[]
if len(ports)>0 and PickSystem is not None :
	for port in ports:
		_systems += api.getAllClassificationSystems(port)

	_class_name=[]
	for s in _systems:
		_class_name.append(s['name'])

	PickSystem_wrapped = api.get_wrapped_value(PickSystem,_class_name)
	ClassificationSystems = api.show_menu('CLASSIFICATION SYSTEMS',_class_name,PickSystem_wrapped)
	Name = _systems[PickSystem_wrapped]['name']
	Source = _systems[PickSystem_wrapped]['source']
	Version = _systems[PickSystem_wrapped]['version']
	Date = _systems[PickSystem_wrapped]['date']
	Description = _systems[PickSystem_wrapped]['description']
	ClassSystemID = _systems[PickSystem_wrapped]['guid']