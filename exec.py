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

purple = Fore.MAGENTA
green = Fore.GREEN
red = Fore.RED
reset = Style.RESET_ALL

def clear_terminal():
    os.system('cls') if os.name == 'nt' else os.system('clear')
clear_terminal()

print(f'''{Dgreen}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⡉⠙⣻⣷⣶⣤⣀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⡿⠋⠀⠀⠀⠀⢹⣿⣿⡟⠉⠉⠉⢻⡿⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠰⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⣿⣿⣇⠀⠀⠀⠈⠇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠉⠛⠿⣷⣤⡤⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣶⣦⣤⣤⣀⣀⣀⡀⠉⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀
⠀⠀⠀⢀⣀⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠙⠛⠿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀
⠀⠀⣰⣿⣿⣿⣿⣿⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣧⠀⠀
⠀⠀⣿⣿⣿⠁⠀⠈⠙⢿⣿⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⠀⠀
⠀⠀⢿⣿⣿⣆⠀⠀⠀⠀⠈⠛⠿⣿⣶⣦⡤⠴⠀⠀⠀⠀⠀⣸⣿⣿⣿⡿⠀⠀
⠀⠀⠈⢿⣿⣿⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⠃⠀⠀
⠀⠀⠀⠀⠙⢿⣿⣿⣿⣶⣦⣤⣀⣀⡀⠀⠀⠀⣀⣠⣴⣾⣿⣿⣿⡿⠃⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠙⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠛⠛⠛⠛⠛⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀''')


def pprint_colored(data):
    colored_data = pprint.pformat(data)
    print(Fore.GREEN + colored_data + Style.RESET_ALL)

def consultar_nome(nome):
    url = f'https://apisdedicado.nexos.dev/SerasaNome/nome?token=2ae274ad75c45b657547631a82358dbc&nome={nome}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()


        if 'results' in data and len(data['results']) > 0:
            resultados = data['results']

            for resultado in resultados:

                NOME = resultado['NOME']
                DATA = resultado['NASC']
                CPF = resultado['CPF']
                SEXO = resultado['SEXO']
                MAE = resultado['NOME_MAE']
                PAI = resultado['NOME_PAI']
                NACIONALIDADE = resultado['NACIONALID']
                RG = resultado['RG']
                RENDA = resultado['RENDA']
                TITULO = resultado['TITULO_ELEITOR']


                formatted_response = f"{Mblack}🐍 snake painel{VRCRM}🐍\n {Gpurple}NOME:{VRCRM} {Dgreen}{NOME}{VRCRM}\n  {Gpurple}CPF:{VRCRM} {Dgreen}{CPF}{VRCRM}\n  {Gpurple}NASC:{VRCRM} {Dgreen}{DATA}{VRCRM}\n  {Gpurple}SEXO:{VRCRM} {Dgreen}{SEXO}{VRCRM}\n  {Gpurple}NOME DA MÃE:{VRCRM} {Dgreen}{MAE}{VRCRM}\n  {Gpurple}NOME DO PAI:{VRCRM} {Dgreen}{PAI}{VRCRM}\n  {Gpurple}RG:{VRCRM} {Dgreen}{RG}{VRCRM}\n  {Gpurple}NACIONALIDADE:{VRCRM} {Dgreen}{NACIONALIDADE}{VRCRM}\n  {Gpurple}RENDA:{VRCRM} {Dgreen}{RENDA}{VRCRM}\n  {Gpurple}TITULO:{VRCRM} {Dgreen}{TITULO}{VRCRM}"


                print(formatted_response)
                print()
        else:
            print(f'{Ired}Nenhum resultado encontrado para o nome fornecido.{VRCRM}')
    else:
        print(f'{Ired}Erro na consulta do nome.{VRCRM}')

