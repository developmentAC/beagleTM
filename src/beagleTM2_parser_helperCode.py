#!/usr/bin/python3
# -*- coding: utf-8 -*-


banner0_str ="""
\t██████╗ ███████╗ █████╗  ██████╗ ██╗     ███████╗████████╗███╗   ███╗
\t██╔══██╗██╔════╝██╔══██╗██╔════╝ ██║     ██╔════╝╚══██╔══╝████╗ ████║
\t██████╔╝█████╗  ███████║██║  ███╗██║     █████╗     ██║   ██╔████╔██║
\t██╔══██╗██╔══╝  ██╔══██║██║   ██║██║     ██╔══╝     ██║   ██║╚██╔╝██║
\t██████╔╝███████╗██║  ██║╚██████╔╝███████╗███████╗   ██║   ██║ ╚═╝ ██║
\t╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝   ╚═╝   ╚═╝     ╚═╝
"""
# banner ref: https://manytools.org/hacker-tools/ascii-banner/


DATE = "6 Feb 2021"
VERSION = "2_iv"
AUTHOR = "Oliver Bonham-Carter"
AUTHORMAIL = "obonhamcarter@allegheny.edu"

"""A body of code to assist with code from my programs. This helper code should be easier to maintain for a project. Right?"""


# debugging
HUSH_MODE = True # False # (True/False) boolean variable; prints if False

# globals
FILE_EXTENTION = "nxml"

# Directories
#MYOUTPUT_DIR = "/tmp/0out/" # all results are saved in this local directory
MYOUTPUT_DIR = "data/" # all results are saved in this local directory

# configure your corpus directory here.
CORPUS_DIR = "corpus/" #local small set of corpus files

# keyword files: To prevent errors, keyword files
# must have the following first line of file to identify them.
KW_ID = "#### keywords"




# colour codes

# Bold High Intensity
BIBlack='\033[1;90m'      # Black
BIRed='\033[1;91m'        # Red
BIGreen='\033[1;92m'      # Green
BIYellow='\033[1;93m'     # Yellow
BIBlue='\033[1;94m'       # Blue
BIPurple='\033[1;95m'     # Purple
BICyan='\033[1;96m'       # Cyan
BIWhite='\033[1;97m'      # White

# Regular Colors
Black='\033[0;30m'        # Black
Red='\033[0;31m'          # Red
Green='\033[0;32m'        # Green
Yellow='\033[0;33m'       # Yellow
Blue='\033[0;34m'         # Blue
Purple='\033[0;35m'       # Purple
Cyan='\033[0;36m'         # Cyan
White='\033[0;37m'        # White

# Bold
BBlack='\033[1;30m'       # Black
BRed='\033[1;31m'         # Red
BGreen='\033[1;32m'       # Green
BYellow='\033[1;33m'      # Yellow
BBlue='\033[1;34m'        # Blue
BPurple='\033[1;35m'      # Purple
BCyan='\033[1;36m'        # Cyan
BWhite='\033[1;37m'       # White


# Bold colour list
colour_list =['\033[1;30m',
'\033[1;31m',
'\033[1;32m',
'\033[1;33m',
'\033[1;34m',
'\033[1;35m',
'\033[1;36m',
'\033[1;37m',
'\033[1;90m',
'\033[1;91m',
'\033[1;92m',
'\033[1;93m',
'\033[1;94m',
'\033[1;95m',
'\033[1;96m',
'\033[1;97m',]


# import libraries
import xml.etree.ElementTree as ET
import math, re, os, sys, string, csv, random


# list other libraries here
#from sklearn.metrics import r2_score
#from sklearn.metrics import mean_squared_error
#import plotly.plotly as py
#import plotly.graph_objs as go
#from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
#import matplotlib.pyplot as plt
#from scipy import stats
#import numpy as np



def helper():

	"""Cheap online help; how to use the program"""
	h_str1 = "\t"+ BIBlue + DATE+" | version: "+VERSION + White
	h_str2 = "\t"+ BIBlue + AUTHOR +"\n\tmail: "+AUTHORMAIL + White
	print("\t"+len(h_str2) * "-")
	print(h_str1)
	print("\t"+len(h_str2) * "-")
	print(h_str2)
	print("\t"+len(h_str2) * "-")

	randomColour_str = random.choice(colour_list) # choose a random colour to display the title screen.
	print(randomColour_str + banner0_str + White)
