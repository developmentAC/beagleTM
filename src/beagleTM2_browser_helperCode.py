#!/usr/bin/python3
# -*- coding: utf-8 -*-

banner0_str = """
  ██████╗ ███████╗ █████╗  ██████╗ ██╗     ███████╗████████╗███╗   ███╗
  ██╔══██╗██╔════╝██╔══██╗██╔════╝ ██║     ██╔════╝╚══██╔══╝████╗ ████║
  ██████╔╝█████╗  ███████║██║  ███╗██║     █████╗     ██║   ██╔████╔██║
  ██╔══██╗██╔══╝  ██╔══██║██║   ██║██║     ██╔══╝     ██║   ██║╚██╔╝██║
  ██████╔╝███████╗██║  ██║╚██████╔╝███████╗███████╗   ██║   ██║ ╚═╝ ██║
  ╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝   ╚═╝   ╚═╝     ╚═╝
"""
# banner ref: https://manytools.org/hacker-tools/ascii-banner/

DATE = "29 November 2022"
VERSION = "0.2.7"
AUTHOR = "Oliver Bonham-Carter"
AUTHORMAIL = "obonhamcarter@allegheny.edu"

"""A body of code to assist with code from my programs. This helper code should be easier to maintain for a project. Right?"""


# Installation notes:
# python3 -m pip install --user streamlit

# main header column names: (for reference...)
# ["Title", "Abstract", "PMID", "Journal", "Year", "References", "Keyword", "Counts"]
# note: to run, type streamlit run <fileName.py>


import streamlit as st
import pandas as pd
import numpy as np
import math, sys, time, os, re
from pyvis.network import Network
from plotly import graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.express as px
import networkx as nx

import spacy  # needed to work with stopwords
from spacy.lang.en.stop_words import STOP_WORDS  # needed to work with stop words

import beagleTM2_parser_helperCode as phc  # for: checkDataDir()


# global variables
header_list = []  # initialize the header_list
FILE_EXTENTION = "csv"
DATADIR = "data/"
# OUTDATADIR = "/tmp/" #output directory
OUTDATADIR = "0_outAnalysis/"  # output directory

# @st.cache
# @st.cache(allow_output_mutation=True)
@st.cache(suppress_st_warning=True)
def load_big_data(myFile_str):
    """Loads the inputted data file"""
    data = pd.read_csv(myFile_str, low_memory=False)
    # 	st.text("Please load data")
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis="columns", inplace=True)
    return data


# end of load_big_data()


def writer(in_str, var=None):
    """Function to make it easy to use st.write(). This function abstracts st.write("".format())"""
    with st.expander("Writer: Pretty Table"):
        if var == None:  # there is no variable to add to a string
            st.write(in_str)

        else:
            in_str = in_str + ": {}"  # add braces
            st.write(in_str.format(var))  # input string should contain the "{}".
    return "ok computer"


# end of writer()


def getAllKeywords(data_dic):
    """Function to grab all keywords from all articles. Returns a list of keywords."""
    # import spacy # needed to work with stopwords
    # from spacy.lang.en.stop_words import STOP_WORDS # needed to work with stop words
    spacy_stopwords = (
        spacy.lang.en.stop_words.STOP_WORDS
    )  # list of meaningless stopwords ("of", "the", "his", "her", etc)
    # writer(spacy_stopwords)

    articleKeyWords_list = data_dic["keyword"]
    # st.write("my list of keywords: {}".format(articleKeyWords_list))

    keywords_set = set()
    stopWords_set = (
        set()
    )  # contains the keywords that were stopwords, sets for single kws only.
    for line in articleKeyWords_list:
        line_list = stringToList(line)
        # 		writer("line is ",line)
        for l in line_list:
            # 			writer("word is :",l)
            if l not in spacy_stopwords:  # word is not a stop word
                keywords_set.add(l)
            else:
                # writer("skipped stop word", l)
                pass
    # st.text("Keywords")

    dataframe = keywords_set

    # with st.expander("Show Keywords"):
    # 	if len(dataframe) > 0: # anything to show?
    # 		st.text(dataframe)

    tmp_list = []  # holds the list of keywords
    for i in keywords_set:
        tmp_list.append(i)

    return sorted(tmp_list)  # return a sorted list


