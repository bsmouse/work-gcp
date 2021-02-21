#!/bin/bash

raspivid -o - -t 0 -vf -hf -w 1280 -h 720 -fps 25 -b 1500000 | ffmpeg -i - -vcodec copy -an -f rtp_mpegts rtp://192.168.10.12:8554/

# ffplay -x 720 rtp://192.168.10.12:8554/
