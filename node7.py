import zmq

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5565")

while True:
    message = input("Enter message to send: ")
    socket.send_string(message)