# end of getAllKeywords()


def getPath():
    """Function to open the myPath.txt file to determine links to the results. Inside a container, the system paths are changed and container-based paths are inaccurate to find the results html files."""

    myPath = None
    try:
        with open("myPath.txt") as pathFile:  # pathFile is object reference
            myPath = pathFile.read().strip()  # remove the "\n" at the end of string
        return myPath
    except FileNotFoundError:
        return None


# end of getPath()


def stringToList(in_str):
    """converts a string that looks like a list, to a list. Ex: '[1,2,3]' -> [1,2,3]"""
    import ast

    if len(in_str) > 0:  # nothing in string
        if isinstance(in_str, str):  # this is a string?
            return ast.literal_eval(in_str)
    else:
        return []


# end of stringToList


def get_platformType():
    """Function to dermine the OS type."""

    platforms = {
        "darwin": "OSX",
        "win32": "Windows",
        "linux1": "Linux",
        "linux2": "Linux",
    }
    if sys.platform not in platforms:
        return sys.platform
    return platforms[sys.platform]


# end of get_platformType()


def openPage(myUrl):
    """function to open a a web page in a browser"""
    import webbrowser

    # writer("Opening url", myUrl)
    webbrowser.open(myUrl, new=0, autoraise=True)


# end of openPage()


def showMyPlot(G, plotName_str):
    """plots according to os type. It seems that macOS does not always open a plot."""
    platform_str = get_platformType().lower()
    # st.write(platform_str)
    # st.success(f" Output file saved: {plotName_str}")

    giveUserLink(plotName_str)

    if platform_str == "osx":
        st.write("osx machine... ")
        G.show(plotName_str)  # compile the graph?
        # tmp_str = "file:///private/" # used for /tmp
        # openPage(tmp_str + plotName_str)
        openPage(plotName_str)

    if platform_str == "linux":
        # st.write("linux machine ...")
        G.show(plotName_str)


# end of showMyPlot()


def createMasterDataDic(data_in):
    """function to create a dictionary of headers (keys; [Title, Abstract, PMID, Journal, Year, References, Keyword, Counts] and the list of data for each one of these keys (values). Returns the dictionary"""

    # st.write("createMasterDataDic()")
    # 	header_list = ["Title", "Abstract", "PMID", "Journal", "Year", "References", "Keyword", "Counts"]

    pmid_list = data_in["pmid"]
    # st.write("example of pmid_list: {}".format(pmid_list))
    refOfPMID_list = list(data_in["references"])

    # #Determine the headers of the data set.
    # header_list = []
    for i in data_in:
        header_list.append(i)
    # 	st.write(header_list)

    header_dic = {}
    tmp_list = []

    for i in header_list:
        # st.write(i, i.lower(), list(data_in[i.lower()]))
        tmp_list = list(data_in[i.lower()])
        # st.write(i, "::", tmp_list, "done")
        header_dic[i] = tmp_list

    return header_dic


# end of createMasterDataDic()


def getPmidsForKeywords(data_dic, keyword_list=[]):
    """Function to get a listing of article pmids for which a SINGLE keyword exists"""

    articleKeyWords_list = data_dic["keyword"]
    pmid_list = data_dic[
        "pmid"
    ]  # listed in an order of appearance. all lists in the data_dic have same order.

    myPmid_list = []  # store the pmids that we find for these keywords

    # writer("type(articleKeyWords_list)",type(articleKeyWords_list))
    # need to get the position in array of the article containing keyword
    counter = 1  # used to print the line number
    for position in range(len(articleKeyWords_list)):
        # st.write("position = {}, line ={}, type = {} ".format(line, articleKeyWords_list, type(articleKeyWords_list)))
        line_list = stringToList(articleKeyWords_list[position])  # working with a list
        # st.write("position = {}, line_list = {}".format(position, line_list))
        # output: position = 1, line_list = ['with', 'and', 'virus', 'is', 'in', 'with', 'rate', 'is', 'known', 'the', 'of', 'this', 'virus', 'in', 'we', 'the', 'of', 'in', 'samples', 'collected', 'from', 'in', 'the', 'of', 'we']

        for word in keyword_list:
            if word in line_list:
                # st.write("position : {}, data_dic['pmid'][position] : {}".format(position, data_dic["pmid"][position]))
                # st.write("\t Article number (position): <{}>, Word found <{}>, pmid : <{}>".format(counter, word, data_dic["pmid"][position]))
                # st.write("\t Word found <{}> in article : <{}>".format(word, data_dic["pmid"][position]))
                myPmid_list.append(data_dic["pmid"][position])
                counter += 1
            # st.write(myPmid_list) # [17961509,19102767] # listing of pmids for which word was found.
    return myPmid_list


