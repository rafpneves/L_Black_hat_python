import socket

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

target_host = "www.google.com"
target_port = 80

target_host2 = "127.0.0.1"
target_port2 = 9997

# [clear] Limpa historico anterior
def Clear():
    print("")

def logo(): #CrypR
# In non HEX Format 
    print(f"  {GREEN}  ________________           __  ______  ____  {F}")
    print(f"  {GREEN} /_  __/ ____/ __ \         / / / / __ \/ __ \ {F}")
    print(f"  {GREEN}  / / / /   / /_/ / _____  / / / / / / / /_/ / {F}")
    print(f"  {GREEN} / / / /___/ ____/ /____/ / /_/ / /_/ / ____/  {F}")
    print(f"  {GREEN}/_/  \____/_/             \____/_____/_/       {F}")
    print(f" {GREEN}<============{B}{RED_T} Created by Ascoid {F}{GREEN}=============> {F}")
    print()

def TCP():
    print("[ TCP ]")
    Clear()
    # criar um objeto socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connectar o cliente
    client.connect((target_host,target_port))

    # enviar alguns dados
    client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

    # receber alguns dados
    respose = client.recv(4096)

    print(respose.decode())
    client.close()


def UDP():
    Clear()
    print("[ UDP ]")
    Clear()
    # criar um objeto socket
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # enviar alguns dados
    client.bind((target_host2, target_port2))
    client.sendto(b"AAABBBCCC",(target_host2,target_port2))

    # receber alguns dados
    data, addr = client.recvfrom(4096)

    print(data.decode())
    client.close()

if __name__ == "__main__":
    Clear()
    logo()
    TCP()
    UDP()
