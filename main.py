# node1.py
import time

import zmq
import threading
from Node import Node
# create three nodes on ports 5555, 5556, and 5557, with appropriate neighbors

node1 = Node(5558, None)
node2 = Node(5559, None)
node3 = Node(5560, None)


node1.neighbors=[node2, node3]
node2.neighbors=[node1, node3]
node3.neighbors=[node1, node2]
# start listening for incoming messages on all nodes
node1.start_listening()
node2.start_listening()
node3.start_listening()

# send a message from node1 to all neighbors
node1.send_message("Hello from node 1!")

# stop listening for incoming messages on node2
node2.stop_listening()
