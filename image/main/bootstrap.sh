#!/bin/bash

# ...env
mkdir -p /$PROJECT/.env
source /usr/local/bin/virtualenvwrapper.sh
mkvirtualenv $PROJECT
pip install -r /tmp/requirements.txt

# ...
ln -s /usr/local/lib/python3.6/site-packages/cv2.cpython-36m-x86_64-linux-gnu.so /$PROJECT/.env/main/lib/python3.6/site-packages/cv2.cpython-36m-x86_64-linux-gnu.so