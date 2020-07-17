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

import streamlit as st
import pandas as pd
import numpy as np
import time
import sys
import os
from pyvis.network import Network
from plotly import graph_objs as go
import networkx as nx

import spacy # needed to work with stopwords
from spacy.lang.en.stop_words import STOP_WORDS # needed to work with stop words

import beagleTM2_analysis_helperCode as hc


# DATE_STR = "17 July 2020"
# VERSION = "2_iii"
# AUTHOR = "Oliver Bonham-Carter"
# AUTHORMAIL = "obonhamcarter@allegheny.edu"

"""The driver program for the analysis side of the thing. """


def begin():
	"""Driver function"""

	st.text(hc.banner0_str)
	st.sidebar.title("BeagleTM Data Analysis")
	st.sidebar.subheader(f"Date: {hc.DATE_STR}, Ver: {hc.VERSION}")
	st.sidebar.text("\U0001F415 \U0001F631 \U0001f5ff \U0001F608 \U0001f600 ")
 	# Create a text element and let the reader know the data is loading.

	# get and load the file.

	myFile_str = hc.grabFile()
	try:
		data = hc.load_big_data(myFile_str)
		# create a dictionary having headers as keys and values as lists of column data.
		data_dic = hc.createMasterDataDic(data)
	except:
		st.sidebar.error("No data entered...")

# menu system
	doThis_sb = st.sidebar.selectbox(
		"What are we doing with this data?",
		[
			"ReadMe",
			"Show_data",
			"Articles connected by pmids",
			"Articles having ANY of the selected keywords",
			"Articles having ALL of the selected keywords",
			"Heatmaps of keyword saturation"
		],
	)
	if doThis_sb == "ReadMe":
		with open("README.md") as readme_file:
			st.markdown(readme_file.read())


	if doThis_sb == "Show_data":
		hc.showData(data)


	if doThis_sb == "Articles connected by pmids":
		hc.articleConnectivity(data_dic)


	if doThis_sb == "Articles having ANY of the selected keywords":
		hc.keywordAnalysis(data_dic)


	if doThis_sb == "Articles having ALL of the selected keywords":
		hc.keywordAndkeywordsInArticle(data_dic)

	if doThis_sb == "Heatmaps of keyword saturation":
		hc.keywordSaturation(data_dic)

	hc.writer("\U0001F415 WOO WOO!! \U0001F415")
	hc.writer(" ok :","computer")
		# end of begin()
#
#
# 	# progress_bar = st.progress(0)
# 	#
# 	# for i in range(100):
# 	# 	# Update progress bar.
# 	# 	progress_bar.progress(i)
#



begin()
