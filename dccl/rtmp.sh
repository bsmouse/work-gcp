#!/bin/bash

raspivid -o - -t 0 -w 1280 -h 720 -fps 25 -b 1000000 | ffmpeg -i - -vcodec copy -an -f flv rtmp://localhost/stream/dcclkey

#raspivid -o - -t 0 -w 1280 -h 720 -fps 25 -b 1000000 | ffmpeg -i - -vcodec copy -an -f flv rtmp://utuntu.pi/record/dcclkey?psk=a_secret_password

