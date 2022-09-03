from archicad import ACConnection

conn = ACConnection.connect ()

acc = conn.commands
act = conn.types

response = acc.ExecuteAddOnCommand (act.AddOnCommandId ('TapirCommand', 'GetArchicadLocation'))
print (response)
