import socket
import threading

clients = []
start = 0

def handle_client(client_socket, addr):
    print(f"[+] {addr} connected.")
    while True:
        try:
            msg = client_socket.recv(1024).decode()
            print(msg)
            data = list(msg.split(','))
            if data[0] == "len":
                answer("len"+","+str(len(clients)), client_socket)
            elif data[0] == "move":
                broadcast(f"{msg}", client_socket)
            elif data[0] == "play":
                start += 1
            elif data[0] == "cancel":
                start -= 1
            elif not msg:
                break
            print(f"[{addr}] {msg}")
            broadcast(f"{msg}", client_socket)
        except:
            break
        if start == 2:
            broadcast(f"{"start"}", None)

    print(f"[-] {addr} disconnected.")
    clients.remove(client_socket)
    client_socket.close()

def broadcast(msg, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(msg.encode())
            except:
                pass

def answer(msg, sender_socket):
        try:
            msg = str(msg)
            sender_socket.send(msg.encode())
        except Exception as e:
            print("Error:", e)
            pass

def main():
    host = '0.0.0.0'
    port = 20001

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)

    print(f"[+] Server listening on {host}:{port}")

    while True:
        client_socket, addr = server.accept()
        clients.append(client_socket)
        thread = threading.Thread(target=handle_client, args=(client_socket, addr))
        thread.start()

if __name__ == "__main__":
    main()