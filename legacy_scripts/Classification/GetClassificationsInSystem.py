
ghenv.Component.Name = 'Get Classifications In System'
ghenv.Component.NickName = 'GetClassificationsInSystem'
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

#https://archicadapi.graphisoft.com/JSONInterfaceDocumentation/#GetAllClassificationsInSystem

import  api2 as api 
ports = api.get_active_port()
port = ports[0]
classifications_menu=[]
className 	= []
classId 	= []
classDesc 	= []
classGUID 	= []
if len(ports)>0 and PickClass is not None:
	# for port in ports:
	classes = api.GetAllClassificationsInSystem(port,ClassSystemID)
	for c in classes:
		classifications_menu.append(c['classificationItem']['id'])
		classId.append(c['classificationItem']['id'])
		className.append(c['classificationItem']['name'])
		classDesc.append(c['classificationItem']['description'])
		classGUID.append(c['classificationItem']['classificationItemId']['guid'])
		try:
			for child in c['classificationItem']['children']:
				classifications_menu.append('\t\t|__\t'+child['classificationItem']['id'])
				classId.append(child['classificationItem']['id'])
				classGUID.append(child['classificationItem']['classificationItemId']['guid'])
				className.append(child['classificationItem']['name'])
				classDesc.append(child['classificationItem']['description'])

		except:
			pass
	PickClass_wrapped = api.get_wrapped_value(PickClass,classifications_menu)
	printToPanel = api.show_menu('CLASSIFICATIONS IN {}'.format('system'),classifications_menu,PickClass_wrapped)
	
	ClassID = classId[PickClass_wrapped]
	ClassGUID = classGUID[PickClass_wrapped]
	ClassName = className[PickClass_wrapped]
	ClassDescription = classDesc[PickClass_wrapped]
	# for c  in classifications:

	# 	print c
else:	
	print 'Connect INPUT'