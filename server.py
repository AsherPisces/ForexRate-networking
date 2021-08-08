import socket
import json
from threading import Thread
from logger import is_logged, is_sign_up
from tkinter import *
import time
from requests import get
from xml.dom import minidom

def Download(url, file_name):
    with open(file_name, "wb") as file:
        # get request
        response = get(url)
        # write to file
        file.write(response.content)

def Download_connection():
    global setData
    while True:
         # save Data here
        setData = []
        Download("https://portal.vietcombank.com.vn/Usercontrols/TVPortal.TyGia/pXML.aspx", "data_vietcombank.xml")
        my_tree = minidom.parse('data_vietcombank.xml')
        tag_name = my_tree.getElementsByTagName('Exrate')
        header_table_data = ["Currency Code", "Currency Name", "Cash", "Transfer", "Selling Rates"]
        setData.append(header_table_data)
        date = my_tree.getElementsByTagName('DateTime')[0]
        day = date.childNodes[0]
        data_current = []
        for x in tag_name:
            data_current.append(x.attributes['CurrencyCode'].value)
            data_current.append(x.attributes['CurrencyName'].value)
            data_current.append(x.attributes['Buy'].value)
            data_current.append(x.attributes['Transfer'].value)
            data_current.append(x.attributes['Sell'].value)
            setData.append(data_current)
            data_current = []

        setData.append(day.nodeValue)
        # 
        status.insert(END, "Update {}".format(setData[len(setData)-1]))
        time.sleep(5)

PORT = 5455
HOST = "0.0.0.0"
# ThreadCount = 0 

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
# ==================GUI-SERVER-MAIN=============
window = Tk()
window.geometry("350x400")
window.title("Forex Rate")
icon = PhotoImage(file='logo_server.png')
window.iconphoto(True, icon)
# ====logo=====
frame_logo_root = Frame(window, bg = "white", bd = 5)
frame_logo_root.place(x = 0, y = 0, height = 150, width = 250)
logo_root = Label(frame_logo_root, text = "FOREX RATE", font =("Impact", 30, "bold"), fg = "#D2691E")
logo_root.place(x = 15, y = 10)
# ====scroll-bar====
scroll_bar = Scrollbar(window)
scroll_bar.pack(side = RIGHT, fill = Y )
# ====status-main===
status = Listbox(window, width = 32, height = 15, yscrollcommand = scroll_bar.set)
status.place(x = 25, y = 70)
status.insert(END, "Waiting for client...")
# ====scroll-bar-command====
scroll_bar.config(command = status.yview)

def Accept_connection():
    while True:
        conn, addr = server.accept()
        # print(f"connected by {addr}")
        status.insert(END,f"connected by {addr}")
        conn.sendall(f"Server: Welcome {addr}".encode("utf-8"))
        Thread(target=Handle_client, args=(conn, addr)).start()

def Handle_client(conn, addr):
    # log
    while True:
        while True:
            client_select = conn.recv(1024).decode("utf-8")
            user_json = conn.recv(1024).decode("utf-8")
            user = json.loads(user_json)
            is_success = False
            if client_select == "login":
                # login
                if is_logged(user):
                    # print("{} logged in!".format(user["name"]))
                    status.insert(END,"{} logged in!".format(user["name"]))
                    conn.sendall("login_success".encode("utf-8"))
                    is_success = True
                else:
                    conn.sendall("login_fail".encode("utf-8"))
            elif client_select == "sign_up":
                # regis
                if is_sign_up(user):
                    # print("{} signed up!".format(user["name"]))
                    status.insert(END,"{} signed up!".format(user["name"]))
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
            if data_client["msg"] == "quit":
                status.insert(END, "{} logged out!".format(data_client["name"]))
                break
            # response
            if data_client["msg"] == "GET": 
                # print("{} request {}".format(data_client["name"], data_client["msg"]))
                status.insert(END, "{} request {}".format(data_client["name"], data_client["msg"]))
                # do something
                # sendall setData
                clients[user["name"]].sendall(json.dumps(setData).encode("utf-8"))
            # if data_server == "quit":
            #     conn.close()


def on_closing():
    window.destroy()
    server.close()
    # exit()


if __name__ == "__main__":
    # ...the same as hash table
    clients = {}
    server.listen(6)
    ACCEPT_THREAD = Thread(target=Accept_connection)
    DOWNLOAD_THREAD = Thread(target=Download_connection)
    ACCEPT_THREAD.start()
    DOWNLOAD_THREAD.start()
    window.protocol("WM_DELETE_WINDOW", on_closing)
    window.mainloop()
    ACCEPT_THREAD.join()