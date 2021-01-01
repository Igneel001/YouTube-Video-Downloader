import socket
import threading

host = '127.0.0.1'
port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(clients)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            nicknames.remove(nickname)
            broadcast("{} left the chat".format(nickname).encode('ascii'))
            break

def receive():
    while True:
        client, address = server.accept()
        print("{} connected with the server",format(str(address)))
        client.send("NICK".encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(clients)
        print("Nickname is {}".format(nickname))
        broadcast("{} joined the chat".format(nickname))
        client.send("Conneted to the server".encode('ascii'))

        thread = threading.Thread(target=handle, args=(client))
        thread.start()
print("server is running\n")
receive()