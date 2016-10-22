#!/usr/bin/python

import sys,getopt

def main(filename,argv):
	esHost = ''
	indexFormat =  ''
	intervalDays = 0

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
			intervalDays = int(arg)

	#TODO check if user didn't set a parameter
	#TODO check the right format of the parameters (if -e contains url and port, if interval is number etc)		

	print 'Starting with parameters\n* ElasticSeach Host='+esHost+'\n* Index Format='+indexFormat+'\n* Interval Days='+str(intervalDays)

	#Setup a connection to elastic search

	#Create a ES client

	#List all indicies

	#For all indicies get only that are matching to format

	#Some how split them (or get the information from inside them) and check them based on date. If they are older from current date - interval , delete them

	#Close connection and terminate



if __name__ == "__main__":
   main(sys.argv[0],sys.argv[1:])


