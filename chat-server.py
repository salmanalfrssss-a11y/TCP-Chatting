import socket
import threading

HOST = "0.0.0.0"
PORT = 7001

def receive(conn):
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                print("Koneksi terputus.")
                break

            print(f"\nTeman : {data.decode('utf-8')}")
            print("Anda : ", end="")

        except:
            print("Koneksi terputus.")
            break

def send(conn):
    while True:
        pesan = input("Anda : ")

        if pesan.lower() == "/exit":
            conn.close()
            break

        conn.sendall(pesan.encode("utf-8"))

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("Menunggu koneksi...")

conn, addr = server.accept()

print(f"Terkoneksi dengan {addr}")

threading.Thread(target=receive, args=(conn,), daemon=True).start()

send(conn)