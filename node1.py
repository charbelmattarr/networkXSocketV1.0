# node1.py
import socket


IP_ADDRESS = 'localhost'
PORT = 1232
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

# send data to node 2
message = "Hello from node 1"
send_data(message, IP_ADDRESS, PORT)

# receive data from node 3
receive_data(IP_ADDRESS, PORT2)