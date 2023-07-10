#!/bin/bash

MY_IP=$(hostname -I)

#raspivid -o - -t 0 -vf -hf -w 1280 -h 720 -fps 25 -b 1000000 | gst-launch-1.0 -v fdsrc ! h264parse ! rtph264pay config-interval=1 pt=96 ! gdppay ! tcpserversink host=0.0.0.0 port=8554

# raspivid -t 0 -h 720 -w 1280 -fps 25 -b 2000000 -vf -hf -n -o - | gst-launch-1.0 -v fdsrc ! h264parse ! gdppay ! tcpserversink host=$MY_IP port=8554 | ./test-launch "( tcpclientsrc host=$MY_IP port=8554 ! gdpdepay ! avdec_h264 ! rtph264pay name=pay0 pt=96 )"
raspivid -t 0 -h 720 -w 1280 -fps 25 -b 2000000 -vf -hf -n -o - | gst-launch-1.0 -v fdsrc ! h264parse ! rtph264pay config-interval=1 pt=96 ! gdppay ! tcpserversink host=127.0.0.1 port=8554
