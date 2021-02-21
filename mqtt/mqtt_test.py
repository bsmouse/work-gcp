#!/usr/bin/python3
import datetime
import os
import subprocess

# First go to the "/var/www/html" directory
# os.chdir("C:/Users/admin/Desktop/HSEC/darknet-master/darknet-master/build/darknet/x64")

# Print current working directory
# print("Current working dir : %s" % os.getcwd())


def subprocess_open(command):
    popen = subprocess.Popen(
        command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    (stdoutdata, stderrdata) = popen.communicate()
    return stdoutdata, stderrdata


strdate = datetime.datetime.now().strftime("%b %e")
# print(strdate)
command = "cat /var/log/auth.log | grep \"{}\" | wc -l".format(strdate)
print(command)
stdoutdata, stderrdata = subprocess_open(command)
strout = stdoutdata.decode('utf-8').replace("\n", "", 1)
print(strdate, ":", strout)

# projects/feisty-proton-286721/topics/mqtt-test/
# projects/feisty-proton-286721/subscriptions/vm-auth
