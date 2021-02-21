#!/usr/bin/python3
from datetime import datetime
import paho.mqtt.client as mqtt
from time import sleep

pub_count = 0


def read_time():
    global pub_count
    pub_count += 1

    # str_time = datetime.today().strftime("%Y/%m/%d %H:%M:%S")
    str_time = "{:3d} {}".format(
        pub_count, datetime.today().strftime("%Y/%m/%d %H:%M:%S"))

    client = mqtt.Client("sensor_pub")
    client.connect("dev20.gcp", 1883, 60)
    client.publish("sensors/time", str_time)
    client.disconnect()

    print("Send({:3d}) : {}".format(pub_count, str_time))

    sleep(10)


# client = mqtt.Client("sensor_pub")
# client.connect("dev20.gcp", 1883, 60)
# #client.connect("seoamo.wr", 1883, 60)

try:
    while True:
        read_time()

except KeyboardInterrupt:
    sys.exit(0)