# end of getPmidsForKeywords()


def newRefPlot(
    data_dic, pmid_list=[], showNodesPanel_bol=False, showPhysicsPanel_bol=False
):
    """New way of making a network of all pmids and their associated reference pmids. The pmid_list is the group of selected pmids to place into the network. If all pmids are to be placed in the network, then pmid_list is empty. We will use the position of the pmids lists. All lists in data have same positions for a single article."""

    pmid_dic = {}
    # st.write("newRefPlot() pmid_list= {}".format(pmid_list))

    # determine length of lists, to determine each position
    pos_list = []  # position in list of pmid; all list have same order of articles

    # working code for an empty pmid_list
    if (
        len(pmid_list) == 0
    ):  # then show all pmids, all positions of the pmids in the pmid_list.
        pos_list = [i for i in range(len(data_dic["pmid"]))]
    else:  # the pmid_list has selected pmids in it...

        # 		st.write(" else: pmid_list :{}".format(pmid_list))
        # 		st.write(" type(data_dic['pmid']) {}".format(type(data_dic["pmid"])) )
        # 		st.write(" data_dic: {}".format(data_dic))

        # note: data_dic["pmid"] is a list
        # gather the postitions of the selected article information.
        for p in pmid_list:
            # st.write(data_dic["pmid"].index(p))
            myPos_int = data_dic["pmid"].index(p)
            pos_list.append(myPos_int)
        # st.write(pos_list)

    # for each key, fill in the refs
    for q in pos_list:
        # st.write("q:{} , {}".format(q, data_dic["references"][q]))
        ref_list = stringToList(data_dic["references"][q])
        tmp_list = []
        tmp_list.append(ref_list)
        title = data_dic["title"][q]
        tmp_list.append(title)
        # st.write("tmp_list : {}".format(tmp_list))
        pmid_dic[data_dic["pmid"][q]] = tmp_list

    # st.write(" showNodesPanel_bol is {}".format(showNodesPanel_bol))
    # st.write(" showPhysicsPanel_bol is {}".format(showPhysicsPanel_bol))

    createNetwork(pmid_dic, showNodesPanel_bol, showPhysicsPanel_bol)


# end of newRefPlot()


