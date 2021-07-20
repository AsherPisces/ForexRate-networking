import socket
# Hello anh =)))

SERVER_HOST = "192.168.1.77"
SERVER_PORT = 5656


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((SERVER_HOST,SERVER_PORT))
while True:
    data_client = input("Client: ")
    client.sendall(data_client.encode("utf-8"))
    if data_client == "quit":
        client.close()
        break
    data_server = client.recv(1024).decode("utf-8")
    print(f"Server: {data_server}")
    if data_server == "quit":
        client.close()
        break


