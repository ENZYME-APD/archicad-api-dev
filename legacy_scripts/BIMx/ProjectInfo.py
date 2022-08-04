
ghenv.Component.Name = 'Project Info'
ghenv.Component.NickName = 'ProjectInfo'
ghenv.Component.Message = '0.1'
ghenv.Component.Category = 'ARCHICAD_API'
ghenv.Component.SubCategory = 'Bimx'
ghenv.Component.Description = '''
'''

import json
# if Title is not None and URL is not None:
#     titles = Title.split('\n')
#     urls  = URL.split('\n')
#     if len(titles)!=len(urls):
#         ProjectInfo =  'differetn'
#     else:
#         _projectInfo=[]

#         for i,j in enumerate(titles):
#             _projectInfo.append({'title':titles[i],'url':urls[i]})
#         j = json.dumps(_projectInfo,indent=4)
#         ProjectInfo = j
# else:
#     ProjectInfo = 'INPUTS Please'



import json
if Title is not None and URL is not None:
    _elem = {
        'title':Title,
        'url':URL
    }

    j = json.dumps(_elem,indent=4)
    ProjectInfo = j
