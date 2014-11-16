import json
jsonFile=open('web.log')
for line in jsonFile:
	data=json.loads(line)
	for field in data.keys(): print field
