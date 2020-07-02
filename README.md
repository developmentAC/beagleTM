##### BeagleTM: PubMed Interactive Knowledge Discovery
##### Date: 30 June 2020
##### Oliver Bonham-Carter, [Allegheny College](https://allegheny.edu/)
##### email: obonhamcarter@allegheny.edu



[![MIT Licence](https://img.shields.io/bower/l/bootstrap)](https://opensource.org/licenses/MIT)
[![Built with spaCy](https://img.shields.io/badge/built%20with-spaCy-09a3d5.svg)](https://spacy.io)
[![Built with Streamlit](https://img.shields.io/badge/built%20with-Streamlit-09a3d5.svg)](https://www.streamlit.io/)
[![Build Status_OpenSource](https://travis-ci.com/developmentAC/beagleTM.svg?token=swrouvRyxqupKYRs8yq8&branch=master)](https://travis-ci.com/developmentAC/beagleTM.svg?branch=master&status=passed)
[![Build Status_devi](https://travis-ci.com/developmentAC/beagletm_devi.svg?token=swrouvRyxqupKYRs8yq8&branch=master)](https://travis-ci.com/github/developmentAC/beagletm_devi)
[![codecov](https://codecov.io/gh/myResearchTM/beagleTM/branch/master/graph/badge.svg)](https://codecov.io/gh/myResearchTM/beagleTM)
[![BLM](https://img.shields.io/badge/BlackLivesMatter-yellow)](https://blacklivesmatter.com/)



## Table of Contents

* [Command Summary](#command-summary)
* [Overview](#overview)
* [Relationship Networks](#relationship-networks)

* [Keywords](#keywords)
* [Parsing](#parsing)
* + [Run a Parsing Job](#run-a-parsing-job)
* [Analysis](#analysis)
* + [Run an Analysis Job](#run-an-analysis-job)
* [What are we doing with this data?](#what-are-we-doing-with-this-data)
* [Supporting libraries](#supporting-libraries)
* [Citing](#citing)
* [A Work in Progress](#a-work-in-progress)

## Command Summary

Here are the commands that you will be using to run this application. Involved discussion is below and you are encouraged to read through it before you run a major project. Before you can proceed with the commands below, please install `python-pip` and `pipenv`. Below are offered some sample commands to run a parsing and analysis job using the sample keyword file, `keywords_sample_i.md`.



#### Open up a session of pipenv

To run this project's `virtualenv`, you can initiate the shell as shown below. When the shell is initiated, it is expected that the `Pipfile` file will guide the installation of the necessary libraries for the application.


``` bash
pipenv shell
```

##### Run the parser
``` bash
./beagleTM2_parser.py keywords_sample_i.md
```
or

``` bash
# python3
python beagleTM2_parser.py keywords_sample_i.md
```

##### Run the Analyzer
``` bash
 streamlit run beagleTM2_analysis_i.py
 ```
 and then, in the streamlit app, load the example output file, `all_keywords_sample_i_analysis.csv` from the directory, `data/`.



Alternately, you can run the parser and analyzer inside the `virtualenv` with `pipenv run` as shown below.


##### Run the Parser
``` bash
pipenv run python3 beagleTM2_parser.py keywords_sample_i.md
```


##### Run the Analyzer
```bash
pipenv run streamlit run beagleTM2_analysis_i.py
```


## Overview

BeagleTM is an interactive text mining tool to facilitate discovery of knowledge in [PubMed](https://pubmed.ncbi.nlm.nih.gov/) peer-reviewed articles.

BeagltTM Named after my puppy Beagle, Flint, who spends all his time rooting around with his nose to the ground. In following his lead, PubMed articles can also be discovered in a similar fashion.

BeagleTM has been designed to discover knowledge in PubMed articles and supporting references for the convenient creation of sophisticated literature reviews. The data for BeagleTM comes from curated article data made available from PubMed's [ftp site at ftp://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_bulk/](ftp://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_bulk/).

Textmining article information with BeagleTM involves two steps: _Parsing_ and _Analyzing_. During _parsing_, abstracts from the corpus documents are checked for their keyword content. Results are saved in an output document which undergo _analysis_ to find relationship networks (i.e., the interconnections between the knowledge of articles according to keyword content). These inter-relationships concern common themes of studies, articles of similar keywords, articles which are connected by common references and other types of bridges that serve to combine the intricate facts of knowledge areas.


#### Relationship Networks

A relationship network displays the connected information as obtained with keywords. The network includes the main articles for which the keywords are relevant, and their supporting references in which the keywords are likely to be relevant. Networks are written in `html` files and are to be opened in a browser, shown in Figure 1, each node of a network is labeled with PubMed’s PMID identifier number that serves to hyperlink nodes to articles at PubMed.

There are two types of nodes available in the networks: red and blue, for main and supporting reference articles, respectively. We note that the keywords are present in abstracts of main articles (red nodes), whereas they are not necessarily a part of supporting documents (blue nodes).

![A body of connected knowledge, File: connected.png](graphics/connected.png)
Figure 1: The articles relating to keywords create a body of knowledge. Main articles (red nodes, found by keyword content) are connected to their reference (blue nodes) articles. In networks, we are able to visualize which blue nodes serve as bridges for more than one red node to suggest that these references may be important bridges between works.


Shown in Figure 2, a mouse-over action of each node shows some metadata behind the nodes. In the case of red nodes (main articles), a title may be displayed which also serves as a link to the article at PubMed. In the case of blue nodes (reference articles), only a link to the article at PubMed may be obtained; the title information was not available during the text-mining process of the articles.


![Titles may be found in the networks, File mouseOver.png](graphics/mouseOver.png)
Figure 2: A screenshot of the red (main articles) and blue (supporting references). A mouse-over gives a title and link for red nodes and only a link for blue nodes.



Heatmaps are also available in which articles may be discovered according to their counts of supplied keywords, as shown in Figure 3.

![Heatmaps provide a new way of selecting articles, File heatmapOfResults.png](graphics/heatmapOfResults.png)
Figure 3: Heatmaps provide a new way of deciding which articles are most relevant according to the numbers of keywords in their abstracts. Each colour represents a different count of keywords found in abstracts and a mouse-over will show that count for the keyword's column.

---

## Setting Up The Corpus

PubMed offers its articles as a download from ftp://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_bulk/ in two types of  packages: _commercial_ and _non-commercial_. For details about these two types of downloads, please see the _readme.me_ file at ftp://ftp.ncbi.nlm.nih.gov/pub/pmc/.

Note: Bash scripts may be employed to automate the download and un-tarring of files from the ftp download site. In my own setup, my download script is the following.
```
# save the downloaded files to a directory
mkdir corpusData
cd corpusData
# keep track of how the download is going
mkdir log

# Download files in the background.
wget ftp://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_bulk/comm_use.A-B.xml.tar.gz 1>log/ab_out.1 2>log/ab_download.1 &

wget ftp://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_bulk/comm_use.C-H.txt.tar.gz  1>log/ch_out.1 2>log/ch_download.1 &

wget ftp://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_bulk/comm_use.I-N.txt.tar.gz 1>log/in_out.1 2>log/in_download.1 &

wget  ftp://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_bulk/comm_use.O-Z.xml.tar.gz 1>log/oz_out.1 2>log/oz_download.1 &

# make sure that there are no error messages which would be saved in a file.
ls -l log/
```
Once these files have been downloaded, to un-tar them, I use the following script. Naturally, you may need to edit the the script for your own usage.

```
# Save the uncompressed files to a directory.
mkdir allDocs
cd allDocs

# keep track of the untarring; this may take awhile.
mkdir log

#untar files in the background, save them to allDocs (the name of the corpus)
tar -zxvf ../comm_use.A-B.xml.tar.gz 1>log/tar_ab_commUse_out.1 2>log/tar_ab_commUse_err.1 &

tar -zxvf ../comm_use.C-H.txt.tar.gz 1>log/tar_ch_commUse_out.1 2>log/tar_ch_commUse_err.1 &

tar -zxvf ../comm_use.I-N.txt.tar.gz 1>log/tar_in_commUse_out.1 2>log/tar_in_commUse_err.1 &

tar -zxvf ../comm_use.O-Z.xml.tar.gz 1>log/tar_oz_commUse_out.1 2>log/tar_oz_commUse_err.1 &

```

Please consider updating the corpus files regularly as they are updated by PubMed.

---

## Overview to Parsing and Analysis
To search for knowledge in PubMed articles to create a literature review, all keywords must be known before the task is begin. These keywords are then parsed in a corpus and articles which contain any occurrences are recorded in an output file. The output files must then be analyzed by another set of files which involves Streamlit to simplify the analysis. Below, we discuss each operation; parsing and the analysis of results.


#### pipenv
To develop this code, `pipenv` was used to maintain packages. Information about this coding environment may be found from https://pypi.org/project/pipenv/. A handy cheat sheet for the commands may be found at: https://pipenv-fork.readthedocs.io/en/latest/. If you require a `requirements.txt` file, then this file may be created by `pipenv` using the included `Pipfile` with the following command.

``` bash
pipenv lock -r > requirements.txt
```

To import your libraries from the `requirements.txt` file, use the following command.
```
pipenv install -r requirements.txt
```

If the path is different from the local directory, then use the following.
```
pipenv install -r path/to/requirements.txt
```
---
## Parsing

Parsing is completed by two files; `beagleTM2_parser.py` and its associated file, `beagleTM2_parser_helperCode.py`. The path to the `corpus/` directory has been hardcoded in the `beagleTM2_parser_helperCode.py`, however, if using an external hard drive or similar, a path to `corpus/` could be altered by updating the global variable, `CORPUS_DIR` as shown below.


```
# configure your corpus directory here.
#CORPUS_DIR = "corpus/" # local directory # former path and directory
CORPUS_DIR = "myNewCorpusDirectory/" # new path and directory
```

#### Keywords

To begin a parsing job, the keyword file, `myKeyword.md`,  written in [Markdown](https://www.markdownguide.org/cheat-sheet/) must have the first line, `#### keywords`, which is followed by a line-by-line listing of searchable words in the PubMed abstracts. There is no limit to the number of keywords although it should be mentioned here that the resulting output file may become too large to be analyzed in feasible time. Therefore, it is advised that the keywords lists be no longer than necessary, and be very specific to the type of Knowledge being searched.  

```
#### keywords
keyword_1
keyword_n
```


#### Run a Parsing Job

Use the following command to run your parsing step.
```
pipenv run python3 beagleTM2_parser.py keywords_sample_i.md
```

This operation will create a file called `all_keywords4_analysis.csv`. The filename of the keyword file has become a part of this output file to determine the origins of this data set.

---

## Analysis

To analyze the results from `beagleTM2_parser.py`, [Streamlit](https://www.streamlit.io) is used to launch the analysis scripts: `beagleTM2_analysis_i.py` and `beagleTM2_analysis_helperCode.py`. To run an analysis of the data set, run the following command.

#### Run an Analysis Job
Use the following command to get Streamlit to start up the analysis step of your project.

``` bash
pipenv run streamlit run beagleTM2_analysis_i.py

```

You then will see something resembling the following.

```
You can now view your Streamlit app in your browser.

Local URL: http://localhost:8501
Network URL: http://xxx.xxx.x.x:8501
```

Open your browser to the URL: ```http://localhost:8501/```. The page that opens should be a Streamlit application with __BeagleTM Data Analysis__ displayed on the side bar, at the top left. To quit, use _Control-C_.

Enter the directory where the `csv` file may be found from the parsing operation. The directory `data/` is searched first for data files from the parser. The user is able to change to a different directory in the application.


#### What are we doing with this data?

Below we discuss some of the plots that are created by an analysis. All plots will be automatically saved to the `/tmp` directory. This project was created in Linux but if you are using Windows, then a search for the files (see the browser tabs) will show you where they are being saved. In addition,  if the Manifests (collections of keywords for the current plot) are saved by clicking on the _Save a Manifest_ button, then these files will also be saved in the same directory as the plots.

There are several options to choose from for the analysis.
 - **Show_data** : Displayes a data table of the current data.


 - **Articles connected by pmids** : We use networks (from the `pyvis` library) to get a view of all articles in the dataset along with their connections to their supporting reference articles. Here we note that the red and blue nodes indicate main and reference articles, respectively. From this view, we can see which reference articles are being listed by more than one article.

 - **Articles having ANY of the selected keywords** : By selecting keywords in the selection field, we are able to see which articles surface to have _at least one_ of the keywords in their abstracts. All abstracts for which any one these keywords is presents may suggest a loose type of inter-relationship.

 - **Articles having ALL of the selected keywords** : By selecting keywords in the selection field, we are able to see which articles surface to have _at least one_ of the keywords in their abstracts.

  We note that abstracts are carefully worded short texts in which each word seemingly plays a central role in the context of the article. To discover an abstract for which all supplied words are present may suggest that the keywords share a _guilt by association_ and we may perhaps conclude that a strong relationship exists. Please also note that as lists of keywords extend, it is less likely to find them all in a single abstract.


 - **Heatmaps of keyword saturation** :
 Viewing articles as heatmaps allows us to determine which articles have  most of the supplied keywords. On the left, links to the PubMed articles may be used to access articles which may be more important to a particular search for knowledge. Please note that you may need to zoom-in (see controls at the upper right in heatmap plot) to be able to find the exact article link for the line in the heatmap. This would be necessary in the case of many articles in the dataset in which  keywords have been found.


---

## Supporting libraries
Please see the `Piplock` file for the details of the libraries necessary for the project.

---

## Citing

If you would like to cite this work, then place use the following reference.
The current interactive BeagleTM software is a derivative of this former work.

``` bash
Bonham-Carter, Oliver. "BeagleTM: An Adaptable Text Mining Method for
 Relationship Discovery in Literature."
 Future of Information and Communication Conference.
 Springer, Cham, 2020.
```

The BibTex code is provided below.

``` bash
@inproceedings{bonham2020beagletm,
 title={BeagleTM: An Adaptable Text Mining Method for Relationship Discovery in Literature},
 author={Bonham-Carter, Oliver},
 booktitle={Future of Information and Communication Conference},
 pages={237--256},
 year={2020},
 organization={Springer}
}
```

## A Work In Progress


BeagleTM is a work-in-progress. Tests for the code will come soon and I will continue to update the repository with updates. If you would like to contribute to this project, __then please do!__ For instance, if you see some low-hanging fruit or task that you could easily complete, that could add value to the project, then I would love to have your insight.

Otherwise, please create an Issue for bugs or errors. Since I am a teaching faculty member at Allegheny College, I may not have all the time necessary to quickly fix the bugs and so I would be very happy to have any help that I can get from the OpenSource community for any technological insight. Much thanks in advance. I hope that this project helps you find the knowledge from PubMed that you require for your project. :-)
