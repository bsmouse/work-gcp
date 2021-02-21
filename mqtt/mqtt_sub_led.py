#!/usr/bin/python3
from datetime import datetime
import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time


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


first_msg = 0
im = 0


def on_message(client, userdata, msg):
    print("[" + datetime.today().strftime("%Y/%m/%d %H:%M:%S") +
          "] topic : " + msg.topic)
    print("payload : " + str(msg.payload))
    if msg.payload == b"on":
        print("on-----------------\n")
        for x in range(0, 10):
            GPIO.setup(led, GPIO.OUT)
            GPIO.output(led, on)
            time.sleep(1)
            GPIO.output(led, off)
            time.sleep(1)
    elif msg.payload == b"off":
        print("off-----------------\n")
        for x in range(0, 3):
            GPIO.setup(led, GPIO.OUT)
            GPIO.output(led, on)
            time.sleep(1)
            GPIO.output(led, off)
            time.sleep(1)
    elif msg.payload == b"allwayson":
        print("allwayson-----------------\n")
        GPIO.setup(led, GPIO.OUT)
        GPIO.output(led, on)
    elif msg.payload == b"allwaysoff":
        print("allwaysoff-----------------\n")
        GPIO.setup(led, GPIO.OUT)
        GPIO.output(led, off)


GPIO.setmode(GPIO.BOARD)
led = 12
on = True
off = False


# 새로운 클라이언트 생성
client = mqtt.Client()
# 콜백 함수 설정 on_connect(브로커에 접속), on_disconnect(브로커에 접속종료), on_subscribe(topic 구독), on_message(발행된 메세지가 들어왔을 때)
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_subscribe = on_subscribe
client.on_message = on_message

client.connect('192.168.0.56', 1883)
client.subscribe('sensors/test/#', 1)
client.loop_forever()

finally:
    GPIO.clear()
