import networkx as nx
import matplotlib.pyplot as plt
import threading
from Node import Node


# Define the nodes and edges of the network
nodes = [ 1,2,3, 4, 5,6,7,8]
edges = [(1,4),(1,3),(2,4),(2,3),(3,5),(3,6),(4,7),(4,8)]

# Create the graph object
G = nx.Graph()

# Add nodes to the graph
G.add_nodes_from(nodes)

# Add edges to the graph
G.add_edges_from(edges)

#pos = nx.spring_layout(G)
pos = {1: (0, 0), 2: (2, 0), 3: (0, -2), 4: (2, -2), 5: (-3, -5), 6: (1, -5), 7: (3, -5), 8: (7, -5)}

labeldict = {}
labeldict[1] = "12345"
labeldict[2] = "12348"
labeldict[3] = "12347"
labeldict[4] = "12346"
labeldict[5] = "12349"
labeldict[6] = "12350"
labeldict[7] = "12351"
labeldict[8] = "12352"



# Draw the graph
nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_labels(G,pos,labels=labeldict)
#nx.draw(G, pos,with_labels=True)
print("Graph Analysis")
print("Eulerin :" +str(nx.is_eulerian(G)))
betweenness_centrality = str(nx.betweenness_centrality(G))
print("Bridges? :"+betweenness_centrality)
print("Average shortest Path" + str(nx.closeness_centrality(G)))
print("Clustering Coefficient : " + str(nx.clustering(G)))

# Show the graph
plt.show()

node1 = Node("127.0.0.1",12345,[12347,12346])
node2 = Node("127.0.0.1",12348,[12347,12346])
node3 = Node("127.0.0.1",12347,[12345,12348,12349,12350])
node4 = Node("127.0.0.1",12346,[12345,12348,12351,12352])
node5 = Node("127.0.0.1",12349,[12347])
node6 = Node("127.0.0.1",12350,[12347])
node7 = Node("127.0.0.1",12351,[12346])
node8 = Node("127.0.0.1",12352,[12346])


# Start a separate thread to read incoming messages
t = threading.Thread(target=node1.zmqRead, args=())
t.daemon = True
t.start()

t1 = threading.Thread(target=node2.zmqRead, args=())
t1.daemon = True
t1.start()

t2 = threading.Thread(target=node3.zmqRead, args=())
t2.daemon = True
t2.start()

t3 = threading.Thread(target=node4.zmqRead, args=())
t3.daemon = True
t3.start()

t4 = threading.Thread(target=node5.zmqRead, args=())
t4.daemon = True
t4.start()

t5 = threading.Thread(target=node6.zmqRead, args=())
t5.daemon = True
t5.start()

t6 = threading.Thread(target=node7.zmqRead, args=())
t6.daemon = True
t6.start()

t8 = threading.Thread(target=node8.zmqRead, args=())
t8.daemon = True
t8.start()

#t2 = threading.Thread(target=node3.zmqWrite, args=("Bonjour",12346))
#t2.daemon = True
#t2.start()
node3.zmqWrite("Bonjour",12345,node3.ports)
