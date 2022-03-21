import socket
import termcolor
import os #operative system
from Sequence import Seq

IP = "localhost"
PORT = 8080
GENES = ["ADA", "FRAT1", "FXN", "RNUG_269P", "U5"]

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

try:
    server_socket.bind((IP, PORT))
    server_socket.listen()

    print("SEQ Server onfigured!")

    while True:
        print(f"Waiting for clients...")
        (client_socket, client_address ) = server_socket.accept()

        request_bytes = client_socket.recv(2048)
        request = request_bytes.decode("utf-8")

        slices = request.split(" ")
        command = slices[0]
        if command == "PING":
            termcolor.cprint("PING command!", 'green')
            response = f"OK!\n"
            print(response)
            response_bytes = str.encode(response)
            client_socket.send(response_bytes)
        elif command == "GET":
            genes_number = int(slices[1])
            gene = GENES[genes_number]
            seq = Seq()
            #file_name = "../P0/MyFiles/{GENE}.txt""
            file_name = os.path.join("..", "Genes", f"{gene}.txt")
            seq.read_fasta(file_name)



        client_socket.close()

except socket.error:
    print(f"Problems using port {PORT}. Do you permission?")
except KeyboardInterrupt:
    print("Server stopped by the admin.")
    server_socket.close()