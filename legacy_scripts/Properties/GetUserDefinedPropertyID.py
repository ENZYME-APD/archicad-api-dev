
ghenv.Component.Name = 'Get UserDefined Property ID'
ghenv.Component.NickName = 'GetUserDefinedPropertyID'
ghenv.Component.Message = '0.1'
ghenv.Component.Category = 'ARCHICAD'
ghenv.Component.SubCategory = 'API3'
ghenv.Component.Description = '''
Picks GUID of User defined Property
INPUT:
	PropertyGroup    : int  		: Picks Property group
	Property         : int  		: Picks properties in a group
						  

OUTPUT:
	printToPanel 	    : Message 	 
	PropertyGroups 	    : Message 	:Property groups based on name prefix 
	PropertiesInGroup	: Message 	:properties in a group

	PropertyID 			: string 	: GUID of property
'''


import api2 as api 
reload(api)
ports = api.get_port()
port = ports[0]

run  = api.get_global_toggle()
print 'sdfs',run
ud_groups , ud_properties = api.getUserDefinedPropertyGroups(port)

if len(ports)>0 or PropertyGroups is not None and Property is not None: 
	PropertyGroup_wrapped = api.get_wrapped_value(PropertyGroup,ud_groups) 
	_group = ud_groups[PropertyGroup_wrapped]
	_properties_in_group = ud_properties[_group]
	Property_wrapped = api.get_wrapped_value(Property,_properties_in_group) 
	print 	Property,Property_wrapped

	PropertyGroups = api.show_menu('GROUPS',ud_groups,PropertyGroup_wrapped)



	PropertiesInGroup = api.show_menu(
		'PROPERTIES IN GROUP "{}"'.format(_group),
		_properties_in_group,
		Property_wrapped
		)
	_property_name = _properties_in_group[Property_wrapped]

	if run:
		PropertyID  = api.getUserDefinedPropertyId(_group,_property_name,port)
		printToPanel = 'Global toggle is on'
	else:
		PropertyID  = ''
		printToPanel = 'GH scheme is globally turned off. Use Input <RunGlobally> in PickPort Node\n'
		

else:
	printToPanel = '''
INPUT:
	PropertyGroups: int
	Property: 		int
OUTPUT:
	PropertyGroups 		:list of groups printed to Panel node
	PropertiesInGroup 	:list of properties in chosen group  printed to Panel node
	PropertyID 			:str Property GUID as string
	'''

# choosen_property_name = ud_properties[Property_wrapped]
