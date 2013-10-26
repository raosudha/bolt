#!/usr/bin/python
import sys, getopt
import os

def main(argv):
   inputdir = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["idir=","ofile="])
   except getopt.GetoptError:
      print 'preprocess_twitter_data.py -i <inputdir> -o <outputfile>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'test.py -i <inputdir> -o <outputfile>'
         sys.exit()
      elif opt in ("-i", "--idir"):
         inputdir = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
   print 'Input dir is "', inputdir
   print 'Output file is "', outputfile
   separate_out_tweets(inputdir, outputfile)

def separate_out_tweets(inputdir, outputfile):
	inputfiles = os.listdir(inputdir)
	ofile = open(outputfile, "w")
	for inputfile in inputfiles:
		ifile = open(os.path.join(inputdir, inputfile), "r")
		input = ifile.read()
		lines = input.split("\n")
		for line in lines:
			if(not line == None):
				if(len(line.split("\t")) > 1):
					ofile.write(line.split("\t")[1] + "\n")
		ifile.close()
	ofile.close()
if __name__ == "__main__":
	main(sys.argv[1:])

