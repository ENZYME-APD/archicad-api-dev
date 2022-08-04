
ghenv.Component.Name = 'Show Element In 3d Context'
ghenv.Component.NickName = 'showElementIn3dContext'
ghenv.Component.Message = '0.1'
ghenv.Component.Category = 'ARCHICAD_API'
ghenv.Component.SubCategory = 'Bimx'
ghenv.Component.Description = '''
'''

import json
import api2

show_type = {
'Show Hypermodel Contents':'showHypermodelContents',
'Show Element In 3d Context':'showElementIn3dContext',
'Show 2d Document':'show2dDocument',
'Install Extension':'installExtension'
}


if HypermodelName is not None and ElementID is not None:
    if len(ElementID)==36:
        elements_list = ElementID
    else:
        elements_list = json.loads(ElementID)
        elements_list = ','.join(elements_list)
        
        
    HypermodelName = HypermodelName.replace(' ','&nbsp')
    HYPERLINK = 'bimxapplication://showElementIn3dContext?hypermodel={}'.format(HypermodelName)
    ELEMENTS  = 'element_guids={}'.format(elements_list)
    _Hyperlink = '&'.join([HYPERLINK,ELEMENTS])
    if LinkName is not None:
        Hyperlink = '[{}]({})'.format(LinkName,_Hyperlink)
    else:
        Hyperlink = _Hyperlink