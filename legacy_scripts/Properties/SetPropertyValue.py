
ghenv.Component.Name = 'Set Property Value'
ghenv.Component.NickName = 'SetPropertyValue'
ghenv.Component.Message = '0.1'
ghenv.Component.Category = 'ARCHICAD'
ghenv.Component.SubCategory = 'API3'
ghenv.Component.Description = '''
Sets value of given property GUID
INPUT:
	PropertyID         : string  : GUID of Property
	ElementsID         : dict    : dictionary of elements GUID
	SetValue           : dict    : values packed
						  

OUTPUT:
	PropertyValue 	    : dict 	 : Dicionary with 3 keys: value,type and status
	
'''

import api2 as api
reload(api)


ports = api.get_port()
port = ports[0]

run = api.get_global_toggle()

# def convert_types(value,type_name):
# 	if type_name=='number':return float(value)
# 	if type_name=='string':return str(value)
if len(ports)>0 and (PropertyID is not None and ElementsID is not None and SetValue is not None):
	_elements = api.unpack(ElementsID)
	# _elements = api.unpack(ElementsID)['elements']
	property_value = api.getPropertyValue(_elements,[PropertyID],port)
	
	types = [t['type'] for t in property_value]
	new_values = api.unpack(SetValue)
	# new_values = api.unpack(SetValue)['values']
	# todo: recognize type !!
	types_values = zip(new_values,types)



	
	for i in range(len(new_values)):
		property_value[i]['value'] = api.convert_types(new_values[i],types[i])
		property_value[i]['type'] =  types[i]
		# property_value[i]['value'] =  new_values[i]
	
	# print property_value
	
	if run:
		printToPanel = api.setPropertyValue(_elements,PropertyID,property_value,port)
	else:
		printToPanel = 'GH scheme is globally turned off. Use Input <RunGlobally> in PickPort Node'
else: 
	printToPanel = '''
INPUT:
	PropertyID : string
	ElementsID : list
OUTPUT:
	printToPanel: message
	'''
