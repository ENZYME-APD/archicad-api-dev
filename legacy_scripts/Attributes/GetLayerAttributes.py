
ghenv.Component.Name = 'Get Layer Attributes'
ghenv.Component.NickName = 'GetLayerAttributes'
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

import  api2 as api 
reload(api)
ports = api.get_active_port()
port = ports[0]
run = api.get_global_toggle()

_layers_guid = api.GetAttributesByType('Layer',port)
f = api.GetAttributes('Layer',_layers_guid)


# jsonQuerry_layers_attributes = [api.GetAttributes('Layer',guid) for guid in _layers_guid]
# print jsonQuerry_layers_attributes
result = api.connect(f,port)
# print result
_layerName=[]
_isLocked=[]
_isHidden=[]
_isWireframe=[]
_interGroup=[]
for i in result['result']['attributes']:
	_layerName.append(i['layerAttribute']['name'])
	_isLocked.append(i['layerAttribute']['isLocked'])
	_isHidden.append(i['layerAttribute']['isHidden'])
	_isWireframe.append(i['layerAttribute']['isWireframe'])
	_interGroup.append(i['layerAttribute']['intersectionGroupNr'])

Name = _layerName
isLocked = _isLocked
isHidden = _isHidden
isWireframe = _isWireframe
intersectionGroupNr = _interGroup
