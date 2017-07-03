FROM python:2.7-slim
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
RUN apt-get -y update
RUN apt-get install -y --fix-missing \
    build-essential \
    python-matplotlib \
    python-scipy \
    python-skimage \
    python-pip \
    cmake \
    gfortran \
    git \
    wget \
    curl \
    graphicsmagick \
    libgraphicsmagick1-dev \
    libatlas-dev \
    libavcodec-dev \
    libavformat-dev \
    libboost-all-dev \
    libgtk2.0-dev \
    libjpeg-dev \
    liblapack-dev \
    libswscale-dev \
    pkg-config \
    python-dev \
    python-numpy \
    python-protobuf\
    software-properties-common \
    zip \
    && apt-get clean && rm -rf /tmp/* /var/tmp/*

RUN pip install Pillow
RUN pip install --upgrade scikit-image

RUN cd ~ && \
    mkdir -p dlib && \
    git clone https://github.com/davisking/dlib.git dlib/ && \
    cd dlib/ && \
    python setup.py install --yes USE_AVX_INSTRUCTIONS


