import socket

HOST = '127.0.0.1'
PORT = 8000

def start_echo_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    pesan = "Halo, ini pesan echo!"
    print(f"Mengirim ke server: {pesan}")
    client_socket.sendall(pesan.encode('utf-8'))

    #Menunggu kembalian dari server
    data = client_socket.recv(1024)
    print(f"Echo dari server: {data.decode('utf-8')}")

    client_socket.close()

if __name__ == "__main__":
    start_echo_client()
