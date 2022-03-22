from Client0 import Client

SERVER_IP = "localhost"
SERVER_PORT = 8081
MESSAGES = 5

client = Client(SERVER_IP, SERVER_PORT)
for i in range(MESSAGES):
    c.debug_talk(f"Message {i}")