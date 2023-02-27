# node3.py
import socket

IP_ADDRESS = 'localhost'
PORT = 1235
PORT2 = 1239
def send_data(message, ip_address, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip_address, port))
    s.sendall(message.encode())
    s.close()


def receive_data(ip_address, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((ip_address, port))
    s.listen(1)
    conn, addr = s.accept()
    data = conn.recv(1024)
    print(f"Received data: {data.decode()}")
    conn.close()

# receive data from node 2
receive_data(IP_ADDRESS, PORT)

# send data to node 1
message = "Hello from node 3"
send_data(message, 'localhost', PORT2)
