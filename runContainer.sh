# Formatting
GREEN='\033[0;32m'        # Green
BIGreen='\033[1;92m'      # Green
NC='\033[0m' # No Colour

# Summary of commands
# Build:
printf "\n [+] ${BIGreen} Hello ${USER}! Setting up your working container.${NC}\n [+]  ${BIGreen}You may be asked to enter your password.${NC}\n"
sudo docker build -t beagletm2 .
# Mount local directory and run container:
sudo docker run -it -p 8501:8501 --mount type=bind,source=$PWD,target=/home/beagletm2 beagletm2

printf "\n  [+] ${BIGreen} Ignore the below error messages if you have not done any work during this session. ${NC}\n"
# Cleaning up
sudo chown $USER __pycache__/
sudo chown $USER __pycache__/*

rm -r __pycache__
sudo chown $USER data/
sudo chown $USER data/*
sudo chown $USER 0_outAnalysis/
sudo chown $USER 0_outAnalysis/*
printf "\n  [+] ${BIGreen} The working container is now closed. ${NC}\n"
