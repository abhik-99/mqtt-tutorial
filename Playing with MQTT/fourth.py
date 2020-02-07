#Handling Multiple Topic Subscriptions
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

Subscribing to a topic using client.subscribe(<topic_name>,<quality_of_service>)
<quality_of_service> -
Quality of Service determines the number of times a specific message is received.
The values QOS can take are -
0 - (at most once) The message is sent at most once and not stored by the sender.
This is the fastest but least secure method.
1 - (at least once) The message is sent repeatedly till a confirmation/acknowledgement
is recieved.
2 - (exactly once) This is the most secure method where the sender waits for an
acknowledgement from the receiver. 
"""
#default qos =0
#client.subscribe("first/test")

#subscribing to multiple topics
#l = [("first/test1",0),("first/test2",0)]
#client.subscribe(l)

"""
Above logic is used when the topics are different from the root. However,
if there is a topic (eg. "home") with 3 subtopics (eg. "light","fan","ac")
such that the topics are - home/light , home/fan, home/ac, then one can 
subscribe directly to all of them by subscribing using "home/#"
"""
client.subscribe("first/#")


#publishing to the topic using our client
client.publish("first/test1","hello world!")
# client.subscribe("first/test")
time.sleep(4)
client.publish("first/test2","New World Now!")
time.sleep(4)

client.loop_stop()
client.disconnect()