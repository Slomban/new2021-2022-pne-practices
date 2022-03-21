import socket
SERVER_PORT = 8080
SERVER_IP = "localhost"

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((SERVER_IP, SERVER_PORT))

server_socket.listen()

print("The server is configured!")
print("Waiting for clients to connect.")

server_socket.accept()
print("A client has connected to the server!")

server_socket.close()