import socket
import threading

F='\033[m'
B='\033[1m'

WHITE='\033[38;2;255;255;255m'
PINK='\033[38;2;255;0;255m'
YELLOW='\033[38;2;255;255;0m'
AZUL1='\033[38;2;0;255;255m'
RED='\033[38;2;255;0;0m'
GREEN='\033[38;2;0;255;0m'
AZUL2='\033[38;2;0;0;255m'

RED_T='\033[48;2;255;0;0m'

target_host = "0.0.0.0"
target_port = 9998


def S():
    print("")

def logo(): #CrypR
# In non HEX Format 
    print(f"  {GREEN}   _____                                    ______ _____ ___ {F}")
    print(f"  {GREEN}  / ___/___  ________  _____  _____        /_  __// ___//__ \{F}")
    print(f"  {GREEN}  \__ \/ _ \/ ___/| | / / _ \/ ___/ _____   / /  / /   / /_//{F}")
    print(f"  {GREEN} ___/ /  __/ /    | |/ /  __/ /    |_____| / /  / /__ / ___/ {F}")
    print(f"  {GREEN}/____/\___/_/     |___/\___/_/            /_/   \____/_/      {F}")
    print(f" {GREEN}<===================={B}{RED_T} Created by Ascoid {F}{GREEN}=====================> {F}")
    print()

def main():
    print("[ Servidor - TCP ]")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((target_host,target_port))
    server.listen(5)
    print(f"[*] Ouvindo em {target_host}:{target_port}")

    while True:
        client, address = server.accept()
        print(f"[*] Conexão aceita de {address[0]}:{address[1]}")
        client_handler = threading.thread(target=client_handler, args=(client,))
        client_handler.start()

def handle_client(client_socket):
    with client_socket as sock:
        request = sock.recv(1024)
        print(f'[*] Recebido: {request.decode("utf-8")}')
        sock.send(b"ACK")

if __name__ == "__main__":
    #Clear()
    logo()
    main()
    

