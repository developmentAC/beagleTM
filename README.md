##### BeagleTM analysis project
##### Date: 18 June 2020
##### Oliver Bonham-Carter
##### email: obonhamcarter@allegheny.edu


[![Build Status](https://travis-ci.com/myResearchTM/beagleTM.svg?token=swrouvRyxqupKYRs8yq8&branch=master)](https://travis-ci.com/myResearchTM/beagleTM)
[![codecov](https://codecov.io/gh/myResearchTM/beagleTM/branch/master/graph/badge.svg)](https://codecov.io/gh/myResearchTM/beagleTM)
[![Built with spaCy](https://img.shields.io/badge/built%20with-spaCy-09a3d5.svg)](https://spacy.io)

##### Information:

Run the code script with the following command.
```bash
streamlit run [filename]
```

##### Supporting libraries

There are other libraries that may be necessary to install, depending on your system configuration. The libraries are listed below, along with the commands to install them.

Note: the below commands do not always run on all machines. Alternatively, you can try the following command, as adapted to the below commands.
 ```bash
 python3 -m pip install --user libraryName
 ```

 - Streamlit : the library which is used to provide the analysis and the visualation in a web browser environment. Streamlit’s open-source app framework is the easiest way for data scientists and machine learning engineers to create beautiful, performant apps in only a few hours!  All in pure Python. All for free. (reference: `https://www.streamlit.io/`). To install, use the following command.
 ```bash
 pip install streamlit
 ```


 - Spacy is a library for language processing and is used for some text mining manipulations (reference: `https://spacy.io/`). It can be installed with the following command:

 ```bash
 pip install spacy --user
 ```

 - Pytest : A framework that makes building simple and scalable tests easy. Tests are expressive and readable—no boilerplate code required. Get started in minutes with a small unit test or complex functional test for your application or library (reference: `https://docs.pytest.org/en/latest/`). Here, it is used to check the code of this project. It can be installed with the following command.
 ```bash
 pip install -U pytest
 ```

 - Coverage.py measures code coverage, typically during test execution. It uses the code analysis tools and tracing hooks provided in the Python standard library to determine which lines are executable, and which have been executed (reference:`https://pypi.org/project/coverage/`). This software can be installed with the following command.
  ```bash
  pip -m pip install coverage
  ```


 - Flake8 : a command-line utility for enforcing style consistency across Python projects. By default it includes lint checks provided by the PyFlakes project, PEP-0008 inspired style checks provided by the PyCodeStyle project, and McCabe complexity checking provided by the McCabe project. It will also run third-party extensions if they are found and installed (reference: `https://pypi.org/project/flake8/`). It can be installed with the following command.

 ```bash
 pip -m pip install flake8
 ```

 - PyFlakes
 - pycodestyle



 - Spacy is a library for language processing and is used for some text mining manipulations (reference: `https://spacy.io/`). It can be installed with the following command:

 ```bash
 pip install spacy --user
 ```

 - Not yet used: Commonmark is a markdown parcer (reference: `https://pypi.org/project/commonmark/`) and can installed with the following command.

 - Bokeh: bokeh.models.widgets
 - Plotly's plotly.express:
 ``` bash
 pip3 install plotly_express
```

## Web Interface

TextMining is mainly developed on its web interface with [Streamlit](https://www.streamlit.io)
in order to provide fast analysis and visualizations.

In order to run Streamlit, type and run the following command in your terminal.

```bash
pipenv run streamlit run streamlit_web.py
```

You then will see something like this

```
You can now view your Streamlit app in your browser.

Local URL: http://localhost:8501
Network URL: http://xxx.xxx.x.x:8501
```

End of readme.md

---
