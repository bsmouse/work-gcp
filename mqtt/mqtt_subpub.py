#!/usr/bin/python3
from datetime import datetime
import paho.mqtt.client as mqtt
from time import sleep
import sys

pub_count = 0


def read_time():
    global pub_count
    global client
    pub_count += 1

    # str_time = datetime.today().strftime("%Y/%m/%d %H:%M:%S")
    str_time = datetime.today().strftime("%H:%M:%S")
    client.publish("sensors/time/{:03d}".format(pub_count), str_time)

    print("Sent({:03d}) : {}".format(pub_count, str_time))
    sleep(30)


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))


def on_disconnect(client, userdata, flags, rc=0):
    print("Disconnected with result code "+str(rc))


def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))


def on_message(client, userdata, msg):
    data = dict(
        topic=msg.topic,
        payload=msg.payload.decode()
    )
    print("Received : ", data)


# 새로운 클라이언트 생성
client = mqtt.Client("sensor_sub")

client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_subscribe = on_subscribe
client.on_message = on_message
client.username_pw_set(username="blueapm", password="1234qwer")

# client.connect('dev20.vm', 1883)
client.connect('dev20.gcp', 1883)
client.loop_start()

# common topic 으로 메세지 발행
# # => multi level wildcard
# + => single level wildcard.
client.subscribe('sensors/#', 1)

# client.loop_forever()

try:
    while True:
        client.loop(1, 1)
        read_time()


except KeyboardInterrupt:
    client.loop_stop()
    client.disconnect()
    sys.exit(0)