def createNetwork(in_dic, showNodesPanel_bol, showPhysicsPanel_bol):
    """Function to take a dic and to build a network from it. Key = pmid, value = [refs]. We can selected whether we want panel to edit nodes or gravity
    in_dic must have format;
    [+] pmid_dic = {pmid_int : [[ref1_str, ..., refn_str], title_str]}
    [+] in_dic :{19102772: [[12764516, 15825143, 15702043], 'Identification of a novel picornavirus related to cosaviruses in a child with acute diarrhea'], 31622334: [[20536486, 17627978], 'Use of personalized risk-based screening schedules to optimize workload and sojourn time in screening programmes for diabetic retinopathy: A retrospective cohort study']}.
    """

    # get the network ready
    G = Network(height="1000px", width="95%", bgcolor="#222222", font_color="white", notebook = True)
    # Note: the above notebook = True is a fix from ref: https://stackoverflow.com/questions/75565224/in-pyvis-i-always-get-this-error-attributeerror-nonetype-object-has-no-attr

    # G.barnes_hut()

    # add the reference nodes
    for i in in_dic:

        # add a link to the article on pubmed
        myTitle_str = in_dic[i][1]
        # addToMyTitle_str = '<a href="https://pubmed.ncbi.nlm.nih.gov/{}" target="_blank"> Link:{}'.format(i,i)
        addToMyTitle_str = (
            '<a href="https://pubmed.ncbi.nlm.nih.gov/{}" target="_blank">'.format(i)
        )
        myTitle_str = addToMyTitle_str + myTitle_str
        # st.write("i = {} and list of refs = {}, title = {}".format(i, in_dic[i][0], myTitle_str))
        # main node
        G.add_node(
            str(i), color="#dd4b39", value=1, title=myTitle_str
        )  # , mass = 10)# [1] = title

        # reference nodes
        # are there any refs for the node?
        if len(in_dic[i][0]) != 0:

            for j in in_dic[i][0]:  # [0] = ref nodes
                # st.write("REF Node j :{}".format(j))
                refNode_str = str(j)  # add main node
                # st.write("pmid = <{}>, adding ref node j <<{}>>".format(i, refNode_str))

                # add the ref node; no titles to give so we use the pubmed link instead.
                myTitle = '<a href="https://pubmed.ncbi.nlm.nih.gov/{}" target="_blank"> Link:{}'.format(
                    refNode_str, refNode_str
                )
                G.add_node(refNode_str, title=myTitle)

                # draw edge between main node and ref node
                G.add_edge(str(i), refNode_str, value=1)
        else:
            # st.write("pmid = <{}> has no references. :-(".format(i))
            pass

    if showNodesPanel_bol == True:
        G.show_buttons(filter_=["nodes"])  # shown below graph in browser
    # G.show_buttons(filter_=['physics']) #shown below graph in browser

    if showPhysicsPanel_bol == True:
        G.show_buttons(filter_=["physics"])  # shown below graph in browser

    phc.checkDataDir(OUTDATADIR)
    plotName_str = OUTDATADIR + "pmidPlot.html"
    # plotName_str = "/tmp/pmidPlot.html"
    showMyPlot(G, plotName_str)  # push out the plot to browser


# end of createNetwork()


def getFileListing(corpusDir):
    """function to load a list of files from a directory. returns a list."""
    files_list = []  # holds each file and directory

    for root, dirs, files in os.walk(corpusDir):
        for file in files:
            if file.endswith(FILE_EXTENTION):
                dataFile = os.path.join(root, file)
                files_list.append(dataFile)
    # st.text(" getfileListing : files_list :{}".format(files_list))
    return files_list


# end of getFileListing


def grabFile():
    """Function to allow user to pick data file"""

    st.sidebar.text("Default data directory is :{}".format(DATADIR))
    dataDir_str = st.sidebar.text_input("Enter the path to data file.", DATADIR)
    files_list = getFileListing(dataDir_str)
    myFile_str = st.sidebar.selectbox("Choose the ANALYSIS file to load", files_list)

    # Below file chooser code does not work at this time (18 June 2020).
    # code ref: https://github.com/streamlit/streamlit/issues/120
    # with st.file_input() as input:
    # 	if input == None:
    # 		st.warning('No file selected.')
    # 	else:
    # 		file_contents = input.read()
    return myFile_str


# end of grabFile()


def setupNetwork():
    """Function to set up options of node or physics adjustment for networks"""
    # network Parameters ##############
    ###################################
    ###################################
    # from global variables
    st.subheader("Network options")
    showPhysicsPanel_bol = False
    showNodesPanel_bol = False

    networkOption_radio = st.radio(
        "Which interaction panel to include in the Network?",
        ("Physics", "Node", "Neither"),
    )

    if networkOption_radio == "Physics":
        st.text("Physics interaction")
        showPhysicsPanel_bol = True

    if networkOption_radio == "Node":
        st.text("Node interaction")
        showNodesPanel_bol = True

    if networkOption_radio == "Neither":
        st.text("Neither")
        showNodesPanel_bol = False
        showPhysicsPanel_bol = False

    return showNodesPanel_bol, showPhysicsPanel_bol


