import socket
import threading
import sys
TCP_HOST = '127.0.0.1'
TCP_PORT = 5000
UDP_HOST = '127.0.0.1'
UDP_PORT = 5001
tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_client.connect((TCP_HOST, TCP_PORT))
udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
def receive_tcp():
    while True:
        try:
            message = tcp_client.recv(1024).decode('utf-8')
            if message:
                print(f"[TCP] {message}")
            else:
                print("[TCP] Server closed the connection.")
                tcp_client.close()
                break
        except:
            print("[TCP] Connection closed.")
            tcp_client.close()
            break
def send_tcp_message(message):
    try:
        tcp_client.send(message.encode('utf-8'))
    except BrokenPipeError:
        print("[TCP] Cannot send message, connection lost.")
def send_udp_message(message):
    try:
        udp_client.sendto(message.encode('utf-8'), (UDP_HOST, UDP_PORT))
    except Exception as e:
        print(f"[UDP] Failed to send message: {e}")
def start_receiving_tcp():
    thread = threading.Thread(target=receive_tcp)
    thread.start()
start_receiving_tcp()
print("Connected to the chat. Type your messages below.")
print("Commands:\n/msg <text> for TCP\n/udp <text> for UDP\n/exit to leave")
while True:
    try:
        message = input()
        if message.lower() == "/exit":
            print("Exiting chat...")
            tcp_client.close()
            udp_client.close()
            break
        elif message.startswith("/msg "):
            send_tcp_message(message[5:])  
        elif message.startswith("/udp "):
            send_udp_message(message[5:])  
        else:
            print("Unknown command. Use /msg <text> for TCP or /udp <text> for UDP.")
    except KeyboardInterrupt:
        print("\nExiting chat...")
        tcp_client.close()
        udp_client.close()
        sys.exit()
