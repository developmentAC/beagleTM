#!/usr/bin/python3
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

# DATE = "22 June 2022"
# VERSION = "0.2.2"
# AUTHOR = "Oliver Bonham-Carter"
# AUTHORMAIL = "obonhamcarter@allegheny.edu"

# """The driver of the whole thing."""


# import libraries
import os, sys, math
import beagleTM2_parser_helperCode as hc
import parserClass as myParser
import KWmanagerClass as myKwManager

# Notes: to format nxml files into human readable formats
#ref: https://www.freeformatter.com/xml-formatter.html

def goThruFiles(inFile0_str, keyWord_list):
	"""file collecting, loading and parsing Accepts a list of keyword (words in strings)"""

	file_list = hc.getFileListing() # get a listing of the files out there in the corpus dir
	# print(f"\t +++ [file_list] : {file_list}")
	if len(file_list) == 0:
		hc.printErrorByPlatform("\t There do not appear to be any input files in <{}> ...Exiting".format(hc.CORPUS_DIR))
		exit()

	articlesOfKeywords_list = [] # holds the details of articles in which keywords were found.
	counter = 0

	# Begin to prepare the final statistics for the data:
	# we contain the stats for found words and article numbers.
	stats_dic = {"Total_articles":len(file_list)-1}

	for f in file_list:
		#print("\t [file_list] file :",f)
		data_str = hc.openFile(f) # get the data for current file

		# how many files done and number to go
		hc.printByPlatform(f"\n\t {counter} of {len(file_list)-1} File: {f}")
		counter += 1

		#print("\n\t ~~~-- Getting article details --~~~")
		# initiate praser() to process xml files

		p = myParser.parser(f, data_str, keyWord_list) #send filename, contents of file, list of key words

		tmp_list = p.getInformationOfKwInDocs()
		# print("\t [This single article's details and found words] {}".format(tmp_list))

		if tmp_list != None: # put all records together
			articlesOfKeywords_list.append(tmp_list)

		# create the headers of the csv data file. These headers will be used to determine which column is what data.
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

	# print("~~--- print Document details for found key words ---~~~")
	# print(hc.printWithColour(hc.BIPurple,f"[+] articlesOfKeywords_list : {articlesOfKeywords_list}"))

	# prepare the headers for the final data file.
	tmp_str = ""
	for i in headers_list:
		tmp_str = tmp_str + " " + str(i) + ","
		# print(hc.printWithColour(hc.BIYellow,f"\t [+] goThruFiles() :{tmp_str}"))
		tmp_str = tmp_str[:len(tmp_str)-1] # lose that last comma
	hc.saveFile(tmp_str)

	for article_list in articlesOfKeywords_list: # go through the articles with found keywords to determine counts of words.
		stats_dic = getLogs(article_list[6], stats_dic)
	print(hc.printWithColour(hc.BIBlue,f"Summary: {stats_dic}"))
	hc.saveStats(stats_dic,inFile0_str)

	return articlesOfKeywords_list


####################
# remove stopwords #
####################

	# # next steps. remove stop words
	# ref: https://stackabuse.com/removing-stop-words-from-strings-in-python/
# end of goThruFiles()

def getLogs(thisKeyWord_list, stats_dic):
	""" A method to get basic stats from search (i.e. number of words found, number of files, etc.). thisKeyWord_str is the keyword to be incremented in stats_dic"""

	# print(hc.printWithColour(hc.BIPurple,f"getLogs() <{len(thisKeyWord_list)}> {type(thisKeyWord_list)} and dictionary = <{stats_dic}>"))
	for word_str in thisKeyWord_list:
		w = word_str.strip()
		# print(hc.printWithColour(hc.BIRed,f"word::--> {w}"))
		if w in stats_dic:
			stats_dic[w] = stats_dic[w] + 1
		else:
			stats_dic[w] = 1
	# print(hc.printWithColour(hc.BIRed,f"type(stats_dic),{type(stats_dic)}"))
	return stats_dic
# end of getLogs()



def getKeywords(keywordFile_str):
	"""Function to engage the KWmanager class to load, prepare keywords from files."""
	hc.printHush("getKeywords()")
	kw = myKwManager.KWmanager(keywordFile_str)
	# print(f"keywordFile_str : {keywordFile_str}")
	kwFile_list = kw.openKWFile()
	# print(f" +++ {kwFile_list}")
	return kwFile_list
	# end of getKeywords

def begin(inFile0=""):
	"""Driver function of program"""
	print("\t [Input file]: ",inFile0)
	keyWord_list = getKeywords(inFile0) #get keyword strings in a list
	# print("\t [Full keyword listing]: ",keyWord_list)
	articlesOfKeywords_list = goThruFiles(inFile0, keyWord_list) # parse xml docs, search for keywords

	# Save output as csv
	#hc.printByPlatform("\t Getting ready to print a csv file")
	hc.makeCSVFile(articlesOfKeywords_list, inFile0)

	print()
	hc.printByPlatform("\t END! Roooo! Roooo!")
	print(hc.printWithColour(hc.BIYellow, "\n\t [+] \t Use following command to analyse your results;"))
	print(hc.printWithColour(hc.BIYellow, f"\n\t \t streamlit run beagleTM2_browser.py"))
	print(hc.White)

	# end of begin()


if __name__ == '__main__':

	if len(sys.argv) == 2: # one parameter at command line
	# note: the number of command line parameters is n + 1
		begin(sys.argv[1])
	else:
		hc.helper()
		sys.exit()
