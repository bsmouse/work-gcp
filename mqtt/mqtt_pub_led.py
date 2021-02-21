#!/usr/bin/python3
from datetime import datetime
import paho.mqtt.client as mqtt
from time import sleep
import curses


def read_time():
    str_time = datetime.today().strftime("%Y/%m/%d %H:%M:%S")
    client.publish("sensors/test/time", str_time)
    sleep(2)


def send_data(data):
    client.publish("sensors/test", data)


client = mqtt.Client("sensor_pub")
client.connect("192.168.0.56", 1883, 60)


# Get the curses window, turn off echoing of keyboard to screen, turn on
# instant (no waiting) key response, and use special values for cursor keys
screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

try:
    while True:
        char = screen.getch()
        if char == ord('a'):
            send_data("on")
        elif char == ord('s'):
            send_data("off")
        elif char == ord('d'):
            send_data("allwayson")
        elif char == ord('f'):
            send_data("allwaysoff")


except KeyboardInterrupt:
    sys.exit(0)

finally:
    # Close down curses properly, inc turn echo back on!
    curses.nocbreak()
    screen.keypad(0)
    curses.echo()
    curses.endwin()