#	print(banner0_str)
#	print("\tHelperCode.py help()")
	print(BIBlue + "\n\tBeagleTM2: A Pubmed article parser." + White)
	platform_str = get_platformType()
	print("\n\t OS type: ",platform_str) # determine what the os is.
	#print("""\n\tLibrary installation notes:""")
	command_str = BGreen + "USAGE: programName <any key to launch>" + White
	if platform_str.lower() == "linux" or platform_str.lower() == "osx":
		print("\t" + BWhite + " \U0001f5ff \U0001F608" * 8)
		print(BGreen + "\n\t [+] \U0001f600 ", command_str)
	else:
		print("\n\t+ :-) ", command_str)
	print(BGreen + f"\t [+] The INPUT directory (Data files are located here)  : {CORPUS_DIR}" + White)
	print(BGreen + f"\t [+] The OUTPUT directory (Output data is placed here)  : {MYOUTPUT_DIR}" + White)
	print("\t"+len(h_str2) * "-")
	print("\tNotes. Data can be downloaded from: ftp://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_bulk/")
	print(BIYellow + "\n\tKeyword files have the following format:\n\n\t#### keywords\n \tkeyword_1\n\tkeyword_n\n" + White)
#end of helper()


def get_platformType():
	"""Function to dermine the OS type."""
	platforms = {
	'darwin' : 'OSX',
	'win32'  : 'Windows',
	'linux1' : 'Linux',
	'linux2' : 'Linux'}
	if sys.platform not in platforms:
		return sys.platform
	return platforms[sys.platform]
#end of get_platformType()


def printByPlatform(in_str):
	"""prints emojicons according to OS type"""
	# list of unicodes of emoticons
	# https://www.fileformat.info/info/unicode/block/emoticons/images.htm
	platform_str = get_platformType()
	if platform_str.lower() == "linux" or platform_str.lower() == "osx":
		print("  " + " \U0001F415 ",in_str)
	else:
		print("\n\t+ ~~~-- article details --~~~\n\t",in_str)
	# end of printByPlatform()

def printErrorByPlatform(in_str):
	"""prints error with emojicons according to OS type"""
	# list of unicodes of emoticons
	# https://www.fileformat.info/info/unicode/block/emoticons/images.htm
	platform_str = get_platformType()
	if platform_str.lower() == "linux" or platform_str.lower() == "osx":
		print("\n  " + " \U0001F631 ",in_str + " \U0001F631 " )
	else:
		print("Error: ",in_str)
	#end of printErrorByPlatform()

def printHush(in_str):
	"""prints if not in HUSH mode"""
	if HUSH_MODE == False:
		print(in_str)
	#end of printHush()


def printer(inThing):
	""" prints things cleanly. Variable inThing is list or dict"""
	if "list" in str(type(inThing)):
		for i in range( len(inThing) ):
			print("\t",i,":", inThing[i])
	if "dict" in str(type(inThing)):
		counter = 0
		for i in inThing:
			print("\t",counter," |  ",i,":",inThing[i])
			counter += 1
#end of printer()


def openFile(inFile1):
	""" open a text file, return string"""
#		f = open(inFile1,"r").read()

	try: #is the file there??
		f = open(inFile1, "r").read() #returns a string
	#print(f,":",type(f))
		return f
	except IOError:
		tmp_str = "\aNo such file!!!! <{}>, so exiting".format(inFile1)
		printErrorByPlatform(tmp_str)
	#end of openFile()


def getFileListing():
	"""method to grab all files with a particular extention"""
	files_list = [] # holds each file and diretory
	for root, dirs, files in os.walk(CORPUS_DIR):
		for file in files:
			if file.endswith(FILE_EXTENTION):
				dataFile = os.path.join(root, file)
				files_list.append(dataFile)
	#print(" getfileListing : files_list :",files_list)
	return files_list
#end of getFileListing


