# 1 client
import socket
PORT = 5656
HOST = "192.168.1.77"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))
server.listen()
print("Waiting for client: ")
conn, addr = server.accept()
print("connect by {}".format(addr))
print("Hello {}!".format(addr))
while True:
    data_client = conn.recv(1024).decode("utf-8")
    print("Client: {}".format(data_client))
    if data_client == "quit":
        conn.close()
        server.close()
        break
    data_server = input("Server: ") 
    conn.sendall(data_server.encode("utf-8"))
    if data_server == "quit":
        conn.close()