# end of setupNetwork()


def articleConnectivity(data_dic):
    """Function to show articles are connected to their references and, perhaps, to each other. Uses PMIDs from Main articles and References to draw networks of this connectivity"""

    st.title("Inter-connections")
    showNodesPanel_bol, showPhysicsPanel_bol = setupNetwork()
    pmid_list = data_dic[
        "pmid"
    ]  # listed in an order of appearance. all lists in the data_dic have same order.
    st.subheader("Pmid Analysis")
    dataframe = pmid_list
    # st.dataframe(dataframe)

    myPmids_list = []
    myPmidsShortList_list = []  # used for sidebar pmid loading

    my_str = st.sidebar.text_input("Enter PMID(s) to plot (separated by comma)")
    msg_str = "Please enter the PMIDs"
    if len(my_str) == 0:
        st.sidebar.text(msg_str)
    else:
        myPmidsShortList_list = re.split(r"[;,\s]\s*", my_str)
        msg_str = f"Entered: {myPmidsShortList_list}"
        st.sidebar.text(msg_str)

    quickPlot_btn = st.sidebar.button("MakeQuickPlot")
    if quickPlot_btn == True:
        try:
            myPmidsShortList_list = [
                int(i) for i in myPmidsShortList_list
            ]  # need elements as ints
            newRefPlot(
                data_dic,
                myPmidsShortList_list,
                showNodesPanel_bol,
                showPhysicsPanel_bol,
            )
        except ValueError:
            st.warning(
                "Problem with the inputted PMIDs. Please separate values by commas. "
            )

    myPmids_list = st.multiselect(
        "Select PMIDs of interest, or leave blank to view all as network.",
        pmid_list,
        [],
    )

    referenceNetwork_btn = st.button(
        "See network of articles and their associated references. Click for to all articles."
    )
    if referenceNetwork_btn == True:
        # newRefPlot(data_dic, myPmids_list)
        newRefPlot(data_dic, myPmids_list, showNodesPanel_bol, showPhysicsPanel_bol)

    manifest_btn = st.button("Save a manifest")
    if manifest_btn == True:
        saveManifest(myPmids_list, "PMIDs_")


# end of articleConnectivity()


def articlesContainingANY(data_dic):
    """Function to find articles having a particular keyword. Note: is several keywords are checked across articles, then any article having one of those keywords will turn up in results."""
    st.title("Analysis by keywords")
    showNodesPanel_bol, showPhysicsPanel_bol = setupNetwork()
    keyWords_list = getAllKeywords(data_dic)
    # contains all unique keywords across all articles; note it may slow things down to put this function here to be run each time...
    # writer(keyWords_list)
    myKeywords_list = st.multiselect(
        "Select keywords of interest, or leave blank to view all as network.",
        keyWords_list,
        [],
    )  # the selected key words from all articles. here we need a list of pmids of associated key words.
    # st.warning("Any keywords must be in an article abstract")
    wordNetwork_btn = st.button(
        "Find articles including ANY of these keywords in abstracts. Click for all keywords in set."
    )
    myPmids_list = []

    if wordNetwork_btn == True:
        myPmids_list = getPmidsForKeywords(
            data_dic, myKeywords_list
        )  # which articles have these keywords?

        # # remove repeating list numbers with a set.
        # writer("1. non-unique references in myPmids_list :",myPmids_list)
        myPmids_list = list(set(myPmids_list))
        # writer("2. unique elements myPmids_list :",myPmids_list)

        newRefPlot(data_dic, myPmids_list, showNodesPanel_bol, showPhysicsPanel_bol)

    manifest_btn = st.button("Save a manifest")
    if manifest_btn == True:
        saveManifest(myKeywords_list, "myKeywords_list")


# end of articlesContainingANY()


def showData(data):
    """shows the data in a table"""
    st.title("Dataframe")
    query_df = pd.DataFrame(data)
    st.dataframe(query_df)


# end fo showData()


