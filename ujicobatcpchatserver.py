import socket
import threading

HOST = "0.0.0.0"
PORT = 7001

clients = {}
lock = threading.Lock()


# ==============================
# Broadcast ke semua client
# ==============================
def broadcast(message, sender=None):
    with lock:
        for client in list(clients.keys()):
            if client != sender:
                try:
                    client.send(message.encode("utf-8"))
                except:
                    client.close()
                    del clients[client]


# ==============================
# Chat dari SERVER
# ==============================
def server_chat():
    while True:
        pesan = input("SERVER : ")

        if pesan.lower() == "/exit":
            print("Server berhenti mengirim pesan.")
            break

        print(f"SERVER : {pesan}")
        broadcast(f"\nSERVER : {pesan}\n")


# ==============================
# Menangani Client
# ==============================
def handle_client(conn, addr):

    try:
        conn.send("Masukkan username: ".encode("utf-8"))
        username = conn.recv(1024).decode("utf-8").strip()

        with lock:
            clients[conn] = username

        print(f"{username} terhubung dari {addr}")

        broadcast(f"\n[SERVER] {username} bergabung ke chat.\n")

        while True:

            data = conn.recv(1024)

            if not data:
                break

            pesan = data.decode("utf-8").strip()

            if pesan == "/exit":
                break

            elif pesan == "/list":
                daftar = ", ".join(clients.values())
                conn.send(f"User Online: {daftar}\n".encode("utf-8"))

            else:
                print(f"{username}: {pesan}")
                broadcast(f"{username}: {pesan}", conn)

    except:
        pass

    finally:
        with lock:
            if conn in clients:
                nama = clients[conn]
                del clients[conn]

                print(f"{nama} keluar.")
                broadcast(f"\n[SERVER] {nama} meninggalkan chat.\n")

        conn.close()


# ==============================
# Membuat Socket Server
# ==============================
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print(f"Server berjalan di {HOST}:{PORT}")

# Thread agar server bisa mengirim chat
threading.Thread(
    target=server_chat,
    daemon=True
).start()


# Menunggu client
while True:

    conn, addr = server.accept()

    threading.Thread(
        target=handle_client,
        args=(conn, addr),
        daemon=True
    ).start()