def saveFile(in_str):
	"""Save the string as a text file. Filename is in_str variable."""


	if len(in_str) > 0:
			tmp_str = ""
			#print("\t [+] saveFile HEADERS_out:\n\t {}".format(in_str))
			# put some commas between the headers for the csv
			for i in in_str.split():
				tmp_str = tmp_str + i +","
			tmp_str = tmp_str[:len(tmp_str)-1] # remove the last comma
			tmp_str = tmp_str + "\n" # add a line break
			#print("\t [+] saveFile HEADERS_out:\n\t {}".format(tmp_str))

			try:
				tmp_dir = checkDataDir(MYOUTPUT_DIR)
				fname = "HEADERS_out.csv"
				filename = MYOUTPUT_DIR + fname
				f = open(filename, "w")
				f.write(tmp_str)
				f.close()
				printByPlatform(BGreen + f"\n\t [+] Saving <{filename}>" + White)

			except IOError:
				printErrorByPlatform(BRed + f"\t Problem saving file... incorrect permissions?!" + White)
	# end of saveFile()


def checkDataDir(dir_str):
#function to determine whether a data output directory exists.
#if the directory doesnt exist, then it is created

	try:
		os.makedirs(dir_str)
		#if MYOUTPUT_DIR doesn't exist, create directory
		#printByPlatform("\t Creating :{}".format(dir_str))
		return 1

	except OSError:
		#printErrorByPlatform("\t Error creating directory or directory already present ... ")
		return 0
#end of checkDataDir()

def makeCSVFile(in_list, inFile0_str):
	"""Function to create a giant CSV file of all results."""
	# print(f"file name : {inFile0_str}")
	# print(f"makeCSVFile(); in_list is {in_list}")

	# check or prepare the output directory
	directoryIsThere_bol = checkDataDir(MYOUTPUT_DIR)

	# change that filename to an output file.
	inFile1_str = MYOUTPUT_DIR + inFile0_str.replace(".md","") + "_out.csv"
	#print("filename : {}".format(inFile0_str))

	file = open(inFile1_str, "w", newline = '') #the newline should make this cross platform compatible

	# ref: https://docs.python.org/3/library/csv.html
	# writing the data into the file
	with file:
		write = csv.writer(file)
		write.writerows(in_list)

	# concatentate the headers to the data for the analysis step.
	data1 = data2 = ""
	headerFile_str = MYOUTPUT_DIR + "HEADERS_out.csv"
	with open(headerFile_str) as myHeaders:
		data1 = myHeaders.read()

	with open(inFile1_str) as myData:
		data2 = myData.read()

	# merge these headers with data file.
	data1 += "\n" # add a space to help in readability of ouptut datafiles
	data1 += data2

	# change that filename to an output file.
	inFile2_str = MYOUTPUT_DIR + "all_" + inFile0_str.replace(".md","") + "_analysis.csv"

	with open (inFile2_str, "w") as fp:
		fp.write(data1)
		printByPlatform(BGreen + f"\n\t [+] Saving <{inFile2_str}>" + White)

	# Clean up header and intermediate file.
	removeFile(headerFile_str)
	removeFile(inFile1_str)

	#end of makeCSVFile()

def removeFile(inFile1_str):
	"""Function to safely remove a file using exceptions. """

	try:
		#print(f"\t Removing file : {inFile1_str}")
		os.remove(inFile1_str)
	except FileNotFoundError:
		pass
	# end of removeFile()


### CLASSES ###


