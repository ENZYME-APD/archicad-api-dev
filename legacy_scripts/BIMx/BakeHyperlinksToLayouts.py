
ghenv.Component.Name = 'Bake Hyperlinks To Layouts'
ghenv.Component.NickName = 'BakeHyperlinksToLayouts'
ghenv.Component.Message = '0.1'
ghenv.Component.Category = 'ARCHICAD_API'
ghenv.Component.SubCategory = 'Bimx'
ghenv.Component.Description = '''Creates link to Layout embeded in BIMx file
'''

import json
import urllib
import api2
import csv
api2=reload(api2)



if BIMxFile is not None and CSVFile is not None:
    xmlData = api2.extract_xml_from_bimx(BIMxFile)
    root = api2.parseXML(xmlData)
    itemsAndFolders = root.findall('HyperDocument')
    _hyperModelName = root.find("HyperModel").text
    _hyperModelName = _hyperModelName.replace(' ', '%20')

    layoutName,layoutID = api2.getLayouts(itemsAndFolders) 

   
    views=[]
    views.append(['HYPERMODEL NAME',_hyperModelName])
    views.append(['LAYOUT NAME','HYPERLINK TO LAYOUT'])
    LINK_BASE = 'bimxapplication://Show2dDocument?hypermodel={0}&layoutGuid={1}'
    for i,j in enumerate(layoutName):
        views.append([layoutName[i],LINK_BASE.format(_hyperModelName,layoutID[i])])
    
    if BakeHyperlinks:

        with open(CSVFile,'w') as file:
            writer = csv.writer(file)
            for row in views:
                writer.writerow(row)
            file.close()