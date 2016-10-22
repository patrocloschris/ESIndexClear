#!/usr/bin/python
import sys,getopt,re
from datetime import datetime,timedelta
from elasticsearch import Elasticsearch
from elasticsearch.client import CatClient
from elasticsearch.client import IndicesClient

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
	es = Elasticsearch([esHost],sniff_on_start=True)
	cat_client = CatClient(es)
	index_client = IndicesClient(es)

	#List all indices
	indices = cat_client.indices(h='index').split('\n')

	pat = re.compile(indexFormat)
	back_interval_days = datetime.now() - timedelta(days=intervalDays)


	for index in indices:
		clean_index = index.strip()
		res = pat.match(clean_index)
		#For all indices get only that are matching to format
		if res:
			index_timestamp=index_client.get(index=clean_index,feature='_settings')[clean_index]['settings']['index']['creation_date']
			#convert epoc timestamp to date
			index_date = datetime.fromtimestamp(float(index_timestamp)/1000.0)
			#compare dates , if true delete it
			if index_date < back_interval_days:
				print 'Deleting index => '+clean_index
				index_client.delete(index=clean_index)



if __name__ == "__main__":
   main(sys.argv[0],sys.argv[1:])




########## Pending ##############
#TODO set timeout to ES requests
#TODO add question ask if the user wants to delete that index and a force option to delete without asking
#TODO in parameter validation use buildin function for url validation