class parser(object):
	"""A class to parse each nxml file for its abstract, pmid and other details. The class also handles parsing the abstracts for keywords."""
	def __init__(self, fileName_str, data_str, keyWord_list):
		self.fileName_str = fileName_str
		self.data_str = data_str # the nxml file's contents
		self.keyWord_list = keyWord_list
		self.abstract_str = ""
		self.title_str = ""
		# pass
		# end of __init__()
	def hello(self):
		print("\t [+] Hello from the parser() class!")
		#end of hello()

	def viewAllTags(self):
		"""Views all tags of xml"""
		printHush("\n\t + viewAllTags()")
		try:
			tree = ET.fromstring(self.data_str)
		except ET.ParseError as err:
			#printErrorByPlatform("Error detected in current File")
			return None

		for child in tree.getiterator():
			tmp_str = "child.tag: " + str(child.tag) + str(type(child.tag))+"\n child.attrib :"+ str(child.attrib) + "\n child.text :"+ str(child.text) + "\n child.tail :"+ str(child.tail)
			printHush(tmp_str)
		#end of viewAllTags()


	def extractTextFromElement0(self, childTag):
		"""Pulls element from tag.child. Usage: extractTextFromElement('tag2', XML_data)"""
		#print("\n\t + extractTextFromElement0()")
		try:
			tree = ET.fromstring(self.data_str)
		except ET.ParseError as err:
			#printErrorByPlatform("Error detected in current File")
			return None

		for child in tree.getiterator():
			tmp_str = "child.tag: " + str(child.tag) + str(type(child.tag))+"\n child.attrib :"+ str(child.attrib) + "\n child.text :"+ str(child.text) + "\n child.tail :"+ str(child.tail)
			printHush(tmp_str)
			#print("child.tag: ",child.tag, type(child.tag))
			#print("child.attrib :", child.attrib) # dict
			#print("child.text :", child.text) #attrib
			#print("child.tail :", child.tail)
	#		if child.tag == childTag:
			if childTag in child.tag:
				#print("tag found...",child.tag, type(child.tag), childTag)
				len = ET.tostring(child).decode("utf-8").replace("\n"," ").replace("  ","").strip()
				#print("len type :",type(len))
				return re.sub(r'<.*?>', '', len)
				# len = re.sub(r'<.*?>', '', len)
				# return len
		#end of extractTextFromElement0()


	def extractTextFromElement1(self, childTag, attribTag_str):
		"""Pulls element from tag.child. Works with lists. Usage: extractTextFromElement('tag2', XML_data, attribTag_str)"""
		printHush("\n\t + extractTextFromElement1(): ")
		tmp_str = "\t attribTag_str: "+attribTag_str+"\n\t childTag: "+childTag
		printHush(tmp_str)
		tmp_list = []
		try:
			tree = ET.fromstring(self.data_str)
		except ET.ParseError as err:
			#printErrorByPlatform("Error detected in current File")
			return None

		for child in tree.getiterator():
			# print("child.tag: ",child.tag, type(child.tag))
			# print("child.attrib :", child.attrib) # dict
			# print("child.text :", child.text) #attrib
			# print("child.tail :", child.tail)
			if childTag in child.tag and attribTag_str in child.attrib.values():
				#print("\t[+] attribTag_str:",attribTag_str,"found.")
				#print("\t child.text:",child.text)
				try:
					tmp_list.append(int(child.text))
				except ValueError: # not an int
					tmp_list.append(child.text)
#				print("extractTextFromElement1(): {} is type {}".format(child.text, type(child.text)))
#		print("extractTextFromElement1(): tmp_list is {} ".format(tmp_list))

		#print("\t extractTextFromElement1: returning {}",format(tmp_list))
		return tmp_list
		#end of extractTextFromElement1()


	def extractTextFromElement2(self, childTag, attrib_str = ""):
		"""Pulls element from tag.attrib."""
		printHush("\n\t + extractTextFromElement2()")
		try:
			tree = ET.fromstring(self.data_str)
		except ET.ParseError as err:
			#printErrorByPlatform("Error detected in current File")
			return None

		for child in tree.getiterator():
			# print("child.tag: ",child.tag, type(child.tag))
			# print("child.attrib :", child.attrib) # dict
			# print("child.text :", child.text) #attrib
			# print("child.tail :", child.tail)
			# print()
	#		if child.tag == childTag:
			if child.tag in childTag:
				#print("tag found...",child.tag, type(child.tag), childTag)
				if attrib_str in child.attrib.values():
					# print("\n\t[attrib]: ",child.text)
					return child.text
		#end of extractTextFromElement2()


	def getTitle(self, task_str = None):
		"""Method to get the title of article in the xml doc. The task_str is a command to only return the column header f the method and will be used in the CVS file creation."""
		#print("\t [+] getTitle()")
		if task_str == "headerCall": return "Title"

		#title:tag, get child.text
		childTag = "article-title"
#		f_str = self.extractTextFromElement0(childTag, self.data_str)
		self.title_str = self.extractTextFromElement0(childTag)
		#print("\t[title]: ",self.title_str)
		return self.title_str
		#end of getTitle()


	def getAbstract(self ,task_str = None):
		"""gets the title of main article in the xml doc"""
		#abstract, get abstract from child.tag
		if task_str == "headerCall": return "Abstract"

		childTag = "abstract"
