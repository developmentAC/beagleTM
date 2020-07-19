#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# # Oliver ######## . # #       # .  #
# # Bonham ######## . # #    # .  #
# # Carter ######## . # # # .  #
# ################# . # # ############
# ################# . # # # .  #
# ################# . # #    # .  #
# ################# . # #       # .  #
#
#
#
#
#

# DATE_STR = "19 July 2020"
# VERSION = "2_iii"
# AUTHOR = "Oliver Bonham-Carter"
# AUTHORMAIL = "obonhamcarter@allegheny.edu"

# """The driver of the whole thing."""


# import libraries
import os, sys
import math
import beagleTM2_parser_helperCode as hc


# Notes: to format nxml files into human readable formats
#ref: https://www.freeformatter.com/xml-formatter.html

def goThruFiles(keyWord_list):
	"""file collecting, loading and parsing Accepts a list of keyword (words in strings)"""

	file_list = hc.getFileListing() # get a listing of the files out there in the corpus dir
	# print("\t [file_list] : ",file_list)
	if len(file_list) == 0:
		hc.printErrorByPlatform("\t There do not appear to be any input files in <{}> ...Exiting".format(hc.corpusDir))
		exit()

	articlesOfKeywords_list = [] # holds the details of articles in which keywords were found.

	counter = 0
	for f in file_list:
		#print("\t [file_list] file :",f)
		data_str = hc.openFile(f) # get the data for current file

		# how many files done and number to go
		hc.printByPlatform("\n\t {} of {} File: {}".format(counter, len(file_list)-1, f))
		counter += 1

		#print("\n\t ~~~-- Getting article details --~~~")
		# initiate praser() to process xml files
		p = hc.parser(f, data_str, keyWord_list) #send filename, contents of file, list of key words
		# p.hello() # determine that the parser class is working

		# debugging
		#	p.viewAllTags()
#		if hc.HUSH_MODE == False:
#			p.viewAllTags()

		tmp_list = p.getInformationOfKwInDocs()

		#print("\t [This single article's details and found words] {}".format(tmp_list))

		if tmp_list != None: # put all records together
			articlesOfKeywords_list.append(tmp_list)

	# print("~~--- Entire doc details with found keywords ---~~~")
	#	print("\t [+] articlesOfKeywords_list : {}".format(articlesOfKeywords_list))

		headers_list = p.getTitlesOfCols() # get the headers for columns of the csv file
	# Notes on articlesOfKeywords_list.
	# For each record,
	# [articleNum][0] : title (string)
	# [articleNum][1] : abstract (string)
	# [articleNum][2] : pmid (string)
	# [articleNum][3] : journal (string)
	# [articleNum][4] : year of publication (string)
	# [articleNum][5] : pmids of references (list of strings)
	# [articleNum][6] : found words in abstract (list of strings)
	# [articleNum][7] : Count of found of found words in abstract (list of integers). This list is in the same order as the list of found words
	# save a manifest file with the header names

#	print("\t [+] headers_list :{}".format(headers_list))

	tmp_str = ""
	for i in headers_list:
		tmp_str = tmp_str + " " + str(i) + ","
		#print("\t [+] goThruFiles() tmp_str ; {}".format(tmp_str))
		tmp_str = tmp_str[:len(tmp_str)-1] # lose that last comma
	hc.saveFile(tmp_str)

	return articlesOfKeywords_list


####################
# remove stopwords #
####################

	# # next steps. remove stop words
	# ref: https://stackabuse.com/removing-stop-words-from-strings-in-python/
# end of goThruFiles()




def getKeywords(keywordFile_str):
	"""Function to engage the KWmanager class to load, prepare keywords from files."""
	hc.printHush("getKeywords()")
	kw = hc.KWmanager(keywordFile_str)
	#kw.hello() # is the KWmanager working?
	kwFile_list = kw.openKWFile()
	hc.printHush(kwFile_list)
	return kwFile_list
	#end of getKeywords

def begin(inFile0=""):
	"""Driver function of program"""
	print("\t [Input file]: ",inFile0)
	keyWord_list = getKeywords(inFile0) #get keyword strings in a list
	print("\t [Full keyword listing]: ",keyWord_list)
	articlesOfKeywords_list = goThruFiles(keyWord_list) # parse xml docs, search for keywords

	# Save output as csv
	#hc.printByPlatform("\t Getting ready to print a csv file")
	hc.makeCSVFile(articlesOfKeywords_list, inFile0)

	print()
	hc.printByPlatform("\t END! Roooo! Roooo!")

	#end of begin()


if __name__ == '__main__':

	if len(sys.argv) == 2: # one parameter at command line
	# note: the number of command line parameters is n + 1
		begin(sys.argv[1])#,sys.argv[2])#,sys.argv[3], sys.argv[4]),sys.argv[5])
	else:
		hc.helper()
		sys.exit()
