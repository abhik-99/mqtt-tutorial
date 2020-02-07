#Understanding the Asynchronous nature of Callbacks

import paho.mqtt.client as mqtt
import time

broker = "test.mosquitto.org"
client_name = "MyClient"
mqtt.Client.connected_flag = False
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected To Broker Succesfully!")
    else:
        print("Connection Error!",rc)
    client.connected_flag = True

def on_log(client, userdata, levels, buf):
    print("log:",buf)


client = mqtt.Client(client_name)

client.on_connect = on_connect
client.on_log = on_log

count = 0

client.connect(broker)
client.loop_start()
time.sleep(0.5)

while client.connected_flag == False:
    print("Connecting...",count)
    time.sleep(0.1)
    count += 1

client.disconnect()
client.loop_stop()