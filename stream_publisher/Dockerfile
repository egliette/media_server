FROM python:3.10-slim

WORKDIR /app

RUN python -m venv /venv
# Make sure we use the virtualenv:
ENV PATH="/venv/bin:$PATH"
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN python -m pip install --upgrade pip

# COPY install-packages.sh .
# RUN ./install-packages.sh

# Update and upgrade
RUN apt-get update && \
    apt-get -y upgrade

# Install GStreamer packages
RUN apt-get -y install --no-install-recommends \
    htop \
    libgstreamer1.0-dev \
    libgstreamer-plugins-base1.0-dev \
    libgstreamer-plugins-bad1.0-dev \
    gstreamer1.0-plugins-base \
    gstreamer1.0-plugins-good \
    gstreamer1.0-plugins-bad \
    gstreamer1.0-plugins-ugly \
    gstreamer1.0-libav \
    gstreamer1.0-tools \
    gstreamer1.0-x \
    gstreamer1.0-alsa \
    gstreamer1.0-gl \
    gstreamer1.0-gtk3 \
    gstreamer1.0-qt5 \
    gstreamer1.0-rtsp \
    gstreamer1.0-pulseaudio

# Install PyGObject and other build dependencies
RUN apt-get -y install --no-install-recommends \
    pkg-config \
    libcairo2-dev \
    gcc \
    python3-dev \
    libgirepository1.0-dev \
    python3-gi \
    gobject-introspection \
    gir1.2-gtk-3.0 \
    graphviz \
    ffmpeg

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && \
    pip install opencv-python-headless
