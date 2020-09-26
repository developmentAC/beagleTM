FROM python:3
# see notes from ref https://discuss.streamlit.io/t/how-to-use-streamlit-in-docker/1067/7
# RUN apt-get update

RUN apt-get update && apt-get -y install git htop vim python3 python3-pip

RUN \
	pip install --upgrade pip && \
	pip install streamlit &&\
	pip install pyvis &&\
	pip install spacy &&\
	pip install pytest &&\
	pip install plotly_express &&\
	pip install pip install jsonpickle


WORKDIR /root/
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

CMD ["bash"]


# Summary of commands to build and run a container called, "devi"
# Build: docker build -t devi .
# Mount local directory and run container:
# docker run --rm -it -p 8501:8501 -v $PWD:/root devi
