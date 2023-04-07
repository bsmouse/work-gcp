#!/bin/bash

## 직접전송
raspivid -n -o - -t 0 -vf -hf -w 1280 -h 720 -fps 25 -b 1500000 | ffmpeg -i - -vcodec copy -an -f flv rtmp://dev20.gcp/record/bsmousekey?psk=a_secret_password

# ffplay -x 720 rtmp://dev20.gcp/stream/bsmousekey

## rtmp서버에서 전송
#gst-launch-1.0 -v rtmpsrc location=rtmp://localhost/stream/bsmousekey ! flvdemux ! h264parse ! rtph264pay pt=96 config-interval=5 ! udpsink host=14.51.92.165 port=5600

## Mission Planner
# udpsrc port=5600 buffer-size=90000 ! application/x-rtp ! rtph264depay ! avdec_h264 ! queue leaky=2 ! videoconvert ! video/x-raw,format=BGRA ! appsink name=outsink sync=false
