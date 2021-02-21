#!/usr/bin/python3
from flask import Flask, request, Response
from datetime import datetime
import paho.mqtt.client as mqtt
from time import sleep

app = Flask(__name__)
onmessage = 1
message = []


@app.route('/auth_flask', methods=['POST', 'GET'])
def auth_flask():
    id = 'blueapm'
    psk = 'a_secret_password'

    output = []
    now = datetime.now()
    output = 'Hello World.... Current Time is : {0}<br><br>'.format(now)

    if request.method == 'GET':
        userID = request.args['id']
        userPasswd = request.args['psk']
    else:
        data = request.get_json(force=True)
        userID = data['id']
        userPasswd = data['psk']

    if id == userID and psk == userPasswd:
        output += '로그인 성공!<br>id : {0}<br>pw : {1}<br>'.format(
            userID, userPasswd)
        return Response(output, status=200)
    else:
        output += '로그인 실패!<br>id : {0}<br>pw : {1}<br>'.format(
            userID, userPasswd)
        return Response(output, status=401)


@app.route('/mqtt_time', methods=['POST', 'GET'])
def mqtt_time():

    output = []
    str_time = datetime.today().strftime("%Y/%m/%d %H:%M:%S")
    output = 'Hello World.... Todsy is : {0}<br><br>'.format(str_time)

    client = mqtt.Client("sensor_pub")
    client.connect("dev20.gcp", 1883, 60)
    client.publish("sensors/mqtt_time", str_time)
    client.disconnect()

    return Response(output, status=200)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
