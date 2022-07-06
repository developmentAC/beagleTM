#!/usr/bin/python3
# -*- coding: utf-8 -*-



import xml.etree.ElementTree as ET
import beagleTM2_parser_helperCode as hc
import re

class parser(object):
	""" Class for handling the parsing job of the articles. A class to parse each nxml file for its abstract, pmid and other details. The class also handles parsing the abstracts for keywords."""

	def __init__(self, fileName_str, data_str, keyWord_list):
		self.fileName_str = fileName_str
		self.data_str = data_str # the nxml file's contents
		self.keyWord_list = keyWord_list
		self.abstract_str = ""
		self.title_str = ""
	# end of __init__()

	def hello(self):
		print("\t [+] Hello from the parser() class!")
	# end of hello()

	def viewAllTags(self):
		"""Views all tags of xml"""
		hc.printHush("\n\t + viewAllTags()")
		try:
			tree = ET.fromstring(self.data_str)
		except ET.ParseError as err:
			#printErrorByPlatform("Error detected in current File")
			return None

		for child in tree.getiterator():
			tmp_str = "child.tag: " + str(child.tag) + str(type(child.tag))+"\n child.attrib :"+ str(child.attrib) + "\n child.text :"+ str(child.text) + "\n child.tail :"+ str(child.tail)
			hc.printHush(tmp_str)
	# end of viewAllTags()

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
			hc.printHush(tmp_str)
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
	# end of extractTextFromElement0()

	def extractTextFromElement1(self, childTag, attribTag_str):
		"""Pulls element from tag.child. Works with lists. Usage: extractTextFromElement('tag2', XML_data, attribTag_str)"""
		hc.printHush("\n\t + extractTextFromElement1(): ")
		tmp_str = "\t attribTag_str: "+attribTag_str+"\n\t childTag: "+childTag
		hc.printHush(tmp_str)
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
	# end of extractTextFromElement1()


	def extractTextFromElement2(self, childTag, attrib_str = ""):
		"""Pulls element from tag.attrib."""
		hc.printHush("\n\t + extractTextFromElement2()")
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
	# end of extractTextFromElement2()


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
	# end of getTitle()


	def getAbstract(self ,task_str = None):
		"""gets the title of main article in the xml doc"""
		#abstract, get abstract from child.tag
		if task_str == "headerCall": return "Abstract"

		childTag = "abstract"
#		f_str = self.extractTextFromElement0(childTag, self.data_str)
		self.abstract_str = self.extractTextFromElement0(childTag)
		return self.abstract_str
	# end of getAbstract()

	def getYear(self, task_str = None):
		"""gets the year of main article in the xml doc"""
		#abstract, get abstract from child.tag
		if task_str == "headerCall": return "Year"

		childTag = "year"
#		f_str = self.extractTextFromElement0(childTag, self.data_str)
		f_str = self.extractTextFromElement0(childTag)
		return f_str
	# end of getAbstract()

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
	# end of getPmid()


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
	# end of getJournal()


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
	# end of getReferences()

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
		#print("\n\t Searching abstract: {} \n".format(self.abstract_str))
		# Get the details of the current article; used later if keywords are found.
		docDetails_list = []
		stats_dic = {}


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
						foundKeyWords_list.append(kw_str) # keep found word in a list


				except: # general exception for badly formatted files.
					# print(f"Error in file... skipping <{self.fileName_str}>")
					pass

			wordCount_list = [] #keep track of how many counts of each word were found in abstract
			if len(foundKeyWords_list) > 0: # is there at least one found word in the list?

				for w in foundKeyWords_list:
					count = self.abstract_str.count(w)
					wordCount_list.append(count)
					print(f"\t \U0001f5ff :",hc.printWithColour(hc.BIGreen,f" <{w}: {count}>"))

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
