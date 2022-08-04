SubCategory = 'Bimx'
ghenv.Component.Description = '''Creates request link
'''
import socket
import json
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip

if domain is None:
    domain = get_ip()
if port is None:
    port=''
else:
    port = ':'+port
if endpoint is None:
    endpoint = '/'
else:
    endpoint = '/'+endpoint
if Parameters is None:
    _parameters = ''
else:
    if '[' in Parameters:
        _parameters = json.loads(Parameters)
        _parameters = '&'.join(_parameters)
    else:
        _parameters = Parameters
    _parameters = '?' + _parameters
    
Address = 'http://{}{}{}'.format(domain,port,endpoint) + _parameters