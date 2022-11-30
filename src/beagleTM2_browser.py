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
#
#
#

# import streamlit as st
import pandas as pd
import numpy as np
import time, sys, os
from pyvis.network import Network
from plotly import graph_objs as go
import networkx as nx

import spacy # needed to work with stopwords
from spacy.lang.en.stop_words import STOP_WORDS # needed to work with stop words

import beagleTM2_browser_helperCode as hc
import statEval as myStats

DATE = "6 July 2022"
VERSION = "0.2.3"
AUTHOR = "Oliver Bonham-Carter"
AUTHORMAIL = "obonhamcarter@allegheny.edu"

"""The driver program for the analysis side of the thing. """


def begin():
	"""Driver function"""

	st.text(hc.banner0_str)
	st.sidebar.title("BeagleTM Data Analysis")
	st.sidebar.subheader(f"Date: {hc.DATE}, Ver: {hc.VERSION}")
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
			"Article inter-connectivity",
			"Articles containing ANY of the selected keywords",
			"Articles containing ALL of the selected keywords",
			"Heatmaps of keyword saturation",
			"Make Simple Heatmaps",
			"Statistics"
		],
	)
	if doThis_sb == "ReadMe":
		with open("README.md") as readme_file:
			st.markdown(readme_file.read())


	if doThis_sb == "Show_data":
		hc.showData(data)


	if doThis_sb == "Article inter-connectivity":
		hc.articleConnectivity(data_dic)


	if doThis_sb == "Articles containing ANY of the selected keywords":
		hc.articlesContainingANY(data_dic)


	if doThis_sb == "Articles containing ALL of the selected keywords":
		hc.articlesContainingALL(data_dic)

	if doThis_sb == "Heatmaps of keyword saturation":
		hc.keywordSaturation(data_dic)

	if doThis_sb == "Make Simple Heatmaps":
		hc.simpleHeatmaps(data, data_dic)


	if doThis_sb == "Statistics":
		myStats.getStats(data_dic)


	st.write("\U0001F415 WOO WOO!! \U0001F415")



begin()
