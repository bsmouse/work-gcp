#!/usr/bin/python3
from datetime import datetime
import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("connected OK")
    else:
        print("Bad connection Returned code=", rc)


def on_disconnect(client, userdata, flags, rc=0):
    print(str(rc))


def on_subscribe(client, userdata, mid, granted_qos):
    print("subscribed: " + str(mid) + " " + str(granted_qos))


def create_figure(header):
    print("create figure with ", header)


def on_message(client, userdata, msg):
    print("Receive topic:" + msg.topic + " payload:" + msg.payload.decode())


# 새로운 클라이언트 생성
client = mqtt.Client()

client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_subscribe = on_subscribe
client.on_message = on_message

client.connect('dev20.gcp', 1883)

# common topic 으로 메세지 발행
# # => multi level wildcard
# + => single level wildcard.
client.subscribe('sensors/#', 1)

client.loop_forever()
