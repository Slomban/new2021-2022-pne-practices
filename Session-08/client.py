import socket

SERVER_IP = "localhost"
SERVER_PORT = 8081

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, SERVER_PORT))

client_socket.send(str.encode("Hello from the client!"))
msg_bytes = client_socket.recv(2048)
msg = msg_bytes.decode("utf-8")
print(f"Message from server: {msg}")

client_socket.close()