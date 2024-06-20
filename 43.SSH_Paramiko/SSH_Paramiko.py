import os
import SSH_rcmd

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

def clear():
    os.system('clear')

def logo(): #CrypR
# In non HEX Format 
    print()
    print(f"  {B}{GREEN} ███████                                         ██ ██                  ████████  ████████ ██      ██{F}")
    print(f"  {B}{GREEN}░██░░░░██                                       ░░ ░██                 ██░░░░░░  ██░░░░░░ ░██     ░██{F}")
    print(f"  {B}{GREEN}░██   ░██  ██████   ██████  ██████     █████████ ██░██  ██  ██████    ░██       ░██       ░██     ░██{F}")
    print(f"  {B}{GREEN}░███████  ░░░░░░██ ░░██░░█ ░░░░░░██ ░░██░░██░░██░██░██ ██  ██░░░░██   ░█████████░█████████░██████████{F}")
    print(f"  {B}{GREEN}░██░░░░    ███████  ░██ ░   ███████  ░██ ░██ ░██░██░████  ░██   ░██   ░░░░░░░░██░░░░░░░░██░██░░░░░░██{F}")
    print(f"  {B}{GREEN}░██       ██░░░░██  ░██    ██░░░░██  ░██ ░██ ░██░██░██░██ ░██   ░██ ██       ░██       ░██░██     ░██{F}")
    print(f"  {B}{GREEN}░██      ░░████████░███   ░░████████ ███ ░██ ░██░██░██░░██░░██████ ░██ ████████  ████████ ░██     ░██{F}")
    print(f"  {B}{GREEN}░░        ░░░░░░░░ ░░░     ░░░░░░░░ ░░░  ░░  ░░ ░░ ░░  ░░  ░░░░░░  ░░ ░░░░░░░░  ░░░░░░░░  ░░      ░░ {F}")
    print()
    print(f" {GREEN}<========================================={B}{RED_T} Created by Ascoid {F}{GREEN}=========================================> {F}")
    print()

def info():
    print(f"           {B}{RED}                               [{B}{WHITE}?{B}{RED}]{B}{GREEN} Select on option{F}")
    print()
    print(f"           {B}{RED}                               [{B}{WHITE}1{B}{RED}]{B}{GREEN} SSH Cliente{F}")
    print(f"           {B}{RED}                               [{B}{WHITE}2{B}{RED}]{B}{GREEN} SSH Servidor{F}")
    print(f"           {B}{RED}                               [{B}{WHITE}3{B}{RED}]{B}{GREEN} SAIR.{F}")
    print()
    r1 = (int(input(f"{B}{GREEN}Crypr: {F}")))

    if r1 == 1:
        # Iniciando o cliente SSH
        print("")
        print(f"{B}{RED}[{B}{WHITE}*{B}{RED}]{B}{GREEN} Iniciado SSH Cliente{F}")
        with open('SSH_rcmd.py', 'r') as file:
            SSH_rcmd = file.read()
            exec(SSH_rcmd)
        print("[*] Teste de ssh_rcmd")
    elif r1 == 2:
        # Iniciando o Servidor SSH
        print("")
        print(f"{B}{RED}[{B}{WHITE}*{B}{RED}]{B}{GREEN} Iniciado SSH Servidor{F}")
        with open('SSH_server.py', 'r') as file:
            SSH_server = file.read()
            exec(SSH_server)
        print("[*] Teste de SSH_server")
    else:
        print()
        print(f"{B}{RED}[{B}{WHITE}!{B}{RED}]{B}{GREEN} SAIR{F}")
        exit()

if __name__ == '__main__':
    clear()
    logo()
    info()
