import socket as skt
import threading as th

MSG_LENGTH = 64 
DISCONNECT_MESSAGE = "!DISCONNECTED"
PORT = 8000
MSG_FORMAT = 'utf-8'
# SERVER_IP = skt.gethostbyname(skt.gethostname())
SERVER_IP = '127.0.0.1'

server_skt = skt.socket(skt.AF_INET, skt.SOCK_STREAM)
server_addr = (SERVER_IP, PORT)
server_skt.bind(server_addr)

# Handle each client via this function separately
def handle_client(client_skt, client_addr):
    print(f"[NEW CONNECTION] {client_addr} connected.")

    connected = True
    while connected:

        # Receive the length of the message as a string
        msg_length = client_skt.recv(MSG_LENGTH).decode(MSG_FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            # Receive the actual message
            msg = client_skt.recv(msg_length).decode(MSG_FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(f"[{client_addr}] {msg}")
            client_skt.send("Message received!".encode(MSG_FORMAT))
   
    print(f"[DISCONNECTED] {client_addr} connection closed.")
    client_skt.close()

def start_server():

    # Listen for clients
    server_skt.listen()
    print(f"[LISTENING] Server is listening on {SERVER_IP}.")
    while True:
        client_skt, client_addr = server_skt.accept()
        client_thread = th.Thread(target=handle_client, args=(client_skt, client_addr))
        client_thread.start()
        print(f"[ACTIVE CONNECTIONS] {th.active_count()-1}")

print(f"[SERVER STARTING] server is starting...")
start_server()