#!/usr/bin/python3
"""
A small Test application to show how to use Flask-MQTT.
test 002
"""

from datetime import datetime
from flask_bootstrap import Bootstrap
from flask_socketio import SocketIO
from flask_mqtt import Mqtt
from flask import Flask, render_template, request, Response
import json
import eventlet

eventlet.monkey_patch()

app = Flask(__name__)
app.config['SECRET'] = 'my secret key'
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['MQTT_BROKER_URL'] = 'dev20.gcp'
app.config['MQTT_BROKER_PORT'] = 1883
app.config['MQTT_CLIENT_ID'] = 'flask_mqtt'
app.config['MQTT_USERNAME'] = ''
app.config['MQTT_PASSWORD'] = ''
app.config['MQTT_KEEPALIVE'] = 5
app.config['MQTT_TLS_ENABLED'] = False
app.config['MQTT_CLEAN_SESSION'] = True

# Parameters for SSL enabled
# app.config['MQTT_BROKER_PORT'] = 8883
# app.config['MQTT_TLS_ENABLED'] = True
# app.config['MQTT_TLS_INSECURE'] = True
# app.config['MQTT_TLS_CA_CERTS'] = 'ca.crt'

mqtt = Mqtt(app, connect_async=True)
socketio = SocketIO(app)
bootstrap = Bootstrap(app)

gdata = dict(topic='sensors/time/null', payload='null')
adata = dict(topic='sensors/auth/null', payload='null')


@app.route('/')
def index():
    mqtt.publish('sensors/time/hello', 'hello world')
    return render_template('index.html')


@app.route('/pub', methods=['POST', 'GET'])
def pub():
    data = []

    str_time = datetime.today().strftime("%Y/%m/%d %H:%M:%S")

    if request.method == 'GET':
        data = dict(
            topic=request.args['topic'],
            message=request.args['message']
        )
    else:
        data = request.get_json(force=True)

    # print(data)
    mqtt.publish(data['topic'], data['message']+' '+str_time)
    return render_template('index.html', **data)


@app.route('/sub', methods=['POST', 'GET'])
def sub():
    global gdata
    global adata

    gdata["time"] = datetime.today().strftime("%Y/%m/%d %H:%M:%S")
    gdata['authcount'] = '{} : {}'.format(adata['topic'], adata['payload'])

    return render_template('index.html', **gdata)


@socketio.on('publish')
def handle_publish(json_str):
    data = json.loads(json_str)
    mqtt.publish(data['topic'], data['message'])


@socketio.on('subscribe')
def handle_subscribe(json_str):
    data = json.loads(json_str)
    mqtt.subscribe(data['topic'], 1)


@socketio.on('unsubscribe_all')
def handle_unsubscribe_all():
    mqtt.unsubscribe_all()


@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    mqtt.subscribe('sensors/#', 1)
    print("Connected with result code "+str(rc))


@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    global gdata
    global adata
    global booldata
    data = dict(
        topic=message.topic,
        payload=message.payload.decode()
    )
    socketio.emit('mqtt_message', data=data)
    print('Message', data)
    if (data['topic'][8:12] == 'auth'):
        adata = data
    else:
        gdata = data


@ mqtt.on_log()
def handle_logging(client, userdata, level, buf):
    # print(level, buf)
    pass


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000,
                 use_reloader=False, debug=False)
