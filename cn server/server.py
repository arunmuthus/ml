import socket
import threading
TCP_HOST = '127.0.0.1'
TCP_PORT = 5000
UDP_HOST = '127.0.0.1'
UDP_PORT = 5001
clients = []
tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_server.bind((TCP_HOST, TCP_PORT))
tcp_server.listen()
udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_server.bind((UDP_HOST, UDP_PORT))
def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"[TCP] Received: {message}")
            broadcast(message, client_socket)
        except:
            if client_socket in clients:
                clients.remove(client_socket)
            client_socket.close()
            break
def broadcast(message, client_socket=None):
    for client in clients:
        if client != client_socket:
            try:
                client.send(message.encode('utf-8'))
            except:
                if client in clients:
                    clients.remove(client)
                client.close()
def handle_udp_messages():
    while True:
        try:
            message, addr = udp_server.recvfrom(1024)
            print(f"[UDP] {addr}: {message.decode('utf-8')}")
            for client in clients:
                try:
                    udp_server.sendto(message, client.getpeername())
                except ConnectionResetError:
                    print("[UDP Server] Failed to send to a client.")
        except ConnectionResetError:
            print("[UDP Server] Connection reset by client. Continuing to listen for new messages.")
        except Exception as e:
            print(f"[UDP Server] An error occurred: {e}")
            break
def start_tcp_server():
    print(f"[TCP Server] Running on {TCP_HOST}:{TCP_PORT}")
    while True:
        client_socket, addr = tcp_server.accept()
        print(f"[TCP] {addr} connected.")
        clients.append(client_socket)
        thread = threading.Thread(target=handle_client, args=(client_socket,))
        thread.start()
def start_udp_server():
    print(f"[UDP Server] Running on {UDP_HOST}:{UDP_PORT}")
    thread = threading.Thread(target=handle_udp_messages)
    thread.start()
tcp_thread = threading.Thread(target=start_tcp_server)
udp_thread = threading.Thread(target=start_udp_server)
tcp_thread.start()
udp_thread.start()
