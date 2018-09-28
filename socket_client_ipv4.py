import socket
import threading

HOST = '127.0.0.1'
PORT = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def send_message():
    while True:
        try:
            tmp = input("...")
            s.send(tmp.encode('utf-8'))
        except:
            break

s.connect((HOST, PORT))
t = threading.Thread(target=send_message)
t.start()
while True:
    data = s.recv(1024)
    if not data:
        break
    data = data.decode('utf-8')
    print(data)
