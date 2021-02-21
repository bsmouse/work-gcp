#!/usr/bin/python3
import datetime
import json
import os
import ssl
import time

import jwt
import paho.mqtt.client as mqtt

# projects/feisty-proton-286721/topics/auth

# GCP parameters
project_id = 'feisty-proton-286721'  # Your project ID.
registry_id = 'reg_mqtt_auth'  # Your registry name.
device_id = 'dev20vm'  # Your device name.
# Path to private key.
private_key_file = '/home/blueapm/work/mqtt/rsa_private.pem'
algorithm = 'RS256'  # Authentication key format.
cloud_region = 'asia-east1'  # Project region.
ca_certs = '/home/blueapm/work/mqtt/roots.pem'  # CA root certificate path.
mqtt_bridge_hostname = 'mqtt.googleapis.com'  # GC bridge hostname.
mqtt_bridge_port = 8883  # Bridge port.
message_type = 'event'  # Message type (event or state).


def create_jwt(project_id, private_key_file, algorithm):
    # Create a JWT (https://jwt.io) to establish an MQTT connection.
    token = {
        'iat': datetime.datetime.utcnow(),
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
        'aud': project_id
    }
    with open(private_key_file, 'r') as f:
        private_key = f.read()
    print('Creating JWT using {} from private key file {}'.format(
        algorithm, private_key_file))
    return jwt.encode(token, private_key, algorithm=algorithm)


def error_str(rc):
    # Convert a Paho error to a human readable string.
    return '{}: {}'.format(rc, mqtt.error_string(rc))


class Device(object):
    # Device implementation.

    def on_connect(self, unused_client, unused_userdata, unused_flags, rc):
        # Callback on connection.
        print('Connection Result:', error_str(rc))

    def on_disconnect(self, unused_client, unused_userdata, rc):
        # Callback on disconnect.
        print('Disconnected:', error_str(rc))

    def on_publish(self, unused_client, unused_userdata, unused_mid):
        # Callback on PUBACK from the MQTT bridge.
        print('Published message acked.')

    def on_subscribe(self, unused_client, unused_userdata, unused_mid,
                     granted_qos):
        # Callback on SUBACK from the MQTT bridge.
        print('Subscribed: ', granted_qos)
        if granted_qos[0] == 128:
            print('Subscription failed.')

    def on_message(self, unused_client, unused_userdata, message):
        # Callback on a subscription.
        payload = message.payload.decode('utf-8')
        print('Received message \'{}\' on topic \'{}\' with Qos {}'.format(
            payload, message.topic, str(message.qos)))

        # if not payload:
        #     return
        # # Parse incoming JSON.
        # data = json.loads(payload)
        # print(data['num_message'])


def main():

    client = mqtt.Client(
        client_id='projects/{}/locations/{}/registries/{}/devices/{}'.format(
            project_id,
            cloud_region,
            registry_id,
            device_id))
    client.username_pw_set(
        username='unused',
        password=create_jwt(
            project_id,
            private_key_file,
            algorithm))
    client.tls_set(ca_certs=ca_certs, tls_version=ssl.PROTOCOL_TLSv1_2)

    device = Device()

    # client.on_connect = device.on_connect
    client.on_publish = device.on_publish
    # client.on_disconnect = device.on_disconnect
    client.on_subscribe = device.on_subscribe
    client.on_message = device.on_message
    client.connect(mqtt_bridge_hostname, mqtt_bridge_port)
    client.loop_start()

    mqtt_telemetry_topic = '/devices/{}/events'.format(device_id)
    mqtt_config_topic = '/devices/{}/config'.format(device_id)

    client.subscribe(mqtt_config_topic, qos=1)

    num_message = 1000
    try:
        while True:
            # If button was pressed - send message.
            currentTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            num_message += 1
            # Form payload in JSON format.
            data = {
                'num_message': num_message,
                # 'led1': device.led1,
                # 'led2': device.led2,
                'message': "Hello",
                'time': currentTime
            }
            payload = json.dumps(data, indent=4)
            print('Publishing payload', payload)
            client.publish(mqtt_telemetry_topic, payload, qos=1)
            # Make sure that message was sent once on press.
            time.sleep(30)

    except KeyboardInterrupt:
        # Exit script on ^C.
        pass
        client.disconnect()
        client.loop_stop()
        print('Exit with ^C. Goodbye!')


if __name__ == '__main__':
    main()
