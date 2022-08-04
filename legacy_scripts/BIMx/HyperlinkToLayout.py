
ghenv.Component.Name = 'Hyperlink To Layout'
ghenv.Component.NickName = 'HyperlinkToLayout'
ghenv.Component.Message = '0.1'
ghenv.Component.Category = 'ARCHICAD_API'
ghenv.Component.SubCategory = 'Bimx'
ghenv.Component.Description = '''Creates link to Layout embeded in BIMx file
'''

import json
import urllib
import api2
api2=reload(api2)



if BIMxFile is not None:
    xmlData = api2.extract_xml_from_bimx(BIMxFile)
    # print xmlData 
    viewsInBIMx = api2.parseXML(xmlData)
    itemsAndFolders = viewsInBIMx.findall('HyperDocument')
    # print itemsAndFolders
    items = []
    
    layoutID= []
    layoutName =[]
    itemType =[]
    hypermodelName =  viewsInBIMx.find("HyperModel").text

    # def addItem(array,item):
    #     array.append(item)
        
    # def openFolder(array,folder):
    #     for f in folder:
    #         if f.tag=='Item':addItem(array,f)
    #         if f.tag=='Folder':openFolder(array,f)

    # def getLayouts(itemsAndFolders):
    #     _layoutName = []
    #     _layoutID   = []
    #     _items= []
    #     for j,i in enumerate(itemsAndFolders[0]):
    #         if i.attrib.has_key('type') == False:
    #             if i.tag=='Item':addItem(_items,i)
    #             if i.tag=='Folder':openFolder(_items,i)
    #     for item in _items:
            
    #         _layoutName.append(item.attrib['title'])
    #         _layoutID.append(item.attrib['id'])
    #     return _layoutName,_layoutID
    layoutName,layoutID = api2.getLayouts(itemsAndFolders)   
    
    wrapped_PickLayout = api2.get_wrapped_value(PickLayout,layoutName)
    
    Layouts = api2.show_menu(
        'LAYOUTS IN "{}" BIMx'.format(hypermodelName),
        layoutName,wrapped_PickLayout
        )

    LINK_BASE = 'bimxapplication://Show2dDocument?hypermodel={0}&layoutGuid={1}'.format(hypermodelName,layoutID[wrapped_PickLayout])
    LINK_BASE = LINK_BASE.replace(' ','%20')

    if HyperlinkName is None:
        LayoutHyperlink = LINK_BASE
    else:
        LayoutHyperlink = '[{0}]({1})'.format(HyperlinkName,LINK_BASE)
    # LayoutHyperlink = urllib.quote(LINK_BASE)
