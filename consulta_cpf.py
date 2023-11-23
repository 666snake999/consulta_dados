import requests
import pprint
import json 

Mblack = '\033[1;30m'   # Preto
Ired = '\033[1;31m'     # Vermelho
Dgreen = '\033[1;32m'   # Verde
Nyellow = '\033[1;33m'  # Amarelo
Iblue = '\033[1;34m'    # Azul
Gpurple = '\033[1;35m'  # Roxo
Hcyan = '\033[1;36m'    # Ciano
Twhite = '\033[1;37m'   # Branco
VRCRM = '\033[0;0m'     # Remover

print(f'''{Gpurple}
███████╗███╗ ██╗ █████╗ ██╗ ██╗███████╗
██╔════╝████╗ ██║██╔══██╗██║ ██╔╝██╔════╝
███████╗██╔██╗ ██║███████║█████╔╝ █████╗  
╚════██║██║╚██╗██║██╔══██║██╔═██╗ ██╔══╝  
███████║██║ ╚████║██║ ██║██║ ██╗███████╗
╚══════╝╚═╝ ╚═══╝╚═╝ ╚═╝╚═╝ ╚═╝╚══════╝
{VRCRM}''')

def consultar_nome(nome):
    url = f'https://apisdedicado.nexos.dev/SerasaNome/nome?token=2ae274ad75c45b657547631a82358dbc&nome={nome}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        pprint.pprint(data)
    else:
        print(f"{Ired}Erro na consulta do nome.{VRCRM}")

def consultar_cpf(cpf):
    url = f'https://apisdedicado.nexos.dev/SerasaCpf/cpf?token=2ae274ad75c45b657547631a82358dbc&cpf={cpf}'
    response = requests.get(url)    
    if response.status_code == 200:
        data = response.json()
        pprint.pprint(data)
    else:
                print(f"{Ired}Erro na consulta do cpf.{VRCRM}")

def exibir_menu():
    print(f"{Hcyan}Menu:")
    print("1. Consultar nome")
    print("2. Consultar cpf")
    print("3. Sair")

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
        elif opcao == "3":
            print(f"{Nyellow}Encerrando o programa...{VRCRM}")
            break 
        else:
            print(f"{Ired}Opção inválida. Tente novamente.{VRCRM}")

menu()