def articlesContainingALL(data_dic):
    """Function to find articles having only all selected keywords. Articles must have simultaneously all chosen articles to be a result."""
    st.title("All chosen keywords in the same article")
    showNodesPanel_bol, showPhysicsPanel_bol = setupNetwork()

    keyWords_list = getAllKeywords(data_dic)
    potentialArticles_dic = (
        {}
    )  # contains a listing of articles for which keywords are found, need to find the pmids in all list values to determine which articles have all keywords included
    myPmids_list = []
    myPmid_set = set()

    myKeyWords_list = st.multiselect(
        "Select keywords of interest, or leave blank to view all as network.",
        keyWords_list,
        [],
    )  # the selected keywords from the user.

    wordNetwork_btn = st.button(
        "Find articles containing ALL selected keywords in abstracts. Click for all keywords in set."
    )

    if wordNetwork_btn == True:
        # check that all words are in same list of keywords from each article.
        hasAllKeywords_dic = {}  # keep track of which word is found in what set
        for i in range(
            len(data_dic["keyword"])
        ):  # keywords of article at ith position in data_dic["keyword"]

            checkTheseKeywords_list = data_dic["keyword"][
                i
            ]  # all keywords from this article
            flag_bol = True
            for myKW_str in myKeyWords_list:
                if myKW_str not in checkTheseKeywords_list:
                    flag_bol = False
                    # st.write("<{}> not in set : {}, flag is <{}>".format(myKW_str, checkTheseKeywords_list, flag_bol))
            if flag_bol == True:  # myKW_str must be in set.
                myPmid_set.add(data_dic["pmid"][i])
            # st.write(myPmid_set)
        myPmids_list = list(myPmid_set)

        if len(myPmids_list) > 0:  # contains some pmids
            newRefPlot(data_dic, myPmids_list, showNodesPanel_bol, showPhysicsPanel_bol)

        else:
            st.error("No hits found ...")

    manifest_btn = st.button("Save a manifest")
    if manifest_btn == True:
        saveManifest(myKeyWords_list, "myKeyWords_list")


# end of articlesContainingALL()


def getIntersection(in1_list, in2_list):
    """Function for determining the intersection of two lists. Returns the common elements."""
    return set(in1_list).intersection(in2_list)


# end of getIntersection()


def getLowercaseElements(in_list):
    """function to convert all strings in a list to lower case."""
    return [in_list[i].lower() for i in range(len(in_list))]


# end of get getLowercaseElements()


def simpleHeatmaps(data, data_dic):
    """Function to create a simple heatmap of keyword items in articles. This heatmap allows user to see which articles have combinations of keywords that may be more helpful to an analysis."""

    st.subheader("Keywords of articles")
    with st.expander("Pretty Table"):
        st.write(data)

    st.markdown("---")
    shortData_dic = {}  # dict to contain articles having two or more keywords
    myCol1 = "keyword"  # what col to work with?
    myCol2 = "pmid"

    keywordThreashold_sld = st.slider(
        "Enter minimum number of user-selected keywords per article.",
        0,
        (len(getAllKeywords(data_dic))),
        3,
    )
    st.write("Minimum keywords per article: ", keywordThreashold_sld)

    for i in range(len(data[myCol1])):
        if (
            len(stringToList(data[myCol1][i])) >= keywordThreashold_sld
        ):  # an article has at least a nubmer of keywords

            # st.write("num:",i, data[myCol1][i],type(data[myCol1][i]), data[myCol2][i], type(data[myCol2][i]))

            itemCol1 = stringToList(data[myCol1][i])
            itemCol2 = stringToList(str(data[myCol2][i]))

            # bad			shortData_dic[str(data[myCol2][i])] = itemCol1
            # 			shortData_dic[data[myCol1][i]] = str(data[myCol2][i])
            dicItem = str(itemCol1) + "_" + str(i)
            # 			st.write(dicItem)

            # 			shortData_dic[dicItem] = str(data[myCol2][i])
            shortData_dic[str(data[myCol2][i])] = dicItem

    # st.write("_shortData__",shortData_dic)
    shortData_df = pd.DataFrame.from_dict(shortData_dic, orient="index")
    with st.expander("See all data"):
        st.bar_chart(data["keyword"])
    st.bar_chart(shortData_df)  # self scaling according to data


