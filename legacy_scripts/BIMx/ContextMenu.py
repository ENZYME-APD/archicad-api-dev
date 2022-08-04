
ghenv.Component.Name = 'Context menu'
ghenv.Component.NickName = 'Contextmenu'
ghenv.Component.Message = '0.1'
ghenv.Component.Category = 'ARCHICAD_API'
ghenv.Component.SubCategory = 'Bimx'
ghenv.Component.Description = '''
'''

import json
if Title is not None and URL is not None and Style is not None and Position is not None:
    _elem = {
        'title':Title,
        'url':URL,
        'style': Style,
        'position':Position

    }
    if shownOnlyIf is not None:
        _shownOnlyIf = json.loads(shownOnlyIf)
        _elem['shown_only_if']=_shownOnlyIf
    j = json.dumps(_elem,indent=4)
    Elem_context_menu = j
else:
    print 'Connect all Inputs!!'