#!/bin/bash
raspivid -n -t 0 -rot 180 -w 1280 -h 720 -fps 15 -b 300000 -co 60 -sh 40 -sa 10 -o - | gst-launch-1.0 -e -vvvv fdsrc ! h264parse ! rtph264pay pt=96 config-interval=5 ! udpsink host=notebook.pi port=5600
