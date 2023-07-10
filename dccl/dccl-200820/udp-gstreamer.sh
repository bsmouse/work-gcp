#!/bin/bash
## host주소는 MP가 실행될 PC의 주소임
raspivid -n -t 0 -rot 180 -w 1280 -h 720 -fps 15 -b 300000 -co 60 -sh 40 -sa 10 -o - | gst-launch-1.0 -e -vvvv fdsrc ! h264parse ! rtph264pay pt=96 config-interval=5 ! udpsink host=192.168.10.12 port=5600
## Mission Planner
# udpsrc port=5600 buffer-size=90000 ! application/x-rtp ! rtph264depay ! avdec_h264 ! queue leaky=2 ! videoconvert ! video/x-raw,format=BGRA ! appsink name=outsink sync=false

## TCP 방식
# raspivid -t 0 -h 720 -w 1080 -fps 25 -hf -b 2000000 -o - | gst-launch-1.0 -v fdsrc ! h264parse !  rtph264pay config-interval=10 pt=96 ! gdppay ! tcpserversink host=0.0.0.0 port=9010
## gstreamer 설치해서 실행
# .\gst-launch-1.0 -v tcpclientsrc host=192.168.10.16 port=9010 ! gdpdepay ! rtph264depay ! h264parse ! queue ! avdec_h264 ! videoconvert ! autovideosink sync=false
