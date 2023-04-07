#!/bin/bash

ffmpeg -i "rtmp://seoamo.wr/stream/dccl_cam" -r 5 /tmp/mjpg/output%03d.jpg

