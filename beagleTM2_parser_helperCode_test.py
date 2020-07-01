#!/usr/bin/env python3
# -*- coding: utf-8 -*-




import unittest

from beagleTM2_parser_helperCode import get_platformType
from beagleTM2_parser_helperCode import printByPlatform
from beagleTM2_parser_helperCode import printErrorByPlatform
from beagleTM2_parser_helperCode import printer
from beagleTM2_parser_helperCode import openFile

class test_beagleTmApp(unittest.TestCase):

	def test_get_platformType(self):
		""" checking that the output of this function is present"""
		osTypes_list = ["osx", "windows", "linux"]
		myOS_str = get_platformType().lower()
		self.assertIn(myOS_str, osTypes_list, msg="returned an os type")
		# end of test_get_platformType()

	def test_printByPlatform(self):
		"""testing that the function is able to print something to be formatted according to the different OS types (i.e., OSX, Windows or Linux)"""
		in_str = "Hi there, this is a test."
		correctMsg_str = "  " + " \U0001F415 ",in_str
		msgFromFunction_str = printByPlatform(in_str)
		# self.assertIn(in_str , msgFromFunction_str, msg = "in_str in the output")
		self.assertIsNotNone(self, msgFromFunction_str) # something is returned.
		# end of test_printByPlatform()

	def test_printErrorByPlatform(self):
		""" Printing an error using symbols of linux, OSX or text for windows"""
		in_str = "Hi there, this is a test."
		self.assertIsNotNone(self,printErrorByPlatform(in_str))
		# end of def test_printByPlatform():

	def test_printer(self):
		""" testing the printing of a list and a dic"""
		my_list = [0,1]
		my_dic = {0:"zero",1:"one"}
		self.assertIsNotNone(self, printer(my_list))
		self.assertIsNotNone(self, printer(my_dic))
		# end of printer()

	def test_openFile(self):
		tmp_str = "myFileThatDoesNotExist.md"

		self.assertIsNotNone(self, openFile(tmp_str))
		# end of test_openFile()
