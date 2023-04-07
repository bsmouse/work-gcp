#! /bin/bash
gst-launch-1.0 -v rtmpsrc location=rtmp://localhost/stream/bsmousekey ! flvdemux ! h264parse ! rtph264pay pt=96 config-interval=5 ! udpsink host=seoamo.wr port=5600

## Mission Planner
# udpsrc port=5600 buffer-size=90000 ! application/x-rtp ! rtph264depay ! avdec_h264 ! queue leaky=2 ! videoconvert ! video/x-raw,format=BGRA ! appsink name=outsink sync=false
