import paho.mqtt.client as mqtt
import time

#we connect to this broker
broker = "test.mosquitto.org"

#these are callback functions which are invoked 
#when a specific event happens
def on_connect(client, userdata, flags, rc):
    if rc==0:
        print("Connected Successfully!")
    else:
        print("Error!",rc)
def on_log(client, userdata, level, buf):
    print("log",buf)

#creating a MQTT Client. 
#Note: Client name must be unique
client = mqtt.Client("Python1")

#mapping the user-defined callback functions
client.on_connect = on_connect
client.on_log = on_log

print("Connecting to Broker",broker)

client.connect(broker)
#client.loop_start()

time.sleep(4)

#client.loop_stop()
client.disconnect()