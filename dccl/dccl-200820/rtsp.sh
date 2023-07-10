#!/bin/bash

raspivid -o - -t 0 -vf -hf -n -w 1280 -h 720 -fps 25 | cvlc -vvv stream:///dev/stdin --sout '#rtp{sdp=rtsp://:8554/}' :demux=h264

# ffplay -x 720 -i rtsp://raspberry.bs:8554/
