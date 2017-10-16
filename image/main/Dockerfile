FROM python:3.6-slim
MAINTAINER Den Elston "4665284@gmail.com"

# ...
RUN apt-get update && apt-get install -y --no-install-recommends locales
RUN sh -c "echo 'LANG="'"'"ru_RU.UTF-8"'"'"' > /etc/default/locale"
ENV LANG='ru_RU.UTF-8' LANGUAGE='ru_RU:ru' LC_ALL='ru_RU.UTF-8'
RUN localedef -i ru_RU -f UTF-8 ru_RU.UTF-8

# ...
ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
    && echo $TZ > /etc/timezone \
    && dpkg-reconfigure -f noninteractive tzdata

# ...    
RUN apt-get update && apt-get install -y --no-install-recommends \
    make \
    gcc \
    build-essential \
    cmake \
    wget \
    unzip \
    yasm \
    pkg-config \
    libswscale-dev \
    libtbb2 \
    libtbb-dev \
    libjpeg-dev \
    libpng-dev \
    libtiff-dev \
    libjasper-dev \
    libavformat-dev \
    libpq-dev

RUN pip install numpy

WORKDIR /
RUN wget https://github.com/opencv/opencv/archive/3.3.0.zip \
&& unzip 3.3.0.zip \
&& mkdir /opencv-3.3.0/cmake_binary \
&& cd /opencv-3.3.0/cmake_binary \
&& cmake -DBUILD_TIFF=ON \
  -DBUILD_opencv_java=OFF \
  -DWITH_CUDA=OFF \
  -DENABLE_AVX=ON \
  -DWITH_OPENGL=ON \
  -DWITH_OPENCL=ON \
  -DWITH_IPP=ON \
  -DWITH_TBB=ON \
  -DWITH_EIGEN=ON \
  -DWITH_V4L=ON \
  -DBUILD_TESTS=OFF \
  -DBUILD_PERF_TESTS=OFF \
  -DCMAKE_BUILD_TYPE=RELEASE \
  -DCMAKE_INSTALL_PREFIX=$(python3.6 -c "import sys; print(sys.prefix)") \
  -DPYTHON_EXECUTABLE=$(which python3.6) \
  -DPYTHON_INCLUDE_DIR=$(python3.6 -c "from distutils.sysconfig import get_python_inc; print(get_python_inc())") \
  -DPYTHON_PACKAGES_PATH=$(python3.6 -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())") .. \
&& make install \
&& rm /3.3.0.zip \
&& rm -r /opencv-3.3.0




#...
RUN pip install --upgrade \
    pip \
    virtualenv \
&& pip install \
    virtualenvwrapper \
&& pip install --upgrade \
    virtualenvwrapper

# ...
# RUN rm -rf /var/lib/apt/lists/*


#..
RUN touch ~/.bashrc \
&& echo " " >> ~/.bashrc \
&& echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc

