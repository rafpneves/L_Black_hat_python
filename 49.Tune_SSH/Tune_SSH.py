import os

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
    print(f"  {GREEN}::::::::::::...    ::::::.    :::..,::::::      {B}{RED}  .::::::.  .::::::.  {B}{GREEN} ::   .:  {F}")
    print(f"  {GREEN};;;;;;;;'''';;     ;;;`;;;;,  `;;;;;;;''''      {B}{RED} ;;;`    ` ;;;`    `  {B}{GREEN},;;   ;;, {F}")
    print(f"  {GREEN}     [[    [['     [[[  [[[[[. '[[ [[cccc      {B}{RED}  '[==/[[[[,'[==/[[[[,,{B}{GREEN}[[[,,,[[[ {F}")
    print(f"  {GREEN}     $$    $$      $$$  $$$ 'Y$c$$ $$''''       {B}{RED}   '''    $  '''    $'{B}{GREEN}$$$'''$$$ {F}")
    print(f"  {GREEN}     88,   88    .d888  888    Y88 888oo,__     {B}{RED}  88b    dP 88b    dP {B}{GREEN}888   '88o{F}")
    print(f"  {GREEN}     MMM    'YmmMMMM'  MMM     YM '''''YUMMMmmmmmmm{B}{RED}'YMmMY'   'YMmMY'  {B}{GREEN}MMM    YMM{F}")
    print("")
    print(f" {GREEN}<================================{B}{RED_T} Created by Ascoid {F}{GREEN}==============================> {F}")
    print()


def info():
    Ip_O = "192.168.1.203"
    res = "8081"
    Ip_D = "192.168.1.207"
    Porta_D = "3000"
    Usuario = "tim"

    print(f"{GREEN}[+] Informe o IP de origem{F}")
    Ip_O = (str(input(f"{B}{GREEN}Ip: {F}")))
    print("")
    print(f"{GREEN}[+] Informe o Porta para a conexão{F}")
    Porta_O = (str(input(f"{B}{GREEN}Porta: {F}")))
    print("")
    print(f"{GREEN}[+] Informe o IP de destino{F}")
    Ip_D = (str(input(f"{B}{GREEN}Ip: {F}")))
    print("")
    print(f"{GREEN}[+] Informe a Porta de destino{F}")
    Porta_D = (str(input(f"{B}{GREEN}Porta: {F}")))
    print("")
    print(f"{GREEN}[+]Informe o usuario da conexão{F}")
    Usuario = (str(input(f"{B}{GREEN}Usuario: {F}")))
    print(f"{GREEN}[*] Tunelamento inciado com o servidor {Ip_D}{F}")
    comando = (f"python3 rforward.py {Ip_O} -p {res} -r {Ip_D}:{Porta_D} -user={Usuario} --password")
    print(comando)
    print("")
    os.system(comando)


if __name__ == "__main__":
    clear()
    logo()
    info()