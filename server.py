from socket import socket, AF_INET, SOCK_STREAM
import json
from threading import Thread
from logger import is_logged, regis
PORT = 5453
HOST = "127.0.0.1"

server = socket(AF_INET, SOCK_STREAM)


server.bind((HOST, PORT))


server.listen()

print("Waiting for client: ")
conn, addr = server.accept()
conn.sendall("accepted".encode("utf-8"))
print(f"connected by {addr}")

user = {}

while True:
    client_select = conn.recv(1024).decode("utf-8")
    user_json = conn.recv(1024).decode("utf-8")
    user = json.loads(user_json)
    is_success = False
    if client_select == "login":
        # login
        if is_logged(user):
            print(f"{addr} logged!")
            conn.sendall("login_success".encode("utf-8"))
            is_success = True
        else:
            conn.sendall("login_fail".encode("utf-8"))
    if client_select == "regis":
        # regis
        regis(user)
        conn.sendall("regis_success".encode("utf-8"))
    if is_success == True:
        break

while True:
    data_client = conn.recv(1024).decode("utf-8")
    print("{} {}: {}".format(user["first_name"], user["last_name"], data_client))
    if data_client == "quit":
        conn.close()
        server.close()
        break
    data_server = input("Server: ") 
    conn.sendall(data_server.encode("utf-8"))
    if data_server == "quit":
        conn.close()
        break



