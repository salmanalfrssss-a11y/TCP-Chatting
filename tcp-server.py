import socket

HOST='0.0.0.0'
PORT=8000

def start_echo_server():
    server_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"Echo server aktif di {HOST}:{PORT}, menunggu koneksi...")

    conn, addr = server_socket.accept()
    print(f"Terhubung dengan client {addr}")

    with conn:
        while True:
            data = conn.recv(1024)
            if not data: #Jika tidak ada data lagi, artinya client memutus
                break
            print(f"Menerima: {data.decode('utf-8')}-> Mengirim balik...")
            conn.sendall(data) #Mengirim balik (echo) data yang sama
    print("Koneksi dengan client selesai.")
    server_socket.close()

if __name__ == "__main__":
    start_echo_server()