import socket
import json
from threading import Thread
from os import system, name
from tkinter import *
from tkinter import messagebox
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

window.geometry("1150x720")
window.title("Forex Rate")



user = {}


def Accept_login(user):
    client.sendall(json.dumps(user).encode("utf-8"))
    if client.recv(1024).decode("utf-8") == "login_success":
        return True
    else:
        return False

def Accept_signup(user):
    client.sendall(json.dumps(user).encode("utf-8"))
    if client.recv(1024).decode("utf-8") == "sign_up_success":
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
    else:
        messagebox.showerror('Forex Rate', 'Your Account Not Approved Yed!')

def Handle_signup(user, user_entry, pass_entry):
    client.sendall("sign_up".encode("utf-8"))
    user["name"] = user_entry.get()
    user["password"] = pass_entry.get()
    if Accept_signup(user):
        messagebox.showinfo('Forex Rate', 'Sign Up Successful!')
    else:
        messagebox.showwarning('Forex Rate', 'Account Already Exists!')

def Start():
    print("Start")
    # perform the work
    # print("1. Task A: ")#tra cuu theo ngay
    # print("2. Task B: ")
    # print("3. Task C: ")
    # print("4. Task D: ")
    # print("5. Task E: ")
    # print("Quit to Exit!")
    # ...more reqest
    user["msg"] = "GET"
    client.sendall(json.dumps(user).encode("utf-8"))
    while True:
        data_server_json = client.recv(40000).decode("utf-8")
        data_server = json.loads(data_server_json)
        print(data_server)
        if data_server == "quit":
            break
        break

background_image= PhotoImage(file = "br2.png")
background_label = Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

frame_logo = Frame(window, bg = "white", bd = 5)
frame_logo.place(x = 75, y = 125, height = 250, width = 350)

logo = Label(frame_logo, text = "FOREX RATE", font =("Impact", 75, "bold"), fg = "#D2691E")
logo.place(x = 10, y = 20)

frame_login = Frame(window, bg = "white", bd = 5)
frame_login.place(x = 75, y = 275, height = 250, width = 350)

title_login = Label(frame_login, text = "Log In", font =("Impact", 45), fg = "#488AC7")
title_login.place(x = 10, y = 0)
user_label = Label(frame_login, text = "Username :")
user_label.place(x = 10, y = 70)
user_entry = Entry(frame_login, width = 20)
user_entry.place(x = 10, y = 90)
pass_label = Label(frame_login, text = "Password :")
pass_label.place(x = 10, y = 120)
pass_entry = Entry(frame_login,width = 20, show="*")
pass_entry.place(x = 10, y = 140)
login_button = Button(frame_login,
    text="Log In",
    padx = 5, pady = 5,
    relief=RAISED,\
        cursor="fleur",
    command = lambda: (
    Handle_login(user, user_entry, pass_entry)
    )
)
login_button.place(x = 10, y = 180)
signup_button = Button(frame_login,
    text="Sign Up",
    padx = 5, pady = 5,
    relief=RAISED,\
        cursor="fleur",
    command = lambda: (
    Handle_signup(user, user_entry, pass_entry)
    )
)
signup_button.place(x = 70, y = 180)

window.mainloop()

client.close()



