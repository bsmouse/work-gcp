#!/bin/bash
gst-launch-1.0 -v rtmpsrc location=rtmp://localhost/stream/dcclkey ! flvdemux ! h264parse ! rtph264pay pt=96 config-interval=5 ! udpsink host=ubuntu.pi port=5600
