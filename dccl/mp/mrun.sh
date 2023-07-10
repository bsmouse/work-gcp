#! /bin/bash

# 20-11-23 : service 로 등록함.
# UDP 전송이 필요한 경우 => /etc/mavlink-router에서 main.conf파일 수정 필요
mavlink-routerd -c main.conf &>> ~/log/mavlink-routerd.log 

# 2개 이상 라우팅이 필요한 경우
#mavlink-routerd -c main0.conf &>> ~/log/mavlink-routerd0.log 
#mavlink-routerd -c main1.conf &>> ~/log/mavlink-routerd1.log 

# UDP 전송이 필요한 경우 => mavlink-router로 해결되어서 필요없어짐
#mavproxy.py --daemon --master=tcp:localhost:5760 --out=udp:bsmouse.wr:14550 &>> ./log/mavproxy.log &


