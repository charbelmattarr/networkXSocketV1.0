import zmq
import threading

def read_data(socket):
    while True:
        message = socket.recv()
        print(message)
        # process the received message here

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:5565")
socket.subscribe(b"")

# start the background thread to read data
thread = threading.Thread(target=read_data, args=(socket,))
thread.daemon = True
thread.start()


print("do anything")


while True:
    message = socket.recv()
    if message is not None:
        print(f"Received message: {message}")
    else:
        print("No message received")
