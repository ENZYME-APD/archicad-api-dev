from archicad import ACConnection

conn = ACConnection.connect ()

acc = conn.commands
act = conn.types

response = acc.ExecuteAddOnCommand (act.AddOnCommandId ('TapirCommand', 'PublishPublisherSet'), {
"publisherSetName" : "1 - Layouts",
"outputPath" : "C:\\Users\\Viktor\\Documents\\Alma"
})

print (response)
