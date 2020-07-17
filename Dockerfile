FROM python:3
# see notes from ref https://discuss.streamlit.io/t/how-to-use-streamlit-in-docker/1067/7
# RUN apt-get update

RUN \
    apt-get update &&\
    apt-get install -y git &&\
    apt-get install -y htop &&\
    apt-get install -y vim &&\
		apt-get install -y python3 &&\
		apt-get install -y python3-pip &&\
		pip3 install streamlit &&\
		pip3 install pyvis &&\
		pip3 install spacy &&\
		pip3 install pytest &&\
		pip3 install plotly_express &&\
		pip3 install pip install jsonpickle

# RUN useradd beagletm2
# RUN mkdir /home/beagletm2
# RUN export HOME=/home/beagletm2

WORKDIR /home/beagletm2
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN mkdir -p /root/.streamlit

RUN bash -c 'echo -e "\
[general]\n\
email = \"\"\n\
" > /root/.streamlit/credentials.toml'

RUN bash -c 'echo -e "\
[server]\n\
enableCORS = false\n\
" > /root/.streamlit/config.toml'

EXPOSE 8501

CMD bash


# Summary of commands
# Build: sudo docker build -t beagletm2 .
# Mount local directory and run container:
# sudo docker run -it -p 8501:8501 --mount type=bind,source=$PWD,target=/home/beagletm2 beagletm2
