
ghenv.Component.Name = 'Value series'
ghenv.Component.NickName = 'ValueSeries'
ghenv.Component.Message = '0.1'
ghenv.Component.Category = 'ARCHICAD'
ghenv.Component.SubCategory = 'API3'
ghenv.Component.Description = '''Repeats value and pack to json object
'''

import json
if nRepeats and Value:
    _a = [Value for i in range(nRepeats)]
    SerializedValues = json.dumps(_a)