#		f_str = self.extractTextFromElement0(childTag, self.data_str)
		self.abstract_str = self.extractTextFromElement0(childTag)
		return self.abstract_str
		#end of getAbstract()

	def getYear(self, task_str = None):
		"""gets the year of main article in the xml doc"""
		#abstract, get abstract from child.tag
		if task_str == "headerCall": return "Year"

		childTag = "year"
#		f_str = self.extractTextFromElement0(childTag, self.data_str)
		f_str = self.extractTextFromElement0(childTag)
		return f_str
		#end of getAbstract()

	def getPmid(self, task_str = None):
		"""gets the main pmid (pubmed's primary key) of main article in the xml doc"""
		#article pmid
		if task_str == "headerCall": return "PMID"

		childTag = "article-id"
		attrib_str = "pmid"
#		f_str = self.extractTextFromElement1(childTag, self.data_str, attrib_str)
		f_list = self.extractTextFromElement1(childTag, attrib_str)
		# print(" \t[",attrib_str,"]: ",f_str)
		try:
			return f_list[0] #gimme a string, not a list
		except:
			return f_list
		#end of getPmid()


	def getJournal(self, task_str = None):
		"""gets the journal name of main article in the xml doc"""
		#journal name
		if task_str == "headerCall": return "Journal"

		childTag = "journal-id"
		attrib_str = "nlm-ta"
#		f_str = self.extractTextFromElement1(childTag, self.data_str, attrib_str)
		f_list = self.extractTextFromElement1(childTag, attrib_str)
		# print(" \t[",attrib_str,"]: ",f_str)
		try:
			return f_list[0] #gimme a string, not a list
		except:
			return f_list
		#end of getJournal()


	def getReferences(self, task_str = None):
		"""gets list of references of main article in the xml doc"""
		# #references (pmids)
		if task_str == "headerCall": return "References"

		childTag = "pub-id"
		attrib_str = "pmid"
#		f_list = self.extractTextFromElement1(childTag, self.data_str, attrib_str)
		f_list = self.extractTextFromElement1(childTag, attrib_str)
		#print(" \t[",attrib_str,"]: ",f_list)
		#print("getReferences() :returning {}".format(f_list))
		return f_list
		#end of getReferences()

	def getTitlesOfCols(self):
		"""Method to call each of the information gathering methods to determine what the headers of the information should be called. Each method (i.e., getTitle()) has a task that will only return the header name. Note, be sure have header names in the order of the data."""

#  We are appending this list to the top of the main list of article details. The header list is collected each time the parser methods are run.

		headers_list = []
		#get the names of the data's headers. (i.e,. the titles of the columns)
		headers_list.append(self.getTitle("headerCall"))
		headers_list.append(self.getAbstract("headerCall"))
		headers_list.append(self.getPmid("headerCall"))
		headers_list.append(self.getJournal("headerCall"))
		headers_list.append(self.getYear("headerCall"))
		headers_list.append(self.getReferences("headerCall"))

# we have to add some column headers manually... :-(
		headers_list.append("Keyword")
		headers_list.append("Counts")

		#print("\t [+] headers_list : {}".format(headers_list))
		return headers_list
		# end of getTitlesOfCols()

	def getInformationOfKwInDocs(self):
		"""A Method to locate the keywords in the document abstracts. If any keyword is found, return all details to program"""
#		print("getInformationOfKwInDocs()")

		#print("\n\t Searching abstract: {} \n".format(self.abstract_str))


		# Get the details of the current article; used later if keywords are found.
		docDetails_list = []
