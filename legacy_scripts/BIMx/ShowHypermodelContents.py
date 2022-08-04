
ghenv.Component.Name = 'Show Hypermodel Contents'
ghenv.Component.NickName = 'ShowHypermodelContents'
ghenv.Component.Message = '0.1'
ghenv.Component.Category = 'ARCHICAD_API'
ghenv.Component.SubCategory = 'Bimx'
ghenv.Component.Description = '''
'''
if HypermodelName is not None:
    Hyperlink = 'bimxapplication://showHypermodelContents?hypermodel={}'.format(HypermodelName)
    
