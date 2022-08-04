

ghenv.Component.Name = 'ARCHICAD Schedule'
ghenv.Component.NickName = 'ARCHICADSchedule'
ghenv.Component.Message = '0.1'
ghenv.Component.Category = 'ARCHICAD'
ghenv.Component.SubCategory = 'API3'
ghenv.Component.Description = '''Reads archicad's schedule saved 
as tabbed txt  file

'''
import api2 as api
import csv
import json
# print(csvFile)
if Delimiter is None:
    Delimiter = '\t'
data = []
ids = []
headers = []
_headers = []
if IdFields is not None and ValuesFields is not None and csvFile is not None:
	with open(csvFile, 'r') as f:
		reader = csv.reader(f,delimiter=Delimiter)
		for row in reader:
			_headers.append(row)
		headers = _headers[0]

	wrapped_IdFields = api.get_wrapped_value(IdFields,headers)
	wrapped_valuesFields = api.get_wrapped_value(ValuesFields,headers)
	printHeaders = api.show_menu_two_inputs('DATA HEADERS',headers,wrapped_IdFields,wrapped_valuesFields)
	# printHeaders = api.show_menu('DATA HEADERS',headers,wrapped_IdFields)





	with open(csvFile, 'r') as f:
		csvData = csv.reader(f,delimiter=Delimiter)
		
		for row in csvData:
			data.append(row[wrapped_IdFields])
			ids.append(row[wrapped_valuesFields])
		data.pop(0)
		ids.pop(0)



	# pack = json.dumps({'elements':data},)
	ElementsID = api.packlist(data)
	Values = api.packlist(ids)

	# Values = ids
else:
	printHeaders = 'Connect number sliders to IdFields and valuesFields Inputs\nConnect FilePath node to csvFile Input'