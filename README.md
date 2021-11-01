##### BeagleTM: PubMed Interactive Knowledge Discovery
##### Date: 1 November 2021
##### Oliver Bonham-Carter, [Allegheny College](https://allegheny.edu/)
##### email: obonhamcarter@allegheny.edu

---
![logo](graphics/beagleTM_logo2.png)

[![MIT Licence](https://img.shields.io/bower/l/bootstrap)](https://opensource.org/licenses/MIT)
[![Built with spaCy](https://img.shields.io/badge/built%20with-spaCy-09a3d5.svg)](https://spacy.io)
[![Built with Streamlit](https://img.shields.io/badge/built%20with-Streamlit-09a3d5.svg)](https://www.streamlit.io/)
[![Build Status_OpenSource](https://travis-ci.com/developmentAC/beagleTM.svg?token=swrouvRyxqupKYRs8yq8&branch=master)](https://travis-ci.com/developmentAC/beagleTM.svg?branch=master&status=passed)
[![Build Status_devi](https://travis-ci.com/developmentAC/beagletm_devi.svg?token=swrouvRyxqupKYRs8yq8&branch=master)](https://travis-ci.com/github/developmentAC/beagletm_devi)
[![codecov](https://codecov.io/gh/myResearchTM/beagleTM/branch/master/graph/badge.svg)](https://codecov.io/gh/myResearchTM/beagleTM)
[![BLM](https://img.shields.io/badge/BlackLivesMatter-yellow)](https://blacklivesmatter.com/)

GitHub link: https://github.com/developmentAC/beagleTM

## Table of contents

* [Overview](#overview)
* + [Relationship Networks](#relationship-networks)
* [Command Summary](#command-summary)
* + [Docker Desktop](#docker-desktop)
* [Keywords](#keywords)
* [Running BeagleTM](#running-beagleTM)
* + [Run a parser job](#run-a-parser-job)
* + [Run an analysis job](#run-an-analysis-job)
* [Analysis methods](#analysis-methods)
* + [Run a Parsing Job](#run-a-parsing-job)
* [Analysis](#analysis)
* + [What are we doing with this data?](#What-are-we-doing-with-this-data)
* [Setting up the corpus](#setting-up-the-corpus)
* [Extra Notes](#extra-notes)
* [Citing](#citing)
* [A Work in Progress](#a-work-in-progress)


## Overview

BeagleTM is an interactive text mining tool to facilitate discovery of knowledge in [PubMed](https://pubmed.ncbi.nlm.nih.gov/) peer-reviewed articles.

BeagleTM Named after my puppy Beagle, Flint, who spends all his time rooting around with his nose to the ground. In following his lead, PubMed articles can also be discovered in a similar fashion.

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


## Command Summary

Here are the commands that you will be using to run this application. Involved discussion is below and you are encouraged to read through it before you run a major project. Before you can proceed with the commands below, please install `python-pip` and `pipenv`. Below are offered some sample commands to run a parsing and analysis job using the sample keyword file, `keywords_sample_i.md`.



### Docker Desktop

While the literature parsing stage is not recommended to be run inside a Docker Desktop  (https://www.docker.com/) container, the analysis portion of a project is recommended to be utilized _inside_ a container. In the below flowchart, we note that a Docker Desktop is used for an analysis of results using Streamlit (https://www.streamlit.io/).

![The flowchart of programs, File: flowchart.png](graphics/flowchart.png)


#### OS-specific scripts to build and run containers
The following bash scripts simplify building the container.


| OS  | Building  | Running  |
|---|---|---|
| MacOS  		|  `./build_macOS.sh` |  `./run_macOS.sh` |
| Linux   	|  `./build_linux.sh` | `./run_linux.sh`  |
| Windows 	|  `build_win.bat` 		|  `run_win.bat` |


These files may be found in the directory, `dockerRunScripts/` and the builder require a copy of `Dockerfile` to run. The `Dockerfile` is found in the main directory and so it is recommended that the user stay in the main and enter the command, ` sh ./dockerRunScripts/build_macOS.sh` or similar to build a container. To run the container, type the command ` sh ./dockerRunScripts/run_macOS.sh`. Us an equivalent command for each OS.


Please note that you may be required to enter your password twice, depending on your machine. The first time you enter your password will be to build and initialize the Docker container. The second time you enter your password will be to change ownership of your output files from `root` to `$USER` once you exit the container.


#### Keywords

To begin a parsing job, the keyword file, `myKeyword.md`,  written in [Markdown](https://www.markdownguide.org/cheat-sheet/) must have the first line, `#### keywords`, which is followed by a line-by-line listing of searchable words in the PubMed abstracts. There is no limit to the number of keywords although it should be mentioned here that the resulting output file may become too large to be analyzed in feasible time. Therefore, it is advised that the keywords lists be no longer than necessary, and be very specific to the type of Knowledge being searched.  

```
#### keywords
keyword_1
keyword_n
```

---
## Running BeagleTM

#### Run a parser job

To search for knowledge in PubMed articles to create a literature review, all keywords must be known before the task is begin. These keywords are then parsed in a corpus and articles which contain any occurrences are recorded in an output file. The output files must then be analyzed by another set of files which involves Streamlit to simplify the analysis. Below, we discuss each operation; parsing and the analysis of results.

The literature parsing operation can be initiated by the following command at the bash or command prompt.

``` bash
python3 beagleTM2_parser.py keywords_sample_i.md
```
The output files of this operation will be placed into the `data/` directory. You will direct the analysis program (running in a Docker container, using Streamlit) to these files to perform an analysis.

#### Run an analysis job

Inside a Docker Desktop container, we can use the following command at the containers bash prompt.

```bash
streamlit run beagleTM2_analysis_i.py
```

When running your container, to access Streamlit, you will need to use your browser using the link, `http://127.0.0.1:8501/`. Once Streamlit is running the analysis program, then direct the program to the `data/` directory to load the output files from the parsing operation above.

#### Analysis methods

When you engage Streamlit, you will see the below URL information on your screen.
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
 - **Show_data** : Displays a data table of the current data.


 - **Articles connected by pmids** : We use networks (from the `pyvis` library) to get a view of all articles in the dataset along with their connections to their supporting reference articles. Here we note that the red and blue nodes indicate main and reference articles, respectively. From this view, we can see which reference articles are being listed by more than one article.

 - **Articles having ANY of the selected keywords** : By selecting keywords in the selection field, we are able to see which articles surface to have _at least one_ of the keywords in their abstracts. All abstracts for which any one these keywords is presents may suggest a loose type of inter-relationship.

 - **Articles having ALL of the selected keywords** : By selecting keywords in the selection field, we are able to see which articles surface to have _ALL_ of the keywords in their abstracts, simultaneously. These papers are rare and are to be considered *strong* papers since they contain all requested keywords. In addition, these papers may serve to connect the keywords in some way using published research.

  We note that abstracts are carefully worded short texts in which each word seemingly plays a central role in the context of the article. To discover an abstract for which all supplied words are present may suggest that the keywords share a _guilt by association_ and we may perhaps conclude that a strong relationship exists. Please also note that as lists of keywords extend, it is less likely to find them all in a single abstract.


 - **Heatmaps of keyword saturation** :
 Viewing articles as heatmaps allows us to determine which articles have  most of the supplied keywords. On the left, links to the PubMed articles may be used to access articles which may be more important to a particular search for knowledge. Please note that you may need to zoom-in (see controls at the upper right in heatmap plot) to be able to find the exact article link for the line in the heatmap. This would be necessary in the case of many articles in the dataset in which  keywords have been found.

---

## Setting up the corpus

PubMed offers its articles as a download from ftp://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_bulk/ in two types of  packages: _commercial_ and _non-commercial_. For details about these two types of downloads, please see the _readme.me_ file at ftp://ftp.ncbi.nlm.nih.gov/pub/pmc/.

Bash scripts may be employed to automate the download and un-tarring processes. The following bash scrips are included in the `buildCorpus/` directory and are discussed below.  These scripts create the directory `corpus/` which must be copied to the BeagleTM project main directory so that the parser and analyzer files are able to use it.

Remember that if the corpus directory is changed to another name, then this alteration is to be updated in the code (see [Parsing](#parsing) Section, below.)


To build the corpus, start from the `buildCorpus/` directory. Then run the bash script with the following command; `sh beagletm_wget.sh`, to perform downloads of the compressed literature from PubMed.

The code is shown below.

```
# Date: 7 Dec 2020
# Reference: data from ncbi: ftp://ftp.ncbi.nlm.nih.gov/pub/pmc/

# keep a log of the download
mkdir log
wget ftp://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_bulk/comm_use.A-B.xml.tar.gz 1>log/ab_out.1 2>log/ab_download.1 &
#wget ftp://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_bulk/non_comm_use.A-B.xml.tar.gz 1>log/ab_nonComm_out.1 2>log/ab_nonComm_download.1 &

wget ftp://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_bulk/comm_use.C-H.txt.tar.gz  1>log/ch_out.1 2>log/ch_download.1 &
#wget ftp://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_bulk/non_comm_use.C-H.xml.tar.gz 1>log/ch_nonComm_out.1 2>log/ch_nonComm_download.1 &

wget ftp://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_bulk/comm_use.I-N.txt.tar.gz 1>log/in_out.1 2>log/in_download.1 &
#wget ftp://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_bulk/non_comm_use.I-N.xml.tar.gz 1>log/in_nonComm_out.1 2>log/in_nonComm_download.1 &

wget  ftp://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_bulk/comm_use.O-Z.xml.tar.gz 1>log/oz_out.1 2>log/oz_download.1 &
#wget  ftp://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_bulk/non_comm_use.O-Z.xml.tar.gz 1>log/oz_nonComm_out.1 2>log/oz_nonComm_download.1 &
ls -l log/

```

Note: The progress of the download can be checked by the command, `tail log/*download* -n 5` which will display the current obtained percentage of each corpus file by reading the log contained in the corresponding `*download*` files.


Once the data files have been downloaded, they must be un-tarred by running the following command; `sh beagletm_untar.sh`. This file is to be fun from the directory that contains the compressed data files. Since PubMed periodically updates its downloadable data files, you will also need to recreate your corpus accordingly.

The code is shown below.

```
# Date: 7 Dec 2020
# Reference: data from ncbi: ftp://ftp.ncbi.nlm.nih.gov/pub/pmc/

mkdir corpus
cd corpus
mkdir log
#untar a file in the background

tar -zxvf ../comm_use.A-B.xml.tar.gz 1>log/tar_ab_commUse_out.1 2>log/tar_ab_commUse_err.1 &
tar -zxvf ../comm_use.C-H.txt.tar.gz 1>log/tar_ch_commUse_out.1 2>log/tar_ch_commUse_err.1 &
tar -zxvf ../comm_use.I-N.txt.tar.gz 1>log/tar_in_commUse_out.1 2>log/tar_in_commUse_err.1 &
tar -zxvf ../comm_use.O-Z.xml.tar.gz 1>log/tar_oz_commUse_out.1 2>log/tar_oz_commUse_err.1 &

```

Once the `corpus/` directory has been created and contains the uncompressed datafiles, it must be moved to the main directory of the BeagleTM project so that the parser program can find it. Alternatively, if moving the corpus is not convenient, the parser and analysis Python programs could be edited to be able to find the corpus.


---

### Extra notes

#### Parsing

Parsing is completed by two files; `beagleTM2_parser.py` and its associated file, `beagleTM2_parser_helperCode.py`. The path to the `corpus/` directory has been hardcoded in the `beagleTM2_parser_helperCode.py`, however, if using an external hard drive or similar, a path to `corpus/` could be altered by updating the global variable, `CORPUS_DIR` as shown below.


```
# configure your corpus directory here.
#CORPUS_DIR = "corpus/" # local directory # former path and directory
CORPUS_DIR = "myNewCorpusDirectory/" # new path and directory
```


#### pipenv
To develop this code, `pipenv` was used to maintain packages and can be used to run BeagleTM parsing. Information about this coding environment may be found from https://pypi.org/project/pipenv/. A handy cheat sheet for the commands may be found at: https://pipenv-fork.readthedocs.io/en/latest/. If you require a `requirements.txt` file, then this file may be created by `pipenv` using the included `Pipfile` with the following command.

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

#### Supporting libraries
Please see the `Piplock` file for the details of the libraries necessary for the project.

#### Run a parsing job with pipenv

Use the following command to run your parsing step.
```
pipenv run python3 beagleTM2_parser.py keywords_sample_i.md
```

This operation will create a file called `all_keywords4_analysis.csv`. The filename of the keyword file has become a part of this output file to determine the origins of this data set.

#### Run an analysis Job with pipenv

Use the following command to employee Streamlit with pipenv to start up the analysis portion of your project.

``` bash
pipenv run streamlit run beagleTM2_analysis_i.py

```
---

## Citing this work

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

## A work in progress

Check back often to see the evolution of the project!! BeagleTM is a work-in-progress. Updates to the methods and tests for the code will come soon and I will continue to update the repository with updates. If you would like to contribute to this project, __then please do!__ For instance, if you see some low-hanging fruit or task that you could easily complete, that could add value to the project, then I would love to have your insight.

Otherwise, please create an Issue for bugs or errors. Since I am a teaching faculty member at Allegheny College, I may not have all the time necessary to quickly fix the bugs and so I would be very happy to have any help that I can get from the OpenSource community for any technological insight. Much thanks in advance. I hope that this project helps you find the knowledge from PubMed that you require for your project. :-)
