
ghenv.Component.Name = 'Create Extension'
ghenv.Component.NickName = 'CreateExtension'
ghenv.Component.Message = '0.1'
ghenv.Component.Category = 'ARCHICAD_API'
ghenv.Component.SubCategory = 'Bimx'
ghenv.Component.Description = '''
'''
import json
from bimx_encoder import  encoder as e 
e=reload(e)
import datetime
now = str(datetime.datetime.now())

bimxx={}
if  BimxxFile is not None and\
    BakeBimxxFile is not None:


    # ProjectInfo is not None and\
    # ElementContextMenu is not None:
    if ExtensionName:bimxx['name'] = ExtensionName#+now 
    if devID:
        bimxx['developer_id'] = devID
    else:
        devID = '8ad9b618-3206-4f60-b7df-24f97986aa65' 
    if UpdateUrl:bimxx['update_url'] = UpdateUrl+'&raw=1'

    if HyperModelNames is not None:
        _hypermodelnames = json.loads(HyperModelNames)
        if isinstance(_hypermodelnames,dict):
            _hypermodelnames = [_hypermodelnames]
        bimxx['hyper_model_names'] = _hypermodelnames#[context_01]
    # bimxx['hyper_model_names'] = ["prj_bimx","WALLS"]

    url_var = [
    '$(hyper_model_name)',
    '$(project_id)',
    '$(project_name)',
    '$(first_measure_point)',
    '$(camera_pos)',
    '$(view_direction)'
    ]
    if ElementContextMenu is not None:
        context = json.loads(ElementContextMenu)
        # print context
        if isinstance(context,dict):
            context = [context]
        bimxx['elem_context_menu'] = context#[context_01]
    #-------------------
    prj_info =  {}
    if ProjectInfo is not None:
        _proj = json.loads(ProjectInfo)#[prj_info]
        if isinstance(_proj,dict):
            _proj = [_proj]
        bimxx['project_info'] = _proj

    if ElementInfo is not None:
        _proj = json.loads(ElementInfo)#[prj_info]
        #if isinstance(_proj,dict):
         #   _proj = [_proj]
        bimxx['elem_info'] = _proj
        
    if ModelInfo is not None:
        _proj = json.loads(ModelInfo)#[prj_info]
        #if isinstance(_proj,dict):
         #   _proj = [_proj]
        bimxx['model_info'] = _proj

    c = json.dumps(bimxx,indent=4)
    print c

    if BakeBimxxFile:
        with open(BimxxFile,'w') as f:
            f.write(c)
#        if EncryptExtension:
#            print 'Extension encrypted'
#            encoder = e.encoder_path()
#            e.encrypt(BimxxFile,encoder,overwrite=True)
#   Feature not implemented yet. Require bimxx encoder that can be found here
#   https://graphisoft.sharefile.com/d-s13ee1be5fc4d44caa108bd81d3c7196f
#   Input parameter name (type bool) <EncryptExtension>

else:
    print 'Connect all Inputs!!'