# end of simpleHeatmaps()


def keywordSaturation(data_dic):
    """Function to study "Heatmaps of keyword saturation": the number of times a selected keyword turns up in abstracts"""

    st.title("All chosen keywords in the same article")

    keyWords_list = getAllKeywords(data_dic)
    keyWords_list = getLowercaseElements(keyWords_list)
    myKeyWords_list = st.multiselect(
        "Select keywords of interest, or leave blank to view all as network.",
        keyWords_list,
        [],
    )
    # the selected key words from the user.

    wordNetwork_btn = st.button(
        "Find articles including ALL keywords in their abstracts. Click to default to all keywords."
    )
    if wordNetwork_btn == True:

        if len(myKeyWords_list) == 0:  # is empty
            myKeyWords_list = keyWords_list  # use all keywords
            st.text("Using all keywords ...")

        abstract_list = data_dic["abstract"]
        abstract_list = getLowercaseElements(abstract_list)  # get lower case elements

        content_list = []  # holds the amount of kw content in each abstract
        keyword_list = []  # holds the keeps track of keyword order
        pmid_list = []  # holds the pmids in the order of articles

        for i in range(len(abstract_list)):
            kwCounts_int = 0  # contains tha number of times that keywords have been found in string
            for kw in myKeyWords_list:
                # 				st.text("abstract number <{}>".format(i))
                if kw in abstract_list[i]:
                    # st.write("____ Found: <{}> in abstract : {}:  {} ::: {}".format(kw, i, data_dic["pmid"][i], abstract_list[i] ))

                    kwCounts_int += abstract_list[i].count(
                        kw
                    )  # the number of times that keyword has been found.
                    pmid_list.append(data_dic["pmid"][i])
                    content_flt = kwCounts_int / len(
                        abstract_list[i].split()
                    )  # the percent of words in a text of words.
                    content_list.append(content_flt)
                    keyword_list.append(kw)
        # get titles
        title_list = []
        for i in range(len(pmid_list)):

            # add a link to the article on pubmed
            addToMyTitle_str = '<a href="https://pubmed.ncbi.nlm.nih.gov/{}" target="_blank"> Link:{}'.format(
                pmid_list[i], pmid_list[i]
            )
            # myTitle_str = myTitle_str + addToMyTitle_str
            title_list.append(addToMyTitle_str)

        # writer("content_list =",content_list)
        # writer("keyword_list =", keyword_list)
        # writer("pmid_list =", pmid_list)
        phc.checkDataDir(OUTDATADIR)  # check that the directory exists
        plotName_str = OUTDATADIR + "contentHeatmap.html"

        # # current way to plot heatmaps
        # trace = go.Heatmap(x = keyword_list, y = title_list, z = content_list, type = 'heatmap', colorscale = 'Viridis')
        # data = [trace]

        # use log transform to see the results better?
        # st.write("Before log transform:",content_list)
        # #content_list = getLogTransform(content_list,10)
        # # content_list = [1,2,3,4,5,6,7,8]
        # st.write("After log transform:",content_list)

        trace = go.Heatmap(type="heatmap", z=content_list, colorscale="Viridis")
        data = [trace]

        # note: the colours of the heatmap can be altered with the following lines.

        # contrasted for large sets of articles
        if len(pmid_list) > 300:  # small scale
            fig = px.density_heatmap(
                data,
                x=keyword_list,
                y=title_list,
                nbinsx=20,
                nbinsy=20,
                color_continuous_scale=[
                    [0, "grey"],
                    [0.005, "yellow"],
                    [1, "rgb(0, 0, 255)"],
                ],
            )

        # contrasted for few articles
        else:  # large scale
            fig = px.density_heatmap(
                data,
                x=keyword_list,
                y=title_list,
                nbinsx=20,
                nbinsy=20,
                color_continuous_scale=[
                    [0, "grey"],
                    [0.005, "yellow"],
                    [0.05, "rgb(0, 0, 255)"],
                ],
            )

        fig.update_layout(
            title="Heatmap of Results",
            xaxis_title="Keywords",
            yaxis_title="PubMed Links",
            font=dict(family="Courier New, monospace", size=18, color="#7f7f7f"),
        )
        plot(fig, filename=plotName_str)
        giveUserLink(plotName_str)

    manifest_btn = st.button("Save a manifest")
    if manifest_btn == True:
        saveManifest(myKeyWords_list, "Keywords_")


