#!/usr/bin/python3
# -*- coding: utf-8 -*-


# keyword files: To prevent errors, keyword files
# must have the following first line of file to identify them.
KW_ID = "#### keywords"


import beagleTM2_parser_helperCode as hc


class KWmanager(object):
    """Manager for extracting and handling keywords class to open keyword files and prepare the words as strings"""

    def __init__(self, keywordFile):
        self.keywordFile = keywordFile
        # pass
        # end of __init__()

    def hello(self):
        print("\t [+] Hello from the KWmanager() class!")
        print("\t [+] Files to open : {}".format(self.keywordFile))
        # end of hello()

    def openKWFile(self):
        kwWords_list = []  # list to store keywords
        try:  # is the file there??
            # self.data = open(self.keywordFile, "r").read() #returns a string
            data = open(self.keywordFile, "r").readlines()  # returns a dict
        except IOError:
            tmp_str = "\aNo such file!!!! <{}>, so exiting".format(self.keywordFile)
            printErrorByPlatform(tmp_str)
            # print("  \a\tNo such file!!!! \"",self.keywordFile,"\" so exiting")
            sys.exit(1)
        # want dictionary of words, key = num, value = keyword
        for word_str in data:
            # clear about carrage returns and excess leading spaces. Add a space to both ends to ensure that the word itself is found, not this subset in another word.

            myword_str = " " + word_str.replace("\n", "").strip() + " "
            # print(f"currentWord :<{myword_str}>")
            kwWords_list.append(myword_str)

            #
            # original code; The below line ad some trouble discerning a word from a subset of a word; no spaces given on both sides of word.
            # kwWords_list.append(word_str.replace("\n","").strip())
            #

        # if kwWords_list[0] == KW_ID: # part of original code to discern the keyword tag to prevent loading non keyword files.
        if KW_ID in kwWords_list[0]:
            # print("\tThis is a keyword file: ",kwWords_list[0])
            kwWords_list.remove(kwWords_list[0])
            # print(kwWords_list)
            return kwWords_list
        else:
            printErrorByPlatform(
                " This is not a Keyword file... \n\tMust have <{}> at top of file to identify.".format(
                    KW_ID
                )
            )
            exit()
            # end of openKWFile()


# end KWmanager class