def consultar_cpf(cpf):
    url = f'https://apisdedicado.nexos.dev/SerasaCpf/cpf?token=2ae274ad75c45b657547631a82358dbc&cpf={cpf}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        if 'status' in data and data['status'] == 'success' and 'results' in data and 'CPF' in data['results']:
            resultado = data['results']
            NOME = resultado['NOME']
            DATA = resultado['NASC']
            CPF = resultado['CPF']
            SEXO = resultado['SEXO']
            MAE = resultado['NOME_MAE']
            PAI = resultado['NOME_PAI']
            NACIONALIDADE = resultado['NACIONALID']
            RG = resultado['RG']
            RENDA = resultado['RENDA']
            TITULO = resultado['TITULO_ELEITOR']

            print(f"{Mblack}🐍 snake painel🐍{VRCRM}")
            print("Informações Pessoais:")
            print(f"{Gpurple}Nome:{VRCRM} {Dgreen}{NOME}{VRCRM}")
            print(f"{Gpurple}CPF:{VRCRM} {Dgreen}{CPF}{VRCRM}")
            print(f"{Gpurple}Data de Nascimento:{VRCRM} {Dgreen}{DATA}{VRCRM}")
            print(f"{Gpurple}Sexo:{VRCRM} {Dgreen}{SEXO}{VRCRM}")
            print(f"{Gpurple}Nome da mãe:{VRCRM} {Dgreen}{MAE}{VRCRM}")
            print(f"{Gpurple}Nome do pai:{VRCRM} {Dgreen}{PAI}{VRCRM}")
            print(f"{Gpurple}Nacionalidade:{VRCRM} {Dgreen}{NACIONALIDADE}{VRCRM}")
            print(f"{Gpurple}RG:{VRCRM} {Dgreen}{RG}{VRCRM}")
            print(f"{Gpurple}Renda:{VRCRM} {Dgreen}{RENDA}{VRCRM}")
            print(f"{Gpurple}Título de Eleitor:{VRCRM} {Dgreen}{TITULO}{VRCRM}")

            telefones = resultado['telefones']
            print(f"\n{Gpurple}Telefones:{VRCRM}")
            for telefone in telefones:
                ddd = telefone['DDD']
                numero = telefone['TELEFONE']
                tipo = telefone['TIPO_TELEFONE']
                print(f"{Gpurple}🐍Telefone:{VRCRM} ({Hcyan}{ddd}{VRCRM}) {Dgreen}{numero}{VRCRM} - Tipo: {Dgreen}{tipo}{VRCRM}")

            emails = resultado['emails']
            print(f"\n{Gpurple}🐍Emails:{VRCRM}")
            for email in emails:
                endereco_email = email['EMAIL']
                prioridade = email['PRIORIDADE']
                score = email['EMAIL_SCORE']
                pessoal = email['EMAIL_PESSOAL']
                duplicado = email['EMAIL_DUPLICADO']
                print(f"{Gpurple}🐍Email{VRCRM}: {Dgreen}{endereco_email}{VRCRM} - {Gpurple}Prioridade:{VRCRM} {Dgreen}{prioridade}{VRCRM} - {Gpurple}Score:{VRCRM} {Dgreen}{score}{VRCRM} - {Gpurple}Pessoal:{VRCRM} {Dgreen}{pessoal}{VRCRM} - {Gpurple}Duplicado:{VRCRM} {Dgreen}{duplicado}{VRCRM}")

            enderecos = resultado['enderecos']
            print(f"\n{Gpurple}🐍Endereços:{VRCRM}")
            for endereco in enderecos:
                tipo_logradouro = endereco['LOGR_TIPO']
                nome_logradouro = endereco['LOGR_NOME']
                numero = endereco['LOGR_NUMERO']
                complemento = endereco['LOGR_COMPLEMENTO']
                bairro = endereco['BAIRRO']
                cidade = endereco['CIDADE']
                uf = endereco['UF']
                cep = endereco['CEP']
                print(f"{Gpurple}🐍Tipo de Logradouro:{VRCRM} {Dgreen}{tipo_logradouro}{VRCRM}")
                print(f"{Gpurple}🐍Nome do Logradouro:{VRCRM} {Dgreen}{nome_logradouro}{VRCRM}")
                print(f"{Gpurple}🐍Número:{VRCRM} {Dgreen}{numero}{VRCRM}")
                print(f"{Gpurple}🐍Complemento:{VRCRM} {Dgreen}{complemento}{VRCRM}")
                print(f"{Gpurple}🐍Bairro:{VRCRM} {Dgreen}{bairro}{VRCRM}")
                print(f"{Gpurple}🐍Cidade:{VRCRM} {Dgreen}{cidade}{VRCRM}")
                print(f"{Gpurple}🐍UF:{VRCRM} {Dgreen}{uf}{VRCRM}")
                print(f"{Gpurple}🐍CEP:{VRCRM} {Dgreen}{cep}{VRCRM}")
                print()

        else:
            print("Nenhum resultado encontrado para o CPF fornecido.")
    else:
        print("Erro na consulta do CPF.")

