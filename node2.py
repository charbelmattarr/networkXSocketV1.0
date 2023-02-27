# node2.py
import socket




IP_ADDRESS = 'localhost'
PORT = 1232
PORT2 = 1235
def send_data(message, ip_address, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip_address, port))
    s.sendall(message.encode())
    s.close()


def receive_data(ip_address, port):
    s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s1.bind((ip_address, port))
    s1.listen(1)
    conn, addr = s1.accept()
    data = conn.recv(1024)
    print(f"Received data: {data.decode()}")
    conn.close()




# receive data from node 1
receive_data(IP_ADDRESS, PORT)
print("after recieved")
# send data to node 3
message = "Hello from node 2"
send_data(message, 'localhost', PORT2)