import socket
import threading

HOST = "10.25.18.23"
PORT = 7001

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))


def receive():

    while True:
        try:
            data = client.recv(1024)

            if not data:
                break

            print(data.decode())

        except:
            break


threading.Thread(
    target=receive,
    daemon=True
).start()


while True:

    pesan = input()

    client.send(pesan.encode())

    if pesan == "/exit":
        break

client.close()