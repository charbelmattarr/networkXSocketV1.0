# node1.py
import time

import zmq
import threading
from Node import Node


node1 = Node(5558)
node2 = Node(5556)

# start listening for incoming messages on both nodes
node1.start_listening()
node2.start_listening()

# send a message from node1 to node2
node1.send_message("Hello from node 1!")

# send a message from node2 to node1
node2.send_message("Hello from node 2!")

# wait for a few seconds for messages to be received
time.sleep(2)

# print received messages for each node
print(f"Node 1 received: {node1.received_messages}")
print(f"Node 2 received: {node2.received_messages}")

# stop listening for incoming messages on node2
node2.stop_listening()
