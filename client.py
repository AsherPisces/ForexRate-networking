import socket

SERVER_HOST = "192.168.1.119"
SERVER_PORT = 5050

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((SERVER_HOST,SERVER_PORT))

data = input("input data: ")

client.sendall(data.encode("utf-8"))