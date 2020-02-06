import paho.mqtt.client as mqtt
import time

broker = "test.mosquitto.org"

def on_connect(client, userdata, flags, rc):
    if rc==0:
        print("Connected Successfully!")
    else:
        print("Error!",rc)
def on_log(client, userdata, level, buf):
    print("log",buf)

client = mqtt.Client("Python1")
client.on_connect = on_connect
client.on_log = on_log

print("Connecting to Broker",broker)

client.connect(broker)
client.loop_start()

time.sleep(4)

client.loop_stop()
client.disconnect()