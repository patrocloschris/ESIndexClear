#!/usr/bin/python

import sys,getopt,re


def check_parameters(esHost,indexFormat,interval):
	#Check esHost
	if esHost is None:
		print 'Elastic search host is empty'
		return false
	host_split = esHost.split(":")
	if len(host_split)>2:
		print 'Elastic search host is not a proper url'
		return false
	res_match= re.match(r'[a-z][a-z0-9]+',host_split[0],re.I | re.M) 
	if not res_match:
		pat = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
		res_match = pat.match(host_split[0])
		if not res_match:
			print 'Elastic search host is not a valid domain'
			return false
	if len(host_split)==2:
		res_match= re.match(r'^[0-9]+',host_split[1],re.I | re.M)	
		if not res_match:
		print 'Elastic search port is not a valid number'
			return false
	# Check indexFormat
	if indexFormat is None:
		print 'Index Format is empty'
		return false
	try:
    	re.compile(indexFormat)
	except re.error:
		print 'Index Format can not be recognized as a regex string'
		return false
	#Check interval	
	if interval is None:
		print 'Interval is empty'
		return false
	res_match= re.match(r'^[1-9][0-9]*',intervalDays,re.I | re.M)	
	if not res_match:
		print 'Interval can not recognized as a valid number'
		return false
	return true	



def main(filename,argv):
	esHost = None
	indexFormat =  None
	intervalDays = None

	# Get input parameters
	try:
		opts, args = getopt.getopt(argv,"he:f:i:")
	except getopt.GetoptError:
		print filename+' -e <elasticsearch host> -f <index format> -i <the number of the last days that you want to keep indexes>'
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

	if not check_parameters(esHost,indexFormat,interval):
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


