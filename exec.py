import requests
import pprint
import json 
import os
import colorama 
from colorama import Fore, Back, Style


Mblack = '\033[1;30m'   # Preto
Ired = '\033[1;31m'     # Vermelho
Dgreen = '\033[1;32m'   # Verde
Nyellow = '\033[1;33m'  # Amarelo
Iblue = '\033[1;34m'    # Azul
Gpurple = '\033[1;35m'  # Roxo
Hcyan = '\033[1;36m'    # Ciano
Twhite = '\033[1;37m'   # Branco
VRCRM = '\033[0;0m'     # Remover

def clear_terminal():
    os.system('cls') if os.name == 'nt' else os.system('clear')
clear_terminal()

print(f'''{Gpurple} .S_sSSs     .S_SSSs     .S   .S_sSSs      sSSs  S.              sSSs   .S_sSSs     .S_SSSs     .S    S.     sSSs
.SS~YS%%b   .SS~SSSSS   .SS  .SS~YS%%b    d%%SP  SS.            d%%SP  .SS~YS%%b   .SS~SSSSS   .SS    SS.   d%%SP
S%S   `S%b  S%S   SSSS  S%S  S%S   `S%b  d%S'    S%S           d%S'    S%S   `S%b  S%S   SSSS  S%S    S&S  d%S'
S%S    S%S  S%S    S%S  S%S  S%S    S%S  S%S     S%S           S%|     S%S    S%S  S%S    S%S  S%S    d*S  S%S
S%S    d*S  S%S SSSS%S  S&S  S%S    S&S  S&S     S&S           S&S     S%S    S&S  S%S SSSS%S  S&S   .S*S  S&S
S&S   .S*S  S&S  SSS%S  S&S  S&S    S&S  S&S_Ss  S&S           Y&Ss    S&S    S&S  S&S  SSS%S  S&S_sdSSS   S&S_Ss
S&S_sdSSS   S&S    S&S  S&S  S&S    S&S  S&S~SP  S&S           `S&&S   S&S    S&S  S&S    S&S  S&S~YSSY%b  S&S~SP
S&S~YSSY    S&S    S&S  S&S  S&S    S&S  S&S     S&S             `S*S  S&S    S&S  S&S    S&S  S&S    `S%  S&S
S*S         S*S    S&S  S*S  S*S    S*S  S*b     S*b              l*S  S*S    S*S  S*S    S&S  S*S     S%  S*b
S*S         S*S    S*S  S*S  S*S    S*S  S*S.    S*S.            .S*P  S*S    S*S  S*S    S*S  S*S     S&  S*S.
S*S         S*S    S*S  S*S  S*S    S*S   SSSbs   SSSbs        sSS*S   S*S    S*S  S*S    S*S  S*S     S&   SSSbs
S*S         SSS    S*S  S*S  S*S    SSS    YSSP    YSSP        YSS'    S*S    SSS  SSS    S*S  S*S     SS    YSSP
SP                 SP   SP   SP                                        SP                 SP   SP
Y                  Y    Y    Y                                         Y                  Y    Y

''')


def pprint_colored(data):
    colored_data = pprint.pformat(data)
    print(Fore.GREEN + colored_data + Style.RESET_ALL)

def consultar_nome(nome):
    url = f'https://apisdedicado.nexos.dev/SerasaNome/nome?token=2ae274ad75c45b657547631a82358dbc&nome={nome}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        pprint_colored(data)
    else:
        print(f'{Fore.RED}Erro na consulta do nome.{VRCRM}')

def consultar_cpf(cpf):
    url = f'https://apisdedicado.nexos.dev/SerasaCpf/cpf?token=2ae274ad75c45b657547631a82358dbc&cpf={cpf}'
    response = requests.get(url)    
    if response.status_code == 200:
        data = response.json()
        pprint_colored(data)
    else:
                print(f"{Ired}Erro na consulta do cpf.{VRCRM}")

def consultar_ip(ip):
    url = f'https://ipwhois.app/json/{ip}'
    response = requests.get(url)    
    if response.status_code == 200:
        data = response.json()
        pprint_colored(data)
    else:
        print(f"{Ired}Erro na consulta do ip.{VRCRM}")

def consultar_cep(cep):
     url = f'https://viacep.com.br/ws/{cep}/json/'
     response = requests.get(url)
     if response.status_code == 200:
          data = response.json()
          pprint_colored(data)
     else:
          print(f"{Ired}Erro na consulta do cep.{VRCRM}")
        
def exibir_menu():
    print(f"{Hcyan}Menu:")
    print("1. Consultar nome")
    print("2. Consultar cpf")
    print("3. Consultar ip")
    print("4. Consultar cep")
    print("5. Sair")

def menu():
    while True:
        exibir_menu()
        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            nome = input('Digite o nome a ser consultado: ')
            consultar_nome(nome)
        elif opcao == "2":
            cpf = input('Digite o cpf a ser consultado: ')
            consultar_cpf(cpf)
        elif opcao == "5":
            print(f"{Nyellow}Encerrando o programa...{VRCRM}")
            break 
        elif opcao == "3":
             ip = input('Digite o ip a ser consultado: ')
             consultar_ip(ip)
        elif opcao == "4":
             cep = input('Digite o cep a ser consultado: ')
             consultar_cep(cep)
        else:
            print(f"{Ired}Opção inválida. Tente novamente.{VRCRM}")

menu()