def consultar_parente(parente):
    url = f'http://api3.beagafans.site:8080/api/parente?cpf={parente}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if len(data) > 0:
            print_parente(data[0])
        else:
            print(f"{Fore.RED}Parente não encontrado.{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}Erro na consulta de parentes.{Style.RESET_ALL}")

def print_parente(data):
    print(f"{Mblack}🐍 snake painel{VRCRM}")
    print(f"{Gpurple}CPF: {VRCRM}{Dgreen}{data['CPF_Completo']}{VRCRM}")
    print(f"{Gpurple}NOME: {VRCRM}{Dgreen}{data['NOME']}{VRCRM}")
    print(f"{Gpurple}CPF DO VINCULO: {VRCRM}{Dgreen}{data['CPF_VINCULO']}{VRCRM}")
    print(f"{Gpurple}NOME DO VINCULO: {VRCRM}{Dgreen}{data['NOME_VINCULO']}{VRCRM}")
    print(f"{Gpurple}VINCULO: {VRCRM}{Dgreen}{data['VINCULO']}{VRCRM}")

def consultar_ip(ip):
    url = f'https://ipwhois.app/json/{ip}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print_ip_details(data)
    else:
        print(f"{Fore.RED}Erro na consulta do IP.{Style.RESET_ALL}")

def print_ip_details(data):
    print(f"{Mblack}🐍 snake painel🐍{VRCRM}")
    print(f"{Gpurple}IP: {VRCRM}{Dgreen}{data['ip']}{VRCRM}")
    print(f"{Gpurple}Success: {VRCRM}{Dgreen}{data['success']}{VRCRM}")
    print(f"{Gpurple}Type: {VRCRM}{Dgreen}{data['type']}{VRCRM}")
    print(f"{Gpurple}Continent: {VRCRM}{Dgreen}{data['continent']}{VRCRM}")
    print(f"{Gpurple}Continent Code:{VRCRM}{Dgreen}{data['continent_code']}{VRCRM}")
    print(f"{Gpurple}País:{VRCRM} {Dgreen}{data['country']}{VRCRM}")
    print(f"{Gpurple}Country Code:{VRCRM}{Dgreen} {data['country_code']}{VRCRM}")
    print(f"{Gpurple}Country Flag:{VRCRM} {Dgreen}{data['country_flag']}{VRCRM}")
    print(f"{Gpurple}Country Capital:{VRCRM} {Dgreen}{data['country_capital']}{VRCRM}")
    print(f"{Gpurple}Country Phone:{VRCRM} {Dgreen}{data['country_phone']}{VRCRM}")
    print(f"{Gpurple}Country Neighbours:{VRCRM} {Dgreen} {data['country_neighbours']}{VRCRM}")
    print(f"{Gpurple}Region: {VRCRM}{Dgreen}{data['region']}{VRCRM}")
    print(f"{Gpurple}City:{VRCRM} {Dgreen}{data['city']}{VRCRM}")
    print(f"{Gpurple}Latitude:{VRCRM} {Dgreen}{data['latitude']}{VRCRM}")
    print(f"{Gpurple}Longitude: {VRCRM}{Dgreen}{data['longitude']}{VRCRM}")
    print(f"{Gpurple}ASN: {VRCRM}{Dgreen}{data['asn']}{VRCRM}")
    print(f"{Gpurple}ORG: {VRCRM}{Dgreen}{data['org']}{VRCRM}")
    print(f"{Gpurple}ISP:{VRCRM} {Dgreen}{data['isp']}{VRCRM}")
    print(f"{Gpurple}Timezone: {VRCRM}{Dgreen}{data['timezone']}{VRCRM}")
    print(f"{Gpurple}Timezone Name: {VRCRM}{Dgreen}{data['timezone_name']}{VRCRM}")
    print(f"{Gpurple}Timezone DST Offset: {VRCRM}{Dgreen}{data['timezone_dstOffset']}{VRCRM}")
    print(f"{Gpurple}Timezone GMT Offset: {VRCRM}{Dgreen}{data['timezone_gmtOffset']}{VRCRM}")
    print(f"{Gpurple}Timezone GMT: {VRCRM}{Dgreen}{data['timezone_gmt']}{VRCRM}")
    print(f"{Gpurple}Currency Code: {VRCRM}{Dgreen}{data['currency_code']}{VRCRM}")
    print(f"{Gpurple}Currency Symbol:{VRCRM} {Dgreen}{data['currency_symbol']}{VRCRM}")
    print(f"{Gpurple}urrency Rates: {VRCRM}{Dgreen}{data['currency_rates']}{VRCRM}")
    print(f"{Gpurple}Currency Plural: {VRCRM}{Dgreen}{data['currency_plural']}{VRCRM}")

