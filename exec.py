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

print(f'''{Ired}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⠀⠀⠀⠀⠀⠀⠀⠀⢀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡀⠠⠤⠤⠶⠦⡴⣞⢦⣘⡿⣦⣀⠀⠀⠀⠀⣀⣠⡾⣇⣠⣞⡶⡤⠶⠶⠤⠤⢄⣀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⡠⠂⠈⠀⠀⠀⠀⠀⠀⠀⢻⢿⣿⣷⢻⡟⠋⠑⡖⠉⠛⣿⢱⣿⡿⢻⠃⠀⠀⠀⠀⠀⠀⠈⠑⠢⡀⠀⠀⠀⠀
⠀⠀⣠⠎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡓⣿⠞⠃⠀⠀⠀⡿⠀⠀⠀⠻⢿⡇⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢢⡀⠀⠀
⠀⣰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⢠⣾⡏⡉⠃⠀⠀⠀⠀⠇⠀⠀⠀⠀⠋⡉⣿⣆⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⡀⠀
⢠⠃⠀⠀⠀⠠⡀⠀⡤⠞⠛⠒⠦⣶⣯⡿⠋⣂⠀⠀⢄⠀⠀⠀⠀⠀⢀⡊⢻⣾⣷⡵⠖⠒⠚⢦⡄⠀⣠⠀⠀⠀⠀⣷⠀
⣾⠀⠀⠀⠀⠀⠻⣾⡇⠀⠀⠀⠀⠙⢻⠃⣦⣨⣳⣦⡀⢱⣶⠂⣠⣶⣫⣠⣆⢿⠛⠀⠀⠀⠀⠀⣽⡶⠃⠀⠀⠀⠀⢸⡀
⣿⣄⡀⠀⠀⠀⠀⠈⠛⠦⣀⠀⠀⠀⠸⣄⣈⠙⠉⠉⢙⠾⠿⣞⠉⠉⠉⢉⣀⡼⠁⠀⠀⢀⡠⠞⠋⠀⠀⠀⠀⠀⢀⢾⡇
⢻⣎⠣⣀⠀⠀⠀⠀⠀⠀⠉⠓⢦⡀⠀⠈⢣⠀⣴⡖⠻⢆⢠⠾⠑⢶⡄⢠⡇⠀⠀⣠⠖⠋⠀⠀⠀⠀⠀⠀⢀⡠⢋⣾⠁
⠀⠙⠧⣈⠑⠢⢤⣤⣀⣀⣀⠀⠀⠹⡤⠴⣿⣷⠻⣿⣷⣶⣿⣶⣿⡿⣣⣿⢻⠊⡾⠁⠀⢀⣀⣀⣠⡤⠤⠖⢉⡠⠟ ⠁⠀
⠀⠀⠀⠀⠉⠉⣩⠟⠋⠉⠉⠙⣆⠀⡇⡼⢿⠙⣧⠻⠿⠿⠿⠻⠿⢃⡏⢹⡼⡆⡇⢀⣾⣯⠽⠋⠉⠉⠛⠯⣁⡄⠀⠀⠀
⠀⠀⠀⣀⠴⠞⠋⠀⠀⠀⠀⣀⠼⡼⠋⠀⠘⡆⢻⣆⠀⠀⡆⠀⢀⣾⠀⡿⠁⠈⠻⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠙⠒⠂⠀
⠀⠐⠿⠄⢀⣀⣀⣠⡐⠚⠉⠁⠀⠀⠀⠀⠀⢹⢸⠙⡄⠀⡇⠀⣾⢻⡆⠇⠀⠀⠀⠀⠀⠀⣠⠤⠂⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠐⠂⠤⠄⣀⣀⣀⠈⢧⣷⣀⡇⢠⠇⠀⠇⠀⠀⣀⡠⠤⠒⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠈⠉⠙⢏⣙⡵⠒⠈⠉⡉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠢⠤⠈⠈⠀⠀⠔⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀''')


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

def consultar_cnpj(cnpj):
     url = f'https://www.receitaws.com.br/v1/cnpj/{cnpj}'
     response = requests.get(url)
     if response.status_code == 200:
          data = response.json()
          pprint_colored(data)
     else:
          print(f"{Ired}Erro na consulta do cnpj.{VRCRM}")

def exibir_menu():
    print(f'''{Gpurple}-----------------------------------
|                                 |
|     PAINEL SNAKE x SAIKY        |
|                                 |
|     Digite a opção desejada     |
|                                 |
| 1. Consulta nome                |
| 2. Consulta cpf                 |
| 3. Consulta cnpj                |
| 4. Consulta ip                  |
| 5. Consulta cep                 |
| 6. Sair                         |
|                                 |
-----------------------------------''')

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
        elif opcao == "6":
            print(f"{Nyellow}Encerrando o programa...{VRCRM}")
            break 
        elif opcao == "4":
             ip = input('Digite o ip a ser consultado: ')
             consultar_ip(ip)
        elif opcao == "5":
             cep = input('Digite o cep a ser consultado: ')
             consultar_cep(cep)
        elif opcao == "3":
             cnpj = input('Digite o cnpj a ser consultado: ')
             consultar_cnpj(cnpj)
        else:
            print(f"{Ired}Opção inválida. Tente novamente.{VRCRM}")

menu()
