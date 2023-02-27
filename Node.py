import zmq
import threading


class Node:
    def __init__(self, port, neighbors=None):
        self.port = port
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.PUB)
        self.socket.bind(f"tcp://*:{self.port}")
        self.sub_socket = self.context.socket(zmq.SUB)
        self.sub_socket.connect(f"tcp://localhost:{self.port}")
        self.sub_socket.subscribe(b"")
        self.received_messages = []
        self.listening_thread = None
        self.listening = False

        self.neighbors = neighbors or []

    def start_listening(self):
        if self.listening:
            return
        self.listening = True
        self.listening_thread = threading.Thread(target=self.receive_messages)
        self.listening_thread.start()

    def stop_listening(self):
        self.listening = False
        self.listening_thread.join()

    def receive_messages(self):
        while self.listening:
            try:
                message = self.sub_socket.recv_string(flags=zmq.NOBLOCK)
                self.received_messages.append(message)
                print(f"Received message on port {self.port}: {message}")
            except zmq.ZMQError:
                pass

    def send_message(self, message):
        self.socket.send_string(message)
        # broadcast the message to neighbors
        for neighbor in self.neighbors:
            neighbor.send_message(message)
