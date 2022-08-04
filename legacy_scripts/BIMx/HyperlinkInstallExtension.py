import urllib
ghenv.Component.Name = 'Hyperlink Install Extension.ghuser'
ghenv.Component.NickName = 'HyperlinkInstallExtension'
ghenv.Component.Message = '0.1'
ghenv.Component.Category = 'ARCHICAD_API'
ghenv.Component.SubCategory = 'Bimx'
ghenv.Component.Description = '''Doeasn work with Google drive yet
and custom repositories
Only dropbox tested and working
'''
if RepoURL is not None:
    if 'dropbox'in RepoURL:
        RepoURL+='&raw=1'
    RepoURL = urllib.quote(RepoURL)
    Hyperlink = 'bimxapplication://installExtension?url={}'.format(RepoURL)

