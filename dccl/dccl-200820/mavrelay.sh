#! /bin/bash
stty  -F /dev/ttyACM0 57600  raw -echo -echoe -echok -iexten -echoctl -echoke  
# optional: provides RTCM injection if ublox m8p is connected to usb
# socat UDP-DATAGRAM:127.0.0.1:13320 file:/dev/ttyACM0

/usr/local/bin/mavproxy.py --out 192.168.0.2:14550
#~pi/venv/mavrelay/bin/mavproxy.py --master=/dev/ttyUSB0 --out=udpbcast:192.168.1.255:14550 --source-system=197
