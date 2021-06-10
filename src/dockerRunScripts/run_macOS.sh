#!/bin/bash
# MacOS and Ubuntu container builder and executer
# Formatting
GREEN='\033[0;32m'        # Green
BIGreen='\033[1;92m'      # Green
NC='\033[0m' # No Colour

# Say something nice to the user. Note, $USER, is login account credential.
# Type 'whoami' to see who you are in Linux.
printf "\n [+] ${BIGreen} Hello ${USER}! Setting up your working container.${NC}\n [+]  ${BIGreen}You may be asked to enter your password.${NC}\n"

# recording the file path to help access the results pages from streamlit
pwd > myPath.txt

# Run container:
docker run --rm -it -p 8501:8501 -v $PWD:/root stevi

printf "\n  [+]  ${BIGreen} Returning file ownership from root to ${USER}.\n       You may be asked to reenter your password.${NC}\n"

# change ownership of a file to your own login if it was created in the docker container.
sudo chown $USER ./*
sudo chown $USER ./data/*
sudo chown $USER ./0_outAnalysis/*


# removing the myPath.txt file which is no longer going to be used.
rm myPath.txt

printf "\n  [+] ${BIGreen} The working container is now closed. ${NC}\n"
