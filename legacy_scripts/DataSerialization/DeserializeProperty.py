ghenv.Component.Name = 'Deserialize Property'
ghenv.Component.NickName = 'DeserializeProperty'
ghenv.Component.Message = '0.1'
ghenv.Component.Category = 'ARCHICAD'
ghenv.Component.SubCategory = 'API3'
ghenv.Component.Description = '''
Deserialize json object that represents property dictionary
				
OUTPUT:
	
'''

import api2 as api

if SerializedProperty is not None:
	lista=[]
	lista = api.unpack(SerializedProperty)
	print lista
	# key_value = lista.items()
	# key = key_value[0][0]
	# _Values = lista[key]


	_ParameterValue=[]
	_ParameterType=[]
	_ParameterStatus=[]

	for v in lista:
		_ParameterValue.append(v['value'])
		_ParameterType.append(v['type'])
		_ParameterStatus.append(v['status'])

	PropertyValue= _ParameterValue
	PropertyType= _ParameterType
	PropertyStatus= _ParameterStatus