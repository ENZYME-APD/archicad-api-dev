ghenv.Component.Name = 'Get All Elements'
ghenv.Component.NickName = 'GetAllElements'
ghenv.Component.Message = '0.1'
ghenv.Component.Category = 'ARCHICAD'
ghenv.Component.SubCategory = 'API3'
ghenv.Component.Description = '''
Collects GUIDS of all elements in a project 
				
OUTPUT:
	ElementsID 	: dict - Elements packed to dictionary
'''

import api2 as p


ports = p.get_active_port()

_ElementsID=[]
if len(ports)>0:
	# port = ports[0]
	for port in ports:
		el = p.getAllElements(port)
		el = p.unpack(el)
		_ElementsID+=el['elements']
	print type(_ElementsID),len(_ElementsID)
	
	if SerializeElements:
		ElementsID = p.packlist(_ElementsID) 
	else:
		ElementsID = _ElementsID 
	# ElementsID = p.pack('elements',_ElementsID) 
