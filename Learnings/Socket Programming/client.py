import socket as skt


MSG_LENGTH = 64
DISCONNECT_MESSAGE = "!DISCONNECTED"
PORT = 8000
SERVER_IP = '127.0.0.1'
MSG_FORMAT = 'utf-8'

server_addr = (SERVER_IP, PORT)
client_skt = skt.socket(skt.AF_INET, skt.SOCK_STREAM)
client_skt.connect(server_addr)

def send_message(socket, msg):

    encoded_msg = msg.encode(MSG_FORMAT)
    msg_length = len(encoded_msg)
    send_length = str(msg_length).encode(MSG_FORMAT)
    padded_send_length = send_length + b' ' * (MSG_LENGTH - len(send_length))
    
    socket.send(padded_send_length)
    socket.send(encoded_msg )

    print(socket.recv(2048).decode(MSG_FORMAT))

send_message(client_skt, "Hello World!")
send_message(client_skt, DISCONNECT_MESSAGE)
client_skt.close()
