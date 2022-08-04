
ghenv.Component.Name = 'Get BIMx Details'
ghenv.Component.NickName = 'GetBIMxDetails'
ghenv.Component.Message = '0.1'
ghenv.Component.Category = 'ARCHICAD_API'
ghenv.Component.SubCategory = 'Bimx'
ghenv.Component.Description = '''Gets metadata from BIMx file
'''

import json
import api2
api2=reload(api2)



if BIMxFile is not None:
    xmlData = api2.extract_xml_from_bimx(BIMxFile)
    root =  api2.parseXML(xmlData)

    # xmlData = api2.extract_xml_from_bimx(BIMxFile)
    # print xmlData
    # root =  api2.parseXML(xmlData)

    ProjectName =  root.find("ProjectInfo/Project").text
    HypermodelName =  root.find("HyperModel").text
    City =  root.find("ProjectInfo/Place").attrib['city']
    strCoordinates =  root.find("ProjectInfo/Place").attrib['coordinates']
    strCoordinates = strCoordinates.replace('+','')
    _Coordinates = strCoordinates.split(',')
    _Coordinates = [float(i) for i in _Coordinates]
    Coordinates = api2.packlist(_Coordinates)
    # City =  root.find("ProjectInfo/Place[@city]")
    # print ProjectName 
    # HypermodelName 
    # print Place 