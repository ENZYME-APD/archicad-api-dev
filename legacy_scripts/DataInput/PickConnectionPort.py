ghenv.Component.Name = 'Pick connection port'
ghenv.Component.NickName = 'PickPort'
ghenv.Component.Message = '0.1'
ghenv.Component.Category = 'ARCHICAD'
ghenv.Component.SubCategory = 'API3'
ghenv.Component.Description = '''
Checks avaliable connection ports and dallows to pick one or all
INPUT:
	Synchronise  : bool Checks avaliable ports. 
						For performance reason should be set to false after first run
	pickPort     : int  Connect Integer type <Number Node> 
	RunGlobally  : bool Turns on/off global variable on which depends  other nodes performance.   
OUTPUT:
	printToPanel : string Message
'''
# ghenv.Component.AdditionalHelpFromDocStrings = '1'



import api2 as api
reload(api)
printToPanel = Synchronise
api.set_global_toggle(RunGlobally)
p=None
ports = []

if Synchronise == True:

    ports = api.open_ports()
    
    p = api.get_port()

    if len(p)>1:
        p =  p + [p]

if p and pickPort is not None:
    wrapped_pickPort = api.get_wrapped_value(pickPort,p)
    printToPanel = api.show_menu('Avaliable ports',p,wrapped_pickPort)
    api.set_active_port(p[wrapped_pickPort])
else:
    printToPanel = 'Plug Boolean Toggle node to Synchronise Input\nand Number Slider to pickPort Input'