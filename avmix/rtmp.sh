#!/bin/bash

## 직접전송
#ffmpeg -i ./china.mp4 -i ./pe0102.mp3 -f flv rtmp://localhost/stream/bsmouse
ffmpeg -i ./china.mp4 -i rtmp://localhost/stream/audio -f flv rtmp://localhost/stream/bsmouse

# ffplay -x 720 rtmp://dev20.gcp/stream/bsmouse

