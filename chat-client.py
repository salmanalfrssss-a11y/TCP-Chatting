import socket
import threading

HOST = "10.25.18.23"
PORT = 7001

def receive(client):
    while True:
        try:
            data = client.recv(1024)
            if not data:
                break

            print(f"\nTeman : {data.decode('utf-8')}")
            print("", end="")

        except:
            break

def send(client):
    while True:
        pesan = input("Anda : ")

        if pesan.lower() == "/exit":
            client.close()
            break

        client.sendall(pesan.encode("utf-8"))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

threading.Thread(target=receive, args=(client,), daemon=True).start()

send(client)