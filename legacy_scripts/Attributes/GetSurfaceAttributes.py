
ghenv.Component.Name = 'Get Surface Attributes'
ghenv.Component.NickName = 'GetSurfaceAttributes'
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

import Rhino

from System.Drawing import Color

def createColor(__color):
	attr = Rhino.DocObjects.ObjectAttributes()
	attr.ColorSource = Rhino.DocObjects.ObjectColorSource.ColorFromObject
	attr.ObjectColor = Color.FromArgb(__color[3],__color[0],__color[1],__color[2])
	return attr.ObjectColor

import  api2 as api 
import json
reload(api)
ports = api.get_active_port()
port = ports[0]
run = api.get_global_toggle()

def getAttributeDetails(attr,port):
	_surface_guid = api.GetAttributesByType(attr,port)
	f = api.GetAttributes(attr,_surface_guid)
	result = api.connect(f,port)
	return result['result']

def _convertColor(color,trans):
	r=int(color['red']*255)
	g=int(color['green']*255)
	b=int(color['blue']*255)
	t = 255-trans
	
	r= min(r,255)
	g= min(g,255)
	b= min(b,255)
	# t=min(t,255)
	
	return [r,g,b,t]
result = getAttributeDetails('Surface',port)
# print json.dumps(result,indent=4)
_matName = []
_surfaceColor =[]
_surfaceTxt =[]

for i in result['attributes']:
	_matName.append(i['surfaceAttribute']['name'])
	__surfColor = (i['surfaceAttribute']['surfaceColor'])
	try:
		__surfTxt = (i['surfaceAttribute']['texture']['name'])
	except:
		__surfTxt = 0
	# print json.dumps(__surfTxt,indent=4)
	_surfaceTxt.append(__surfTxt)
	__surftransparency = (i['surfaceAttribute']['transparency'])
	value = _convertColor(__surfColor,__surftransparency)
	# print 255-__surftransparency
	_surfaceColor.append(createColor(value))

Color = _surfaceColor
Name = _matName
TextureName = _surfaceTxt
# Color = _color

# # jsonQuerry_layers_attributes = [api.GetAttributes('Layer',guid) for guid in _layers_guid]
# print jsonQuerry_layers_attributes
# _layerName=[]
# _isLocked=[]
# _isHidden=[]
# _isWireframe=[]
# _interGroup=[]
# for i in result['result']['attributes']:
# 	_layerName.append(i['layerAttribute']['name'])
# 	_isLocked.append(i['layerAttribute']['isLocked'])
# 	_isHidden.append(i['layerAttribute']['isHidden'])
# 	_isWireframe.append(i['layerAttribute']['isWireframe'])
# 	_interGroup.append(i['layerAttribute']['intersectionGroupNr'])

# Name = _layerName
# isLocked = _isLocked
# isHidden = _isHidden
# isWireframe = _isWireframe
# intersectionGroupNr = _interGroup
