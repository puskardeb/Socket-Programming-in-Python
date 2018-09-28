import threading 
import socket

HOST = '127.0.0.1'
PORT = 12345
BUFFER_SIZE = 1024
ADDR = (HOST, PORT)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(ADDR)
server_socket.listen(100)

list_of_clients = []

print("waiting on connection :")
def handler(client_socket, addr):  
    while True:
        try:
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break
            data = str(addr) + " says : " + data 
            for client in list_of_clients:
                if client != client_socket:
                    client.sendall(data.encode('utf-8'))
        except:
            list_of_clients.remove(client_socket)
            data = str(addr) + "has disconnected from the chat room"
            for client in list_of_clients:
                client.sendall(data.encode('utf-8'))
            print(str(addr) + "has disconnected")
            break
        
while True:
    try:
        client_socket, addr = server_socket.accept()
        t = threading.Thread(target=handler, args=(client_socket, addr))
        t.start()
        data = str(addr) + "has joined the chat room"
        for client in list_of_clients:
            client.sendall(data.encode('utf-8'))
        list_of_clients.append(client_socket)
        print("Connected from ", addr)
    except:
        break