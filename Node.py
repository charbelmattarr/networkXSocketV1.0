import zmq
import threading
class Node:
    def __init__(self, port):
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.SUB)
        self.socket.connect(f"tcp://localhost:{port}")
        self.socket.subscribe(b"")
        self.port = port
        self.received_messages = []

        self.send_socket = self.context.socket(zmq.PUB)
        self.send_socket.bind(f"tcp://*:{port + 1}")

        self.is_running = False

    def start_listening(self):
        if not self.is_running:
            self.is_running = True
            self.listen_thread = threading.Thread(target=self._listen, daemon=True)
            self.listen_thread.start()

    def stop_listening(self):
        self.is_running = False

    def read_data(self):
        while True:
            message = self.socket.recv()
            self.received_messages.append(message)

    def _listen(self):
        while self.is_running:
            try:
                message = self.socket.recv_string()
                print(f"Received message: {message}")
            except zmq.error.ZMQError:
                pass



    def send_message(self, message):
        self.send_socket.send_string(message)

