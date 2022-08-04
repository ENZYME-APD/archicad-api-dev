Description = '''
Output elements guids from Archicad element containers                
INPUT:
    Elements from Archicad container. All types allowed
OUTPUT:
    ElementsID  : Json object consist of collected guids
'''

import api2 
reload(api2)

if Elements is not None:
    ElementsID = str(Elements.Guid)