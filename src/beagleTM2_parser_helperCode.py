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


DATE = "6 July 2022"
VERSION = "0.2.4"
AUTHOR = "Oliver Bonham-Carter"
AUTHORMAIL = "obonhamcarter@allegheny.edu"

"""A body of code to assist with code from my programs. This helper code should be easier to maintain for a project. Right?"""

# debugging
HUSH_MODE = True # False # (True/False) boolean variable; prints if False

# globals
FILE_EXTENTION1 = "nxml"
FILE_EXTENTION2 = "xml"

# Directories
#MYOUTPUT_DIR = "/tmp/0out/" # all results are saved in this local directory
MYOUTPUT_DIR = "data/" # all results are saved in this local directory

# configure your corpus directory here.
CORPUS_DIR = "corpus/" #local small set of corpus files

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
import math, os, sys, string, csv, random


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
	print(BIYellow + "\n\tKeyword files have the following format in a file:\n\n\t#### keywords\n \tkeyword_1\n\tkeyword_n\n" + White)
# end of helper()


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
# end of get_platformType()


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
# end of printErrorByPlatform()

def printHush(in_str):
	"""prints if not in HUSH mode. Used for deugging code """
	if HUSH_MODE == False:
		print(in_str)
# end of printHush()


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
# end of printer()


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
# end of openFile()


def getFileListing():
	"""method to grab all files with a particular extention"""
	files_list = [] # holds each file and diretory
	for root, dirs, files in os.walk(CORPUS_DIR):
		for file in files:
			if file.endswith(FILE_EXTENTION1) or file.endswith(FILE_EXTENTION2):
				dataFile = os.path.join(root, file)
				files_list.append(dataFile)
	#print(" getfileListing : files_list :",files_list)
	return files_list
# end of getFileListing

def saveStats(stats_dic,inFile0):
	"""function to save the statistics file generated by processing articles."""
	tmp_str = "item, count\n"

	for i in stats_dic:
		tmp_str = tmp_str + str(i) +","+ str(stats_dic[i]) + "\n"
	# print(printWithColour(BIPurple,f"tmp_str:\n{tmp_str}"))

	try:
		tmp_dir = checkDataDir(MYOUTPUT_DIR)
		fname = inFile0.replace(".md","")+"_stats.csv"
		filename = MYOUTPUT_DIR + fname
		f = open(filename, "w")
		f.write(tmp_str)
		f.close()
		printByPlatform(BIGreen + f"\n\t [+] Saving <{filename}>" + White)

	except IOError:
		printErrorByPlatform(BIRed + f"\t Problem saving file... incorrect permissions?!" + White)
	# end of saveFile()

	# print(f"saveStats(): s_str {s_str}")



def saveFile(in_str):
	"""Save the string as a text file. Filename is defined in function."""
	if len(in_str) > 0:
			tmp_str = ""

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
				printByPlatform(BIGreen + f"\n\t [+] Saving <{filename}>" + White)

			except IOError:
				printErrorByPlatform(BIRed + f"\t Problem saving file... incorrect permissions?!" + White)
# end of saveFile()

def printWithColour(colCode_str, myMessage_str):
	"""A function to print with colour for Unix and MacOS."""
	platform_str = get_platformType()
	if platform_str.lower() == "linux" or platform_str.lower() == "osx":
		myMessage_str = colCode_str + myMessage_str + BIWhite
		# print(colCode_str + myMessage_str + BIWhite)
	else: # Windows does not seem to like these colourcodes
		# print(myMessage_str)
		pass
	return myMessage_str
# end of printWithColour()


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
# end of checkDataDir()

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
#	inFile2_str = MYOUTPUT_DIR + "all_" + inFile0_str.replace(".md","") + "_analysis.csv"
	inFile2_str = MYOUTPUT_DIR + inFile0_str.replace(".md","") + "_analysis.csv"

	with open (inFile2_str, "w") as fp:
		fp.write(data1)
		printByPlatform(BGreen + f"\n\t [+] Saving <{inFile2_str}>" + White)

	# Clean up header and intermediate file.
	removeFile(headerFile_str)
	removeFile(inFile1_str)

# end of makeCSVFile()

def removeFile(inFile1_str):
	"""Function to safely remove a file using exceptions. """
	try:
		#print(f"\t Removing file : {inFile1_str}")
		os.remove(inFile1_str)
	except FileNotFoundError:
		pass
# end of removeFile()