def consultar_cep(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print_formatted_cep(data)
    else:
        print(f"{Ired}Erro na consulta do CEP.{VRCRM}")

def print_formatted_cep(data):
    print(f"{Mblack}🐍 snake painel🐍{VRCRM}")
    print(f"{Gpurple}🐍CEP:{VRCRM} {Dgreen}{data['cep']}{VRCRM}")
    print(f"{Gpurple}🐍LOGRADOURO:{VRCRM} {Dgreen}{data['logradouro']}{VRCRM}")
    print(f"{Gpurple}🐍COMPLEMENTO:{VRCRM} {Dgreen}{data['complemento']}{VRCRM}")
    print(f"{Gpurple}🐍BAIRRO:{VRCRM} {Dgreen}{data['bairro']}{VRCRM}")
    print(f"{Gpurple}🐍LOCALIDADE:{VRCRM} {Dgreen}{data['localidade']}{VRCRM}")
    print(f"{Gpurple}🐍UF:{VRCRM} {Dgreen}{data['uf']}{VRCRM}")
    print(f"{Gpurple}🐍IBGE:{VRCRM} {Dgreen}{data['ibge']}{VRCRM}")
    print(f"{Gpurple}🐍GIA:{VRCRM} {Dgreen}{data['gia']}{VRCRM}")
    print(f"{Gpurple}🐍DDD:{VRCRM} {Dgreen}{data['ddd']}{VRCRM}")
    print(f"{Gpurple}🐍SIAFI:{VRCRM} {Dgreen}{data['siafi']}{VRCRM}")

def consultar_cnpj(cnpj):
    url = f'https://www.receitaws.com.br/v1/cnpj/{cnpj}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print_formatted_cnpj(data)
    else:
        print(f"{Ired}Erro na consulta do CNPJ.{VRCRM}")

def print_formatted_cnpj(data):
    print(f"{Mblack}🐍 snake painel🐍{VRCRM}")
    print(f"{Gpurple}ABERTURA:{VRCRM} {Dgreen}{data['abertura']}{VRCRM}")
    print(f"{Gpurple}SITUAÇÃO:{VRCRM} {Dgreen}{data['situacao']}{VRCRM}")
    print(f"{Gpurple}TIPO:{VRCRM} {Dgreen}{data['tipo']}{VRCRM}")
    print(f"{Gpurple}NOME:{VRCRM} {Dgreen}{data['nome']}{VRCRM}")
    print(f"{Gpurple}PORTE:{VRCRM} {Dgreen}{data['porte']}{VRCRM}")
    print(f"{Gpurple}NATUREZA JURÍDICA:{VRCRM} {Dgreen}{data['natureza_juridica']}{VRCRM}")
    print(f"{Gpurple}QSA:{VRCRM}")
    for qsa in data['qsa']:
        print(f"  {Dgreen}{qsa['nome']} - {qsa['qual']}{VRCRM}")
        if 'pais_origem' in qsa:
            print(f"    {Gpurple}País de Origem:{VRCRM} {Dgreen}{qsa['pais_origem']}{VRCRM}")
        if 'nome_rep_legal' in qsa:
            print(f"    {Gpurple}Nome Representante Legal:{VRCRM} {Dgreen}{qsa['nome_rep_legal']}{VRCRM}")
        if 'qual_rep_legal' in qsa:
            print(f"    {Gpurple}Qualificação Representante Legal:{VRCRM} {Dgreen}{qsa['qual_rep_legal']}{VRCRM}")
    print(f"{Gpurple}LOGRADOURO:{VRCRM} {Dgreen}{data['logradouro']}{VRCRM}")
    print(f"{Gpurple}NÚMERO:{VRCRM} {Dgreen}{data['numero']}{VRCRM}")
    print(f"{Gpurple}COMPLEMENTO:{VRCRM} {Dgreen}{data['complemento']}{VRCRM}")
    print(f"{Gpurple}MUNICÍPIO:{VRCRM} {Dgreen}{data['municipio']}{VRCRM}")
    print(f"{Gpurple}BAIRRO:{VRCRM} {Dgreen}{data['bairro']}{VRCRM}")
    print(f"{Gpurple}UF:{VRCRM} {Dgreen}{data['uf']}{VRCRM}")
    print(f"{Gpurple}CEP:{VRCRM} {Dgreen}{data['cep']}{VRCRM}")
    print(f"{Gpurple}EMAIL:{VRCRM} {Dgreen}{data['email']}{VRCRM}")
    print(f"{Gpurple}TELEFONE:{VRCRM} {Dgreen}{data['telefone']}{VRCRM}")
    print(f"{Gpurple}DATA SITUAÇÃO:{VRCRM} {Dgreen}{data['data_situacao']}{VRCRM}")
    print(f"{Gpurple}MOTIVO SITUAÇÃO:{VRCRM} {Dgreen}{data['motivo_situacao']}{VRCRM}")
    print(f"{Gpurple}CNPJ:{VRCRM} {Dgreen}{data['cnpj']}{VRCRM}")
    print(f"{Gpurple}ÚLTIMA ATUALIZAÇÃO:{VRCRM} {Dgreen}{data['ultima_atualizacao']}{VRCRM}")
    print(f"{Gpurple}STATUS:{VRCRM} {Dgreen}{data['status']}{VRCRM}")

def consultar_email(email):
    url = f'https://apisdedicado.nexos.dev/SerasaEmail/email?token=2ae274ad75c45b657547631a82358dbc&email={email}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        pprint_colored_email(data)
    else:
        print(f"{Ired}Erro na consulta do email.{VRCRM}")

def pprint_colored_email(data):
    print(f"{Mblack}🐍 snake painel 🐍{VRCRM}")
    print(f"{Nyellow}📧 Email:{VRCRM} {Dgreen}{data['email']}{VRCRM}")
    print(f"{Nyellow}👤 Resultados:{VRCRM}")
    for result in data['results']:
        print(f"  {Gpurple}CPF:{VRCRM} {Dgreen}{result.get('CPF', '')}{VRCRM}")
        print(f"  {Gpurple}Nome:{VRCRM} {Dgreen}{result.get('NOME', '')}{VRCRM}")
        print(f"  {Gpurple}Sexo:{VRCRM} {Dgreen}{result.get('SEXO', '')}{VRCRM}")
        print(f"  {Gpurple}Data de Nascimento:{VRCRM} {Dgreen}{result.get('NASC', '')}{VRCRM}")
        print(f"  {Gpurple}Nome da Mãe:{VRCRM} {Dgreen}{result.get('NOME_MAE', '')}{VRCRM}")
        print(f"  {Gpurple}Nome do Pai:{VRCRM} {Dgreen}{result.get('NOME_PAI', '')}{VRCRM}")
        print(f"  {Gpurple}Cadastro ID:{VRCRM} {Dgreen}{result.get('CADASTRO_ID', '')}{VRCRM}")
        print(f"  {Gpurple}Estado Civil:{VRCRM} {Dgreen}{result.get('ESTCIV', '')}{VRCRM}")
        print(f"  {Gpurple}RG:{VRCRM} {Dgreen}{result.get('RG', '')}{VRCRM}")
        print(f"  {Gpurple}Nacionalidade:{VRCRM} {Dgreen}{result.get('NACIONALID', '')}{VRCRM}")
        print(f"  {Gpurple}ID do Cônjuge:{VRCRM} {Dgreen}{result.get('CONTATOS_ID_CONJUGE', '')}{VRCRM}")
        print(f"  {Gpurple}Solteiro:{VRCRM} {Dgreen}{result.get('SO', '')}{VRCRM}")
        print(f"  {Gpurple}Situação do Cadastro:{VRCRM} {Dgreen}{result.get('CD_SIT_CAD', '')}{VRCRM}")
        print(f"  {Gpurple}Data Situação do Cadastro:{VRCRM} {Dgreen}{result.get('DT_SIT_CAD', '')}{VRCRM}")
        print(f"  {Gpurple}Data Informação:{VRCRM} {Dgreen}{result.get('DT_INFORMACAO', '')}{VRCRM}")
        print(f"  {Gpurple}CBO:{VRCRM} {Dgreen}{result.get('CBO', '')}{VRCRM}")
        print(f"  {Gpurple}Órgão Emissor do RG:{VRCRM} {Dgreen}{result.get('ORGAO_EMISSOR', '')}{VRCRM}")
        print(f"  {Gpurple}UF Emissão do RG:{VRCRM} {Dgreen}{result.get('UF_EMISSAO', '')}{VRCRM}")
        print(f"  {Gpurple}Data Ocorrência:{VRCRM} {Dgreen}{result.get('DT_OB', '')}{VRCRM}")
        print(f"  {Gpurple}Código Mosaic:{VRCRM} {Dgreen}{result.get('CD_MOSAIC', '')}{VRCRM}")
        print(f"  {Gpurple}Renda:{VRCRM} {Dgreen}{result.get('RENDA', '')}{VRCRM}")
        print(f"  {Gpurple}Faixa Renda ID:{VRCRM} {Dgreen}{result.get('FAIXA_RENDA_ID', '')}{VRCRM}")
        print(f"  {Gpurple}Título de Eleitor:{VRCRM} {Dgreen}{result.get('TITULO_ELEITOR', '')}{VRCRM}")
        print(f"  {Gpurple}Código Mosaic Novo:{VRCRM} {Dgreen}{result.get('CD_MOSAIC_NOVO', '')}{VRCRM}")
        print(f"  {Gpurple}Código Mosaic Secundário:{VRCRM} {Dgreen}{result.get('CD_MOSAIC_SECUNDARIO', '')}{VRCRM}")

def consultar_ddd(ddd):
    url = f'https://brasilapi.com.br/api/ddd/v1/{ddd}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        pprint_colored_ddd(data)
    else:
        print(f"{Ired}Erro na consulta do DDD. Código de Status: {response.status_code}{VRCRM}")

def pprint_colored_ddd(data):
    if 'state' in data and 'cities' in data:
        print(f"{Mblack}🐍 SNAKE PAINEL🐍{VRCRM}")
        print(f"{Nyellow}📞 Estado:{VRCRM} {Gpurple}{data['state']}{VRCRM}")
        print(f"{Nyellow}👤 Cidades:{VRCRM}")
        for cidade in data['cities']:
            print(f"  {Dgreen}{cidade}{VRCRM}")
    else:
        print(f"{Ired}Nenhum resultado encontrado.{VRCRM}")

def consultar_banco(banco):
    url = f'https://brasilapi.com.br/api/banks/v1/{banco}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        pprint_colored_banco(data)
    else:
        print(f"{Ired}Erro na consulta do banco.{VRCRM}")

def pprint_colored_banco(data):
    print(f"{Mblack}🐍SNAKE PAINEL🐍{VRCRM}")
    print(f"{Gpurple}🏦 ISP:{VRCRM} {Dgreen}{data['ispb']}{VRCRM}")
    print(f"{Gpurple}🏦 Nome:{VRCRM} {Dgreen}{data['name']}{VRCRM}")
    print(f"{Gpurple}🏦 Código:{VRCRM} {Dgreen}{data['code']}{VRCRM}")
    print(f"{Gpurple}🏦 Nome Completo:{VRCRM} {Dgreen}{data['fullName']}{VRCRM}")

def consultar_telefone(telefone):
    url = f'http://api3.beagafans.site:8080/api/telefonia?telefone={telefone}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        pprint_colored_telefone(data)
    else:
        print(f"{Ired}Erro na consulta do telefone. Código de Status: {response.status_code}{VRCRM}")

def pprint_colored_telefone(data):
    if 'resultado' in data and data['resultado']:
        result = data['resultado'][0]
        print(f"{Mblack}🐍 SNAKE PAINEL🐍{VRCRM}")
        print(f"{Nyellow}📞 Telefone:{VRCRM} {Gpurple}{result.get('telefone', '')}{VRCRM}")
        print(f"{Nyellow}👤 Resultados:{VRCRM}")
        print(f"  {Gpurple}CPF:{VRCRM} {Dgreen}{result.get('CPF', '')}{VRCRM}")
        print(f"  {Gpurple}Nome:{VRCRM} {Dgreen}{result.get('NOME', '')}{VRCRM}")
        print(f"  {Gpurple}Logradouro:{VRCRM} {Dgreen}{result.get('LOGRDOURO', '')}{VRCRM}")
        print(f"  {Gpurple}Endereço:{VRCRM} {Dgreen}{result.get('ENDERECO', '')}{VRCRM}")
        print(f"  {Gpurple}Número:{VRCRM} {Dgreen}{result.get('NUMERO', '')}{VRCRM}")
        print(f"  {Gpurple}Bairro:{VRCRM} {Dgreen}{result.get('BAIRRO', '')}{VRCRM}")
        print(f"  {Gpurple}CEP:{VRCRM} {Dgreen}{result.get('CEP', '')}{VRCRM}")
        print(f"  {Gpurple}Cidade:{VRCRM} {Dgreen}{result.get('CIDADE', '')}{VRCRM}")
        print(f"  {Gpurple}UF:{VRCRM} {Dgreen}{result.get('UF', '')}{VRCRM}")
    else:
        print(f"{Ired}Nenhum resultado encontrado.{VRCRM}")

def consultar_rg(rg):
    url = f'http://api3.beagafans.site:8080/api/rg?rg={rg}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        pprint_colored_rg(data)
    else:
        print(f"{Ired}Erro na consulta do RG. Código de Status: {response.status_code}{VRCRM}")

def pprint_colored_rg(data):
    if 'resultado' in data and data['resultado']:
        result = data['resultado'][0]
        print(f"{Mblack}🐍 SNAKE PAINEL🐍{VRCRM}")
        print(f"{Nyellow}🆔 RG:{VRCRM} {Dgreen}{result.get('RG', '')}{VRCRM}")
        print(f"{Nyellow}👤 Resultados:{VRCRM}")
        print(f"  {Gpurple}Nome:{VRCRM} {Dgreen}{result.get('NOME', '')}{VRCRM}")
        print(f"  {Gpurple}CPF:{VRCRM} {Dgreen}{result.get('CPF', '')}{VRCRM}")
        print(f"  {Gpurple}Data de Nascimento:{VRCRM} {Dgreen}{result.get('NASC', '')}{VRCRM}")
        print(f"  {Gpurple}Nome da Mãe:{VRCRM} {Dgreen}{result.get('NOME_MAE', '')}{VRCRM}")
    else:
        print(f"{Ired}Nenhum resultado encontrado.{VRCRM}")

def consultar_score(score):
    url = f'http://api3.beagafans.site:8080/api/score?cpf={score}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        pprint_colored_score(data)
    else:
        print(f"{Ired}Erro na consulta do score. Código de Status: {response.status_code}{VRCRM}")

def pprint_colored_score(data):
    print(f"{Mblack}🐍 SNAKE PAINEL🐍{VRCRM}")
    print(f"{Nyellow}📊 Score:{VRCRM} {Gpurple}{data.get('CSBA', '')}{VRCRM}")
    print(f"{Nyellow}👤 Resultados:{VRCRM}")
    print(f"  {Gpurple}CPF:{VRCRM} {Dgreen}{data.get('CPF', '')}{VRCRM}")
    print(f"  {Gpurple}Faixa de Score:{VRCRM} {Dgreen}{data.get('CSBA_FAIXA', '')}{VRCRM}")
    print(f"  {Gpurple}Código do Poder Aquisitivo:{VRCRM} {Dgreen}{data.get('COD_PODER_AQUISITIVO', '')}{VRCRM}")
    print(f"  {Gpurple}Poder Aquisitivo:{VRCRM} {Dgreen}{data.get('PODER_AQUISITIVO', '')}{VRCRM}")
    print(f"  {Gpurple}Renda do Poder Aquisitivo:{VRCRM} {Dgreen}{data.get('RENDA_PODER_AQUISITIVO', '')}{VRCRM}")
    print(f"  {Gpurple}Faixa do Poder Aquisitivo:{VRCRM} {Dgreen}{data.get('FX_PODER_AQUISITIVO', '')}{VRCRM}")
    print(f"  {Gpurple}Renda:{VRCRM} {Dgreen}{data.get('RENDA', '')}{VRCRM}")

def consultar_placa(placa):
     url = f'http://api3.beagafans.site:8080/api/buscarPorCampo?campo=placa&valor={placa}'
     response = requests.get(url)
     if response.status_code == 200:
          data = response.json()
          pprint_colored(data)
     else:
          print(f"{Ired}Erro na consulta da placa.{VRCRM}")

def exibir_menu():
    print(f'{purple}-----------------------------------{VRCRM}')
    print(f'{purple}|                                 |{VRCRM}')
    print(f'{purple}|     PAINEL DE CONSULTAS         |{VRCRM}')
    print(f'{purple}|                Coded by: snake  |{VRCRM}')
    print(f'{purple}|     Digite a opção desejada     |{VRCRM}')
    print(f'{purple}|                                 |{VRCRM}')
    print(f'{purple}| [1] nome                 [{Dgreen}ON{VRCRM}{purple}]   |')
    print(f'{purple}| [2] cpf                  [{Dgreen}ON{VRCRM}{purple}]   |')
    print(f'{purple}| [3] cnpj                 [{Dgreen}ON{VRCRM}{purple}]   |')
    print(f'{purple}| [4] telefone             [{Dgreen}ON{VRCRM}{purple}]   |')
    print(f'{purple}| [5] parente              [{Dgreen}ON{VRCRM}{purple}]   |')
    print(f'{purple}| [6] rg                   [{Dgreen}ON{VRCRM}{purple}]   |')
    print(f'{purple}| [7] placa                [{Dgreen}ON{VRCRM}{purple}]   |')
    print(f'{purple}| [8] score                [{Dgreen}ON{VRCRM}{purple}]   |')
    print(f'{purple}| [9] email                [{Dgreen}ON{VRCRM}{purple}]   |')
    print(f'{purple}| [10] ip                  [{Dgreen}ON{VRCRM}{purple}]   |')
    print(f'{purple}| [11] cep                 [{Dgreen}ON{VRCRM}{purple}]   |')
    print(f'{purple}| [12] banco               [{Dgreen}ON{VRCRM}{purple}]   |')
    print(f'{purple}| [13] ddd                 [{Dgreen}ON{VRCRM}{purple}]   |')
    print(f'{purple}| [14] Sair                       |')
    print(f'{purple}-----------------------------------{VRCRM}')

def menu():
    while True:
        exibir_menu()
        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            nome = input(f'{Iblue}Digite o nome a ser consultado: {VRCRM}')
            consultar_nome(nome)
        elif opcao == "2":
            cpf = input(f'{Iblue}Digite o cpf a ser consultado: {VRCRM}')
            consultar_cpf(cpf)
        elif opcao == "14":
            print(f"{Nyellow}Encerrando o programa...{VRCRM}")
            break
        elif opcao == "10":
             ip = input(f'{Iblue}Digite o ip a ser consultado: {VRCRM}')
             consultar_ip(ip)
        elif opcao == "11":
             cep = input(f'{Iblue}Digite o cep a ser consultado: {VRCRM}')
             consultar_cep(cep)
        elif opcao == "3":
             cnpj = input(f'{Iblue}Digite o cnpj a ser consultado: {VRCRM}')
             consultar_cnpj(cnpj)
        elif opcao == "5":
             parente = input(f'{Iblue}Digite o cpf para consultar os parentescos: {VRCRM}')
             consultar_parente(parente)
        elif opcao == "9":
             email = input(f'{Iblue}Digite o email a ser consultado: {VRCRM}')
             consultar_email(email)
        elif opcao == "12":
             banco = input(f'{Iblue}Digite o código do banco a ser consultado: {VRCRM}')
             consultar_banco(banco)
        elif opcao == "4":
             print(f'{Nyellow}Insira o telefone com o ddd, ex: 11993536035{VRCRM}')
             telefone = input(f'{Iblue}Digite o telefone a ser consultado: {VRCRM}')
             consultar_telefone(telefone)
        elif opcao == "6":
             rg = input(f'{Iblue}Digite o rg a ser consultado: {VRCRM}')
             consultar_rg(rg)
        elif opcao == "8":
             score = input(f'{Iblue}Digite o cpf para consultar o score: {VRCRM}')
             consultar_score(score)
        elif opcao == "7":
             placa = input(f'{Iblue}Digite a placa a ser consultada: {VRCRM}')
             consultar_placa(placa)
        elif opcao == "13":
             ddd = input(f"{Iblue}Digite o ddd a ser consultado: {VRCRM}")
             consultar_ddd(ddd)
        else:
            print(f"{Ired}Opção inválida. Tente novamente.{VRCRM}")

menu()
