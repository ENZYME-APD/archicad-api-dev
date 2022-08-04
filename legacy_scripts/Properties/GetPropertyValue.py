
ghenv.Component.Name = 'Get Property Value'
ghenv.Component.NickName = 'GetPropertyValue'
ghenv.Component.Message = '0.1'
ghenv.Component.Category = 'ARCHICAD'
ghenv.Component.SubCategory = 'API3'
ghenv.Component.Description = '''
Gets value of given property GUID
INPUT:
	PropertyID         : string  : GUID of Property
	ElementsID         : dict    : dictionary of elements GUID
	UnpackValue        : dict    : dictionary of elements GUID
						  

OUTPUT:
	PropertyValue 	    : dict 	 : Dicionary with 3 keys: value,type and status
	
'''


import api2 as api 

ports = api.get_port()
port = ports[0]


if len(ports)>0 and (PropertyID is not None and ElementsID is not None):
	# if isinstance(ElementsID,str):
	if len(ElementsID)!=36:
		ElementsID = api.unpack(ElementsID)
	else:
		ElementsID = [ElementsID]


	property_value = api.getPropertyValue(ElementsID,[PropertyID],port)
	# print property_value



# ports = api.get_port()
# port = ports[0]

values=[]
if len(ports)>0 and (PropertyID is not None and ElementsID is not None):
	el = ElementsID
	# el = api.unpack(ElementsID)
	# el = api.unpack(ElementsID)['elements']
	property_value = api.getPropertyValue(el,[PropertyID],port)
	for i in property_value:
		values.append(i)
		# values.append(i['value'])

	if SerializeList:
		PropertyValue = api.packlist(property_value)	
	else:
		__val=[]
		for i in values:
			__val.append(i['value'])
			PropertyValue = __val
		# PropertyValue = values