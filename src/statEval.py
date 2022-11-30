#!/usr/bin/python3
# -*- coding: utf-8 -*-


# from locale import dcgettext
import streamlit as st
import beagleTM2_parser_helperCode as hc
import pandas as pd


def getStats(data_dic):
    """STREAMLIT Function to gather individual counts of unique occurrences of selected keys"""
    st.subheader("Individual Column Output")

    with st.expander("Pretty Table"):
        mydf = pd.DataFrame(data_dic)
        st.dataframe(mydf)
        # st.balloons()
    st.markdown("---")
    # Columns/Layout
    myCol1, myCol2 = st.columns(2)

    with myCol1:

        myKey_list = st.multiselect(
            "Select keywords to determine unique occurrences.", data_dic.keys(), []
        )
        # st.write(f"{data_dic.keys()}")
        # # dict_keys(['title', 'abstract', 'pmid', 'journal', 'year', 'references', 'keyword', 'counts'])

    st.markdown("---")

    with myCol2:
        st.write("Extract these columns")

        # st.dataframe(myKey_list)
        st.text(myKey_list)

    dictKey_btn = st.button("Gather statistics based on which column of data?")

    if dictKey_btn:
        if len(myKey_list) > 0:  # anything to show?
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


# end of getStats()


def makeChartFromDic(in_dic):
    """STREAMLIT Function to make a a histogram from a dictionary"""
    shortData_df = pd.DataFrame.from_dict(in_dic, orient="index")
    st.bar_chart(shortData_df)
    # st.area_chart(shortData_df)


# end of makeChartFromDic()


def getListFromDic(in_dic, kw_str):
    """STREAMLIT Function to input a list. extract each line, sort it and place it in a dic where the lines can beb counted. pairs will be found by having them in abc-order."""
    tmp_dic = {}  # holds elements and counts

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
    """convert a list line as a string without punctuation marks"""
    # have a string: convert to list, sort it, convert back to string
    # st.write(f"getSortedListAsString 1:{in_str}, {type(in_str)}")

    # make a list
    try:
        in_list = list(
            in_str.replace("[", "")
            .replace("]", "")
            .replace("'", "")
            .replace(" ", "")
            .split(",")
        )
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


def getStatsAtParser(data_list, inFile0):
    """BASH Function to quickly make an output file of keyword percentages. A version of function is also used by streamlit but for ig data and automated projejcts, it is useful to have this data as a file after each parsing."""

    # print(hc.printWithColour(hc.BIBlue,f"\t [+] Columns: {data_list[0]}"))

    #  Columns of each line from data_list
    # 0:
    # ['Crystal structure of tri&#173;phenyl(vinyl)&#173;phospho&#173;nium tetra&#173;phenyl&#173;borate',

    # 1:
    #  ' The title ionic salt, C21H20P+&#183;C24H20B&#8722;, crystallized with two independent vinyl&#173;tri&#173;phenyl&#173;phospho&#173;nium cations and two independent tetra&#173;phenyl&#173;borate anions per asymmetric unit. These four independent moieties contain nearly perfect tetra&#173;hedral symmetry about their respective central C atoms. In the crystal, there are no &#960;-stacking or other inter&#173;molecular inter&#173;actions present. ',

    # 2:
    #  25484719,

    # 3:
    # # 'Acta Crystallogr Sect E Struct Rep Online',

    # 4:
    # '2014',

    # 5:
    # [],

    # 6:
    # [' central '],

    # 7:
    # [1]]

    keyWordGroups_list = (
        []
    )  # contains the words as they are found in lit, as pairs or singles

    # Place the value of the line element in the following variale.

    # mySearchKey_int = 4 # years
    mySearchKey_int = 6  # keywords ; group and singles

    # collect the data from one of the chosen columns.
    keyWordGroups_list = [col_list[mySearchKey_int] for col_list in data_list]

    # print(f"keyWordGroups_list:: {keyWordGroups_list}")

    sortedKeywords_dic = {}  # dic used to contain the sorted key words groups
    for unsorted_col_list in keyWordGroups_list:
        col_list = sorted(unsorted_col_list)
        wordGroup_str = (
            str(col_list)
            .replace(" ", "")
            .replace("'", "")
            .replace("[", "")
            .replace("]", "")
        )
        # print(f"col_list :: {col_list}")
        # print(hc.printWithColour(hc.BIBlue,f"\t [+] wordGroup_str = {wordGroup_str}, {type(wordGroup_str)}"))

        if wordGroup_str in sortedKeywords_dic:
            sortedKeywords_dic[wordGroup_str] = sortedKeywords_dic[wordGroup_str] + 1
        else:
            sortedKeywords_dic[wordGroup_str] = 1

    # print(hc.printWithColour(hc.BIGreen,f"sorted keywords : {sortedKeywords_dic}"))
    hc.saveStats(sortedKeywords_dic, inFile0 + "_KWGroups_")

    # end of getStatsAtParser()
