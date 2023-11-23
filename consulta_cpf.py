import requests
import pprint
print('''███████╗███╗ ██╗ █████╗ ██╗ ██╗███████╗
██╔════╝████╗ ██║██╔══██╗██║ ██╔╝██╔════╝
███████╗██╔██╗ ██║███████║█████╔╝ █████╗  
╚════██║██║╚██╗██║██╔══██║██╔═██╗ ██╔══╝  
███████║██║ ╚████║██║ ██║██║ ██╗███████╗
╚══════╝╚═╝ ╚═══╝╚═╝ ╚═╝╚═╝ ╚═╝╚══════╝
''')
def consultar_cpf(cpf):
    url = f'https://apisdedicado.nexos.dev/SerasaCpf/cpf?token=2ae274ad75c45b657547631a82358dbc&cpf={cpf}'

    try:
        response = requests.get(url)

        if response.status_code == 200:
            resultado = response.json()
            return resultado
        else:
            print('Erro na requisição. Código de status:', response.status_code)
            return None

    except requests.exceptions.RequestException as e:
        print('Erro na requisição:', str(e))
        return None

# Função para substituir valores vazios por "Sem informação" e adicionar o DDD
def substituir_valor_vazio(valor):
    if not valor:
        return "Sem informação"
    return valor

# Função para tratar formatos diferentes de data
def formatar_data(data):
    if data and len(data) >= 10:
        return data[:10]
    return "Sem informação"

# Solicita ao usuário que digite o CPF
cpf = input("Digite o CPF a ser consultado: ")

# Chama a função para consultar o CPF
resultado = consultar_cpf(cpf)

# Exibe os resultados no formato desejado
if resultado:
    pp = pprint.PrettyPrinter(indent=4)
    dados_formatados = {
        "NOME": substituir_valor_vazio(resultado['results']['NOME']),
        "DATA DE NASCIMENTO": formatar_data(resultado['results']['NASC']),
        "NOME DA MÃE": substituir_valor_vazio(resultado['results']['NOME_MAE']),
        "NOME DO PAI": substituir_valor_vazio(resultado['results']['NOME_PAI']),
        "SEXO": substituir_valor_vazio(resultado['results']['SEXO'])
    }

    emails = resultado['results'].get('emails')
    if emails:
        dados_formatados["EMAIL"] = [
            substituir_valor_vazio(email.get('EMAIL'))
            for email in emails
        ]

    telefones = resultado['results'].get('telefones')
    if telefones:
        dados_formatados["TELEFONE"] = [
            f"({telefone.get('DDD')}) {substituir_valor_vazio(telefone.get('TELEFONE'))}"
            for telefone in telefones
        ]

    enderecos = resultado['results'].get('enderecos')
    if enderecos:
        dados_formatados["ENDEREÇOS"] = [
            {
                "ENDEREÇO": substituir_valor_vazio(endereco.get('LOGR_NOME')),
                "BAIRRO": substituir_valor_vazio(endereco.get('BAIRRO')),
                "CIDADE": substituir_valor_vazio(endereco.get('CIDADE')),
                "UF": substituir_valor_vazio(endereco.get('UF')),
                "CEP": substituir_valor_vazio(endereco.get('CEP'))
            }
            for endereco in enderecos
        ]

    dados_formatados["ORGÃO EMISSOR"] = substituir_valor_vazio(resultado['results']['ORGAO_EMISSOR'])
    dados_formatados["TITULO DE ELEITOR"] = substituir_valor_vazio(resultado['results']['TITULO_ELEITOR'])
    dados_formatados["NACIONALIDADE"] = substituir_valor_vazio(resultado['results']['NACIONALID'])
    dados_formatados["RENDA"] = substituir_valor_vazio(resultado['results']['RENDA'])

    pp.pprint(dados_formatados)
else:
    print('Não foi possível obter os dados do CPF', cpf)
