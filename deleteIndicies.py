#!/usr/bin/python

import sys,getopt,re

def eprint(msg):
	sys.stderr.write(msg)

def check_parameters(esHost,indexFormat,intervalDays):
	#Check esHost
	if esHost is None:
		eprint('Elastic search host is empty')
		return False
	host_split = esHost.split(":")
	if len(host_split)>2:
		eprint('Elastic search host is not a proper url')
		return False
	res_match= re.match(r'[a-z][a-z0-9]+',host_split[0],re.I | re.M) 
	if not res_match:
		pat = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
		res_match = pat.match(host_split[0])
		if not res_match:
			eprint('Elastic search host is not a valid domain')
			return False
	if len(host_split)==2:
		res_match= re.match(r"^\d{1,5}$",host_split[1])	
		if not res_match:
			eprint('Elastic search port is not a valid number')
			return False
	# Check indexFormat
	if indexFormat is None:
		print 'Index Format is empty'
		return False
	try:
		re.compile(indexFormat)
	except re.error:
		print 'Index Format can not be recognized as a regex string'
		return False
 	#Check intervalDays	
	if intervalDays is None:
		print 'Interval is empty'
		return False
	res_match= res_match= re.match(r"^\d{1,5}$",intervalDays)	
	if not res_match:
		print 'Interval can not recognized as a valid number'
		return False
	return True	



def main(filename,argv):
	esHost = None
	indexFormat =  None
	intervalDays = None

	# Get input parameters
	try:
		opts, args = getopt.getopt(argv,"he:f:i:")
	except getopt.GetoptError:
		eprint(filename+' -e <elasticsearch host> -f <index format> -i <the number of the last days that you want to keep indexes>\n')
		sys.exit(2)
   	for opt, arg in opts:
		if opt == '-h':
			print filename+' -e <elasticsearch host> -f <index format> -i <the number of the last days that you want to keep indexes>'
			sys.exit()
		elif opt in ("-e"):
			esHost = arg
		elif opt in ("-f"):
			indexFormat = arg
		elif opt in ("-i"):	
			intervalDays = arg

	if not check_parameters(esHost,indexFormat,intervalDays):
		print 'Parameters:\n* ElasticSeach Host='+esHost+'\n* Index Format='+indexFormat+'\n* Interval Days='+intervalDays
		sys.exit(2)
	else:
		print 'Starting with parameters:\n* ElasticSeach Host='+esHost+'\n* Index Format='+indexFormat+'\n* Interval Days='+str(intervalDays)
		intervalDays = int(intervalDays)	


	#Setup a connection to elastic search



	#Create a ES client

	#List all indicies

	#For all indicies get only that are matching to format

	#Some how split them (or get the information from inside them) and check them based on date. If they are older from current date - interval , delete them

	#Close connection and terminate



if __name__ == "__main__":
   main(sys.argv[0],sys.argv[1:])


