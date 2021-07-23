import socket
import json
from threading import Thread
from logger import is_logged, is_sign_up
PORT = 5454
HOST = "127.0.0.1"
# ThreadCount = 0 

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))

def handle_client(conn, addr):
    # log
    while True:
        client_select = conn.recv(1024).decode("utf-8")
        user_json = conn.recv(1024).decode("utf-8")
        user = json.loads(user_json)
        is_success = False
        if client_select == "login":
            # login
            if is_logged(user):
                print("{} logged!".format(user["name"]))
                conn.sendall("login_success".encode("utf-8"))
                is_success = True
            else:
                conn.sendall("login_fail".encode("utf-8"))
        elif client_select == "sign_up":
            # regis
            if is_sign_up(user):
                print("{} signed up!".format(user["name"]))
                conn.sendall("sign_up_success".encode("utf-8"))
            else:
                conn.sendall("sign_up_fail".encode("utf-8"))
        if is_success == True:
            break
    clients[user["name"]] = conn
    # run
    while True:
        data_client_json = clients[user["name"]].recv(1024).decode("utf-8")
        data_client = json.loads(data_client_json)
        print("{}: {}".format(data_client["name"], data_client["msg"]))
        if data_client["msg"] == "quit":
            clients[user["name"]].close()
            break
        # response

        if data_client["msg"] == "1":
            print("{}: reqest task A".format(data_client["name"]))
            # do something
            clients[user["name"]].sendall("task A. Done!".encode("utf-8"))
        if data_client["msg"] == "2":
            print("{}: reqest task B".format(data_client["name"]))
            # do something
            clients[user["name"]].sendall("task B. Done!".encode("utf-8"))
        if data_client["msg"] == "3":
            print("{}: reqest task C".format(data_client["name"]))
            # do something
            clients[user["name"]].sendall("task C. Done!".encode("utf-8"))
        if data_client["msg"] == "4":
            print("{}: reqest task D".format(data_client["name"]))
            # do something
            clients[user["name"]].sendall("task D. Done!".encode("utf-8"))
        if data_client["msg"] == "5":
            print("{}: reqest task E".format(data_client["name"]))
            # do something
            clients[user["name"]].sendall("task E. Done!".encode("utf-8"))
        # data_server = input("Server: z") 
        # clients[user["name"]].sendall("Accept".encode("utf-8"))
        # if data_server == "quit":
        #     conn.close()
        #     break
def accept_connection():
    while True:
        conn, addr = server.accept()
        print(f"connected by {addr}")
        # clients.append(conn)
        # start_new_thread(handle_client, (conn,addr))
        # ThreadCount += 1
        conn.sendall(f"Server: Welcome {addr}".encode("utf-8"))
        Thread(target=handle_client, args=(conn, addr)).start()

if __name__ == "__main__":
    # ...the same as hash table
    clients = {}
    server.listen(5)
    print("Waiting for client...")
    ACCEPT_THREAD = Thread(target=accept_connection)
    
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    server.close()