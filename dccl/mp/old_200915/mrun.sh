#! /bin/bash

#stty  -F /dev/ttyS1 57600 raw -echo -echoe -echok -iexten -echoctl -echoke
#stty  -F /dev/ttyACM0 57600 raw -echo -echoe -echok -iexten -echoctl -echoke

mavproxy.py --master=tcp:localhost:5760 --out=udp:bsmouse.wr:14550 
# mavproxy.py --master=udp:10.178.0.3:14550 --out=udp:seoamo.wr:14550 
# mavproxy.py --master=udp:10.178.0.3:14550 --out=udp:bsmouse.wr:14550 --out=udp:seoamo.wr:14550

