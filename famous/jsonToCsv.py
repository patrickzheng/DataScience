import sys
import json
#jsonFile=open('spam.log')
jsonFile=open(sys.argv[1])
outFile=open(sys.argv[1]+'.csv','w')
counter=0
res=set()
keys=['uid','visit_id','tstamp','campaign','experiments','action','query']
for line in jsonFile:
	counter+=1
	data=json.loads(line)
	if counter<500000: 
		#print data
		for field in data.keys(): 
			print field+':'+str(data[field])
			res.add(field)
		for field in keys:
			if field in data.keys():
				outFile.write('"'+str(data[field])+'",')
			else:
				outFile.write('"'+' '+'",')
		outFile.write('\n')
jsonFile.close()
outFile.close()
print res
