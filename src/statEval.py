#!/usr/bin/python3
# -*- coding: utf-8 -*-

#from locale import dcgettext
import streamlit as st
import beagleTM2_browser_helperCode as brhc
import pandas as pd


def getStats(data_dic):
	""" function to gather individual counts of unique occurrences of selected keys """
	st.subheader("Individual Column Output")

	with st.expander("Pretty Table"):
		mydf = pd.DataFrame(data_dic)
		st.dataframe(mydf)
		# st.balloons()
	st.markdown("---")
	# Columns/Layout
	myCol1, myCol2= st.columns(2)


	with myCol1:

		myKey_list = st.multiselect('Select keywords to determine unique occurrences.', data_dic.keys(),[])
		# st.write(f"{data_dic.keys()}")
		# # dict_keys(['title', 'abstract', 'pmid', 'journal', 'year', 'references', 'keyword', 'counts'])

	st.markdown("---")

	with myCol2:
		st.write("Extract these columns")

		# st.dataframe(myKey_list)
		st.text(myKey_list)

	dictKey_btn = st.button("Gather statistics based on which column of data?")

	if dictKey_btn:
		if len(myKey_list) > 0: # anything to show?
			st.text(f"{myKey_list}")

			# get all rows in this column (they are lists), move them into a dictionary where each element is counted. by sure to abc-order elements to be able to count pairs when finding percentages
			for col_str in myKey_list:
				st.markdown(f"### {col_str}")
				with st.expander("See data"):
					st.dataframe(data_dic[col_str])
				keywordCounts_dic = getListFromDic(data_dic, col_str)
				# make a chart here for this col of dictionary
				makeChartFromDic(keywordCounts_dic)
				

	st.markdown("---")

	wordProportions_dic = {} # store the words and counts


# end of myStats()

def makeChartFromDic(in_dic):
	""" Function to make a a histogram from a dictionary"""
	shortData_df = pd.DataFrame.from_dict(in_dic, orient='index')
	st.bar_chart(shortData_df)
	# st.area_chart(shortData_df)
# end of makeChartFromDic()


def getListFromDic(in_dic,kw_str):
	""" Input a list. extract each line, sort it and place it in a dic where the lines can beb counted. pairs will be found by having them in abc-order. """
	tmp_dic = {} # holds elements and counts

	for i in in_dic[kw_str]:
		# st.write(i,type(i))
		# convert str to list.
		line_str = getSortedListAsString(i)

		if line_str in tmp_dic:
			tmp_dic[line_str] = tmp_dic[line_str] + 1
		else:
			tmp_dic[line_str] = 1
	with st.expander("Data in Dictionary Structure"):
		st.success(tmp_dic)
	return tmp_dic
# end of getListFromDic()


def getSortedListAsString(in_str):
	""" convert a list line as a string without punctuation marks """
	# have a string: convert to list, sort it, convert back to string
	# st.write(f"getSortedListAsString 1:{in_str}, {type(in_str)}")

	# make a list
	try:
		in_list = list(in_str.replace("[","").replace("]","").replace("'","").replace(" ","").split(","))
	# st.write(f"getSortedListAsString 2:{in_list}, {type(in_list)}")
	except AttributeError:
		return in_str

	# sort the list
	in_list = sorted(in_list)
	# st.write(f"getSortedListAsString 3:{in_list}, {type(in_list)}")

	# convert back to a string
	in_str = str(in_list)
	# st.write(f"getSortedListAsString 4:{in_str}, {type(in_str)}")

	return in_str
# end of getSortedListAsString()
