#demonstrats publish and subscribe
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

def on_message(client, userdata, msg):
    topic = msg.topic
    mess = msg.payload.decode("utf-8")
    print("msg contents:\nQOS:",msg.qos)
    print("retain:", msg.retain)
    print("Topic:",topic,"Message",mess)
    print(type(msg))
    

client = mqtt.Client("Python1")
client.on_connect = on_connect
#turning off logging
#client.on_log = on_log
client.on_disconnect = on_disconnect
client.on_message = on_message

print("Connecting to Broker",broker)

client.connect(broker)
client.loop_start()
client.subscribe("first/test")
client.publish("first/test","hello world!")
# client.subscribe("first/test")
time.sleep(4)

client.loop_stop()
client.disconnect()