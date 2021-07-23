import socket
import json
from threading import Thread
from os import system, name
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
SERVER_HOST = input("Input IP: ")
SERVER_PORT = int(input("Input Port: "))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((SERVER_HOST,SERVER_PORT))

welcome = client.recv(1024).decode("utf-8")
print(welcome)

user = {}

while True:
    is_success = False
    print("1. Login: ")
    print("2. Regis: ")
    check = input("Select: ")
    if check == "1":#select login
        # login
        while True:
            # clear() # clear screen
            client.sendall("login".encode("utf-8"))
            user["name"] = input("Username: ")
            user["password"] = input("Password: ")
            client.sendall(json.dumps(user).encode("utf-8"))
            if client.recv(1024).decode("utf-8") == "login_success":
                print("logged success!")
                is_success = True
                break
            else:
                print("fail success!")
    elif check == "2":#select registered
        # regis
        while True:
            # clear()
            client.sendall("sign_up".encode("utf-8"))
            user["name"] = input("Username: ")
            user["password"] = input("Password: ")
            client.sendall(json.dumps(user).encode("utf-8"))
            if client.recv(1024).decode("utf-8") == "sign_up_success":
                print("signed up success!")
                break
            else:
                print("fail success!")
    if is_success == True:
        break
# perform the work
print("1. Task A: ")
print("2. Task B: ")
print("3. Task C: ")
print("4. Task D: ")
print("5. Task E: ")
print("Quit to Exit!")
# ...more reqest
while True:
    user["msg"] = input("> ")
    if user["msg"] == "1":
        # do something
        client.sendall(json.dumps(user).encode("utf-8"))
    if user["msg"] == "2":
        # do something
        client.sendall(json.dumps(user).encode("utf-8"))
    if user["msg"] == "3":
        # do something
        client.sendall(json.dumps(user).encode("utf-8"))
    if user["msg"] == "4":
        # do something
        client.sendall(json.dumps(user).encode("utf-8"))
    if user["msg"] == "5":
        # do something
        client.sendall(json.dumps(user).encode("utf-8"))
    data_server = client.recv(1024).decode("utf-8")
    print(data_server)
    # if data_server == "quit":
    #     client.close()
    #     break



