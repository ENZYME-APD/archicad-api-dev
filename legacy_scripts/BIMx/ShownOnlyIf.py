
ghenv.Component.Name = 'Shown Only If'
ghenv.Component.NickName = 'ShownOnlyIf'
ghenv.Component.Message = '0.1'
ghenv.Component.Category = 'ARCHICAD_API'
ghenv.Component.SubCategory = 'Bimx'
ghenv.Component.Description = '''
'''
import json
_shownOnlyIf = {}
if element_guids is not None:
    _element_guids = json.loads(element_guids)
    _shownOnlyIf['element_guids'] = _element_guids
    # shownOnlyIf = json.dumps(_shownOnlyIf) 

_metadata ={}
if isPresent is not None:
    _isPresent = json.loads(isPresent)
    _metadata['is_present'] = _isPresent
    # _shownOnlyIf['metadata'] = _metadata
    # shownOnlyIf = json.dumps(_shownOnlyIf) 

if PropertyName is not None and PropertyValue is not None:
    _propertyNames = json.loads(PropertyName)
    _propertyValues = json.loads(PropertyValue)
    _equals = []
    for i in range(
                min(
                    len(_propertyNames),len(_propertyValues)
                )
            ):
        _equals.append(
                {
                'key':_propertyNames[i],
                'value':_propertyValues[i],
                }
            )
    _metadata['equals'] = _equals

if (PropertyName is not None and PropertyValue is not None) or isPresent is not None:
    _shownOnlyIf['metadata'] = _metadata
shownOnlyIf = json.dumps(_shownOnlyIf) 