#!/bin/bash

~/mp/grun.sh &
screen -L -dmS mavbarn ~/mp/mrun.sh &

# https://www.geeksforgeeks.org/screen-command-in-linux-with-examples/
# -dmS name: It start as daemon: Screen session in detached mode.
# -L: It turn on output logging.
