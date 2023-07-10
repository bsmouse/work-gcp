#!/bin/bash

# export STREAMER_PATH=$HOME/Downloads/mjpg-streamer/mjpg-streamer-experimental/
# export LD_LIBRARY_PATH=$STREAMER_PATH
# $STREAMER_PATH/mjpg_streamer -i "input_raspicam.so -x 1280 -y 720 -fps 10" -o "output_http.so -w $STREAMER_PATH/www"

/usr/local/bin/mjpg_streamer -i 'input_raspicam.so -x 1280 -y 720 -fps 10' -o 'output_http.so -w /usr/local/share/mjpg-streamer/www'

