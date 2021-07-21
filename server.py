import socket
import threading
from logger import is_logged, regis
PORT = 5455
HOST = "127.0.0.1"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server.bind((HOST, PORT))
server.listen()

print("Waiting for client: ")
conn, addr = server.accept()
conn.sendall("accepted".encode("utf-8"))
print(f"connected by {addr}")

while True:
    client_select = conn.recv(1024).decode("utf-8")
    username_client = conn.recv(1024).decode("utf-8")
    password_client = conn.recv(1024).decode("utf-8")
    is_success = False
    if client_select == "login":
        # login
        if is_logged(username_client, password_client):
            print(f"{addr} logged!")
            conn.sendall("login_success".encode("utf-8"))
            is_success = True
        else:
            conn.sendall("login_fail".encode("utf-8"))
    if client_select == "regis":
        # regis
        regis(username_client, password_client)
        conn.sendall("regis_success".encode("utf-8"))
    if is_success == True:
        break

while True:
    data_client = conn.recv(1024).decode("utf-8")
    print(f"Client: {data_client}")
    if data_client == "quit":
        conn.close()
        server.close()
        break
    data_server = input("Server: ") 
    conn.sendall(data_server.encode("utf-8"))
    if data_server == "quit":
        conn.close()
        break



