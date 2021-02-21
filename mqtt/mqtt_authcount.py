#!/usr/bin/python3
import os
import subprocess
from datetime import datetime
import paho.mqtt.client as mqtt
from time import sleep
# import sys

# test 005
# First go to the "/var/www/html" directory
# os.chdir("C:/Users/admin/Desktop/HSEC/darknet-master/darknet-master/build/darknet/x64")
# Print current working directory
# print("Current working dir : %s" % os.getcwd())


def subprocess_open(command):
    popen = subprocess.Popen(
        command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    (stdoutdata, stderrdata) = popen.communicate()
    return stdoutdata, stderrdata


def read_authcount():
    strdate = datetime.now().strftime("%b %e")
    # print(strdate)
    command = "cat /var/log/auth.log | grep \"{}\" | wc -l".format(strdate)
    # print(command)
    stdoutdata, stderrdata = subprocess_open(command)
    strout = "{} : {}".format(strdate, stdoutdata.decode(
        "utf-8").replace("\n", "", 1))
    # print(strdate, ":", strout)

    client.publish("sensors/auth/dev20.gcp", strout)

    sleep(1)


client = mqtt.Client("sensor_pub")
# client.connect("dev20.vm", 1883, 60)
client.connect("dev20.gcp", 1883, 60)
#client.connect("seoamo.wr", 1883, 60)
read_authcount()

client.disconnect()


# try:
#     while True:
#         read_time()

# except KeyboardInterrupt:
#     client.disconnect()
#     sys.exit(0)