#		headers_list = self.getTitlesOfCols()

		self.title_str = self.getTitle() # check to see whether the file is good
		#printByPlatform("\t [+] getInformationOfKwInDocs() title is: {}".format(self.title_str))

		if self.title_str != None: #working title found?
			#hc.printByPlatform("\t ~~~-- article details --~~~ ")
	#		print("\t[getTitle()]: ",f_str)
			docDetails_list.append(self.title_str)
			#print("\t[Title]: {}".format(self.title_str))
			#print("docDetails_list : {}".format(docDetails_list))
			self.abstract_str = self.getAbstract()
			# print("\t[Abstract]: {}".format(self.abstract_str))
			docDetails_list.append(self.abstract_str)

			self.pmid_str = self.getPmid()
			#print("\t[Pmid]: {}".format(self.pmid_str))
			docDetails_list.append(self.pmid_str)

			self.journal_str = self.getJournal()
			#print("\t[Journal]: {} ".format(self.journal_str))
			docDetails_list.append(self.journal_str)

			self.year_str = self.getYear()
			#print("\t[Year]: {} ".format(self.year_str))
			docDetails_list.append(self.year_str)

			#hc.printByPlatform("\t ~~~-- references --~~~ ")
			self.ref_list = self.getReferences()
			#print("\t[References]: {} ".format(self.ref_list))
			docDetails_list.append(self.ref_list)

			#######################
			# If the abstract contains a keyword, then keep the article details, otherwise ditch them.
			foundKeyWords_list = [] # contains keywords that were found in the current article

			for kw_str in self.keyWord_list:
				#print("\t \U0001f5ff Searching keyword <{}> in abstract: \n".format(kw_str))
				printFlag = 0
				try:
					#print("\t trying keyword :{}".format(kw_str))
					if kw_str.lower() in self.abstract_str.lower():
						#	print("\t \U0001f5ff Found keywords ...")
						print("\t \U0001f5ff : <{}>".format(kw_str))
						foundKeyWords_list.append(kw_str) # keep found word in a list
				except: # general exception for badly formatted files.
#					print("Error in file... skipping <{}>".format(self.fileName_str))
					pass

					#print("\t [-] Error <{}>".format(self.fileName_str))

			wordCount_list = [] #keep track of how many counts of each word were found in abstract
			if len(foundKeyWords_list) > 0: # is there at least one found word in the list?

				for w in foundKeyWords_list:
					count = self.abstract_str.count(w)
					wordCount_list.append(count)
					#print("\t\n [Word count] word: <{}>, count: <{}>".format(w, count))
				docDetails_list.append(foundKeyWords_list) # get the words in the abstract
				docDetails_list.append(wordCount_list) # get the count of words in abstract

				return docDetails_list # return the whole set of details and kw counts for this article
			else:
				return None

		else:
			pass
			#print("\t [-] Improper: <{}>".format(self.fileName_str))

		#end of getInformationOfKwInDocs()
# end of parser class
####################


class KWmanager(object):
	"""class to open keyword files and prepare the words as strings"""
	def __init__(self, keywordFile):
		self.keywordFile = keywordFile
		# pass
		# end of __init__()
	def hello(self):
		print("\t [+] Hello from the KWmanager() class!")
		print("\t [+] Files to open : {}".format(self.keywordFile))
		#end of hello()

	def openKWFile(self):
		kwWords_list = [] # list to store keywords
		try: #is the file there??
			# self.data = open(self.keywordFile, "r").read() #returns a string
			data = open(self.keywordFile, "r").readlines() #returns a dict
		except IOError:
			tmp_str = "\aNo such file!!!! <{}>, so exiting".format(self.keywordFile)
			printErrorByPlatform(tmp_str)
			#print("  \a\tNo such file!!!! \"",self.keywordFile,"\" so exiting")
			sys.exit(1)
		#want dictionary of words, key = num, value = keyword
		for word_str in data:
			# clear about carrage returns and excess leading spaces. Add a space to both ends to ensure that the word itself is found, not this subset in another word.

			myword_str = " " + word_str.replace("\n","").strip() + " "
			#print(f"currentWord :<{myword_str}>")
			kwWords_list.append(myword_str)

			#
			# original code; The belo line ad some trouble discerning a word from a subset of a word; no spaces given on both sides of word.
			# kwWords_list.append(word_str.replace("\n","").strip())
			#

		# if kwWords_list[0] == KW_ID: # part of original code to discern the keyword tag to prevent loading non keyword files.
		if KW_ID in kwWords_list[0]:
			#print("\tThis is a keyword file: ",kwWords_list[0])
			kwWords_list.remove(kwWords_list[0])
			#print(kwWords_list)
			return kwWords_list
		else:
			printErrorByPlatform(" This is not a Keyword file... \n\tMust have <{}> at top of file to identify.".format(KW_ID))
			exit()
			# end of openKWFile()
# end KWmanager class
