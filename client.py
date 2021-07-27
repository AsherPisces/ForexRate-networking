import socket
import json
from threading import Thread
from os import system, name
from tkinter import *
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

window = Tk()

window.geometry("500x400")
window.title("VietNam Coin App")
user = {}


def Accept_login(user):
    client.sendall(json.dumps(user).encode("utf-8"))
    if client.recv(1024).decode("utf-8") == "login_success":
        return True
    else:
        return False
        
def Handle_login(user, user_entry, pass_entry):
    client.sendall("login".encode("utf-8"))
    user["name"] = user_entry.get()
    user["password"] = pass_entry.get()
    print(user["name"])
    print(user["password"])
    if Accept_login(user):
        Start()
        print("Login successful")
    else:
        label_login = Label(window, text="Login failed!")
        label_login.grid(row =5, column =1)
        print("Login failed")

def Accept_signup(user):
    client.sendall(json.dumps(user).encode("utf-8"))
    if client.recv(1024).decode("utf-8") == "sign_up_success":
        return True
    else:
        return False

def Handle_signup(user, user_entry, pass_entry):
    client.sendall("sign_up".encode("utf-8"))
    user["name"] = user_entry.get()
    user["password"] = pass_entry.get()
    if Accept_signup(user):
        label_signup = Label(window, text="Sign Up successful!")
        label_signup.grid(row=5, column = 1)
        print("Sign Up successful")
    else:
        label_login = Label(window, text="Sign Up failed!")
        label_login.grid(row =5, column =1)
        print("Sign Up failed")

def Start():
    print("Start")
    # is_success = False
    # print("1. Login: ")
    # print("2. Regis: ")

user_label = Label(window, text = "Username :")
user_label.grid(row = 1, column = 1)
user_entry = Entry(window, width = 20)
user_entry.grid(row = 1, column = 2)
pass_label = Label(window, text = "Password :")
pass_label.grid(row = 2, column = 1)
pass_entry = Entry(window,width = 20)
pass_entry.grid(row = 2, column = 2)
login_button = Button(window,
    text="Log In",
    command = lambda: (
    Handle_login(user, user_entry, pass_entry)
    )
)
login_button.grid(row = 3, column = 1)
signup_button = Button(window,
    text="Sign Up",
    command = lambda: (
    Handle_signup(user, user_entry, pass_entry)
    )
)
signup_button.grid(row = 4, column = 1)



# perform the work
# print("1. Task A: ")#tra cuu theo ngay
# print("2. Task B: ")
# print("3. Task C: ")
# print("4. Task D: ")
# print("5. Task E: ")
# print("Quit to Exit!")
# # ...more reqest
# while True:
#     user["msg"] = input("> ")
#     if user["msg"] == "1":
#         # do something
#         client.sendall(json.dumps(user).encode("utf-8"))
#     if user["msg"] == "2":
#         # do something
#         client.sendall(json.dumps(user).encode("utf-8"))
#     if user["msg"] == "3":
#         # do something
#         client.sendall(json.dumps(user).encode("utf-8"))
#     if user["msg"] == "4":
#         # do something
#         client.sendall(json.dumps(user).encode("utf-8"))
#     if user["msg"] == "5":
#         # do something
#         client.sendall(json.dumps(user).encode("utf-8"))
#     if user["msg"] == "quit":
#         client.sendall(json.dumps(user).encode("utf-8"))
#     data_server = client.recv(1024).decode("utf-8")
#     print(data_server)
#     if data_server == "quit":
#         break

window.mainloop()

client.close()