# end of keywordSaturation()


def giveUserLink(plotName_str):
    """function to show the path and file of outputted plots. The user may click on a copy to clipboard button"""
    # st.success("giveUserLink()")
    path_str = getPath()
    tmpAddress_str = ""
    if path_str != None:

        link_str = "file://" + f"{path_str}/{plotName_str}"
        st.markdown(f"Output file saved:\n ##### {link_str}")

    else:
        link_str = "file://" + f"{plotName_str}"
        st.markdown(f"Output file saved:\n ##### {link_str}")

    tmpAddress_str = f"{link_str}"
    # st.success(st.code(tmpAddress_str))
    st.code(tmpAddress_str, language="bash")


# end of giveUserLink()


def getLogTransform(in_list, base_int):  # UN-USED AT THIS TIME
    """Function to log-transform all elements of a list. Inputs list and a log base, Returns a list."""
    tmp_list = []  # contains the transformed results.
    for i in range(len(in_list)):
        myVal = in_list[i]
        if isinstance(myVal, int) or isinstance(myVal, float):  # is a number
            tmp_list.append(math.log(in_list[i], base_int))
    return tmp_list
    # end fo getLogTransform()


def reduceResults(in_list, a_list, b_list, lowerBound_flt=0, upperBound_flt=100):
    """Function to get the upper half of the results. For example, each entered list has elements for numbers. We only want those elements which are above the average of all values in the list. The a_list and b_list arguments also need to be updated. The threshold value must be met for an element to remain in the list."""
    # print("  reduceResults()")
    # print("  in_list: {}\n  a_list: {}\n  b_list: {}\n  thresholds: {} to {}".format(in_list, a_list, b_list, lowerBound_flt, upperBound_flt))
    tmp_list = []
    newA_list = []
    newB_list = []
    for i in range(len(in_list)):
        # print("considering :",in_list[i])
        if in_list[i] > lowerBound_flt and in_list[i] <= upperBound_flt:
            tmp_list.append(in_list[i])  # grow new lists if condition is true
            newA_list.append(a_list[i])
            newB_list.append(b_list[i])
    return tmp_list, newA_list, newB_list


# end of reduceResults()


def addIt(in_str, my_list):
    """adds an element if not already in a list"""
    if in_str not in my_list:
        my_list.append(in_str)
    else:
        pass
    return my_list


# end of addIt()


def saveManifest(in_list, task_str):
    """Function to save the keywords of a network or heatmap. Task is heatmap or network saving activities."""
    from datetime import datetime

    # datetime object containing current date and time
    now = datetime.now()
    # st.text(f"{now} saving ...")

    # format for the file name:  dd_mm_YY_H_M_S
    dateAndTime_str = now.strftime("%d_%m_%Y_%H_%M_%S")
    # st.text(f"date and time = {dateAndTime_str}")

    phc.checkDataDir(OUTDATADIR)  # check that the directory exists
    fileName_str = OUTDATADIR + "manifest_" + task_str + str(dateAndTime_str) + ".md"

    if len(in_list) > 0:
        tmp_str = (
            tmp_str
        ) = f"#### Date and time:\n{dateAndTime_str}\n\n#### {task_str}\n\n"
        for i in in_list:
            tmp_str = tmp_str + str(i) + "\n"

        f = open(fileName_str, "w")
        f.write(tmp_str)
        f.close()

        st.success(f"Manifest saved: {fileName_str}")
        st.code(f"{fileName_str}", language="bash")
        # TODO: add clickable link to manifest file


# end of saveManifest()
