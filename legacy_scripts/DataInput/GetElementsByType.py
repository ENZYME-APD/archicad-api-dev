ghenv.Component.Name = 'Get All elements by Type'
ghenv.Component.NickName = 'GetElementsByType'
ghenv.Component.Message = '0.1'
ghenv.Component.Category = 'ARCHICAD'
ghenv.Component.SubCategory = 'API3'
ghenv.Component.Description = '''
Collects GUIDS of all elements in a project by thier type
INPUT:
	ElementType  : int Choose type. Connect Number slider from 0 to 17
				
OUTPUT:
	printToPanel 	: string - Display list of all types. 
	ElementsOfType 	: dict - Elements packed to dictionary
'''

import api2 as p
reload(p)

ports = p.get_active_port()

el_types = p.getElementsTypes()

if ElementType is not None and isinstance(ElementType,int):
	wrapped_ElementType = p.get_wrapped_value(ElementType,el_types)

	printToPanel = p.show_menu('Element Types',el_types,wrapped_ElementType)

	choosen_type = el_types[wrapped_ElementType]


	_ElementsOfType=[]
	for port in ports:
		elem = p.getElementsByType(choosen_type,port)
		elem = p.unpack(elem)['elements']
		_ElementsOfType+=elem
	if SerializeElements:   
		ElementsOfType = p.packlist(_ElementsOfType)
	else:
		ElementsOfType = _ElementsOfType

	# ElementsOfType = p.pack('elements',_ElementsOfType)
else:
	printToPanel = 'CAUTION:\nConnect Number Slider to <ElementType> Input'

