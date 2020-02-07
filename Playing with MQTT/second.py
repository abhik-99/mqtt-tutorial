#demonstrats publish
import paho.mqtt.client as mqtt
import time

broker = "test.mosquitto.org"

def on_connect(client, userdata, flags, rc):
    if rc==0:
        print("Connected Successfully!")
    else:
        print("Error!",rc)

def on_disconnect(client, userdata, flags, rc = 0):
    print("Disconnect! Result Code",rc)

def on_log(client, userdata, level, buf):
    print("log",buf)

client = mqtt.Client("Python1")
client.on_connect = on_connect
client.on_log = on_log
client.on_disconnect = on_disconnect

print("Connecting to Broker",broker)

client.connect(broker)
client.loop_start()  #helps to view the output of the callbacks
"""
There is no actual structure to the topic. There can be any design of the topic
like one similar to REST APIs or any custom structure. 
"""
#publishing a "payload" 'hello world' to the topic "first/test" 
client.publish("first/test","hello world!")
time.sleep(4)

client.loop_stop()
client.disconnect()