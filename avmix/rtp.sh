#!/bin/bash

ffmpeg -i ./pe0102.mp3 -f rtp_mpegts rtp://bsmouse.wr:5000/
#ffmpeg -i ./pe0102.mp3  -acodec copy -f rtp_mpegts rtp://192.168.10.12:5000/

# ffplay -x 720 rtp://192.168.10.12:5000/
