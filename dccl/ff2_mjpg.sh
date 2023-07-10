#!/bin/bash

/usr/local/bin/mjpg_streamer -i 'input_file.so -f /tmp/mjpg -r -d 0' -o 'output_http.so -w /usr/local/share/mjpg-streamer/www'

