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

#prints the data recieved in the "msg"
"""
Once you subscribe to a topic, you get any message published using that topic
This message is what you can access using the "msg" argument.
"msg" has 4 attributes, 2 of the important ones are:
msg.topic - contains the topic whose message you recieved.
msg.payload - contains the actual message that was published to the topic
"""
def on_message(client, userdata, msg):
    topic = msg.topic
    mess = msg.payload.decode("utf-8")
    print("msg contents:\nQOS:",msg.qos)
    print("retain:", msg.retain)
    print("Topic:",topic,"Message",mess)
    print(type(msg))
    

client = mqtt.Client("MyClient")
client.on_connect = on_connect
#turning off logging
#client.on_log = on_log
client.on_disconnect = on_disconnect
client.on_message = on_message

print("Connecting to Broker",broker)

client.connect(broker)
client.loop_start()
"""
We subscribe to the topic using our client. This is because once a message is 
sent by the publisher, it is not stored usually by the broker (retain fields
can help in storing the message temporarily).
If there are not subscriber to the topic, it is discarded. So, we subscribe to the
topic first to make sure that we receive the topic message
"""
#subscribing to the topic
client.subscribe("first/test")
#puclishing to the topic using our client
client.publish("first/test","hello world!")
# client.subscribe("first/test")
time.sleep(4)

client.loop_stop()
client.disconnect()