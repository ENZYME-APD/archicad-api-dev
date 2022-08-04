
ghenv.Component.Name = 'Get BuiltIn Property ID'
ghenv.Component.NickName = 'GetBuiltInPropertyID'
ghenv.Component.Message = '0.1'
ghenv.Component.Category = 'ARCHICAD'
ghenv.Component.SubCategory = 'API3'
ghenv.Component.Description = '''
Checks avaliable connection ports and dallows to pick one or all
INPUT:
	PropertyType    : int  		: Picks Property group
	Property        : int  		: Picks properties in group
						  

OUTPUT:
	PropertyGroups 	: Message 	:Property groups based on name prefix 
	PropertiesOfType 	: Message 	:properties in group

	PropertyID 			: string 	: GUID of property
'''


import api2 as api 

#read avaliable ports from GH global (sticky)
ports = api.get_port()
if ports == False:
    port = 0
else:
    port = ports[0]


if ports != False and len(ports)>0 and (PropertyType is not None and Property is not None):

	property_names = api.getBuiltInPropertyNames(port) # get names of builtIn properties
	property_types = api.getBuiltInPropertyTypes(port) # get types from names (first word before underscore)

	PropertyType_wrapped = api.get_wrapped_value(PropertyType,property_types) # wrapup input number slide node to fit list lenngth
	PropertyGroups  = api.show_menu('PROPERTY TYPES',property_types,PropertyType_wrapped)

	_properties_of_type = api.getBuiltInPropertiesOfType(property_names,port,property_types[PropertyType_wrapped]) 

	Property_wrapped = api.get_wrapped_value(Property,_properties_of_type)
	PropertiesOfType = api.show_menu('{} PROPERTIES'.format(property_types[PropertyType_wrapped]), _properties_of_type,Property_wrapped)

	property_name = _properties_of_type[Property_wrapped]

	# PropertyID = property_name
	PropertyID = api.getBuiltInPropertyId(property_name,port)

else:
	PropertyGroups = 'Plug INPUTS'