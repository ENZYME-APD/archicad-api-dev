
ghenv.Component.Name = 'Deserialize List'
ghenv.Component.NickName = 'DeserializeList'
ghenv.Component.Message = '0.1'
ghenv.Component.Category = 'ARCHICAD'
ghenv.Component.SubCategory = 'API3'
ghenv.Component.Description = '''Deserialize json object in to list

'''

import api2

if SerializedList is not None and '[' in SerializedList :
    List = api2.unpack(SerializedList)
    