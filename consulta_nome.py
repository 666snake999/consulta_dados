import requests
import pprint

def consultar_nome(nome):
    url = f'https://apisdedicado.nexos.dev/SerasaNome/nome?token=2ae274ad75c45b657547631a82358dbc&nome={nome}'

    try:
        response = requests.get(url)

        if response.status_code == 200:
            resultado = response.json()
            return resultado
        else:
            print('Erro na requisição. Código de status:', response.status_code)
            return None

    except requests.exceptions.RequestException as e:
        print('Erro na requisição', str(e))
        return None

def substituir_valor_vazio(valor):
    return valor if valor else 'Não disponível'

def formatar_data(data):
    return data

# Solicita ao usuário que digite o nome
nome = input("Digite o NOME a ser consultado: ")

# Chama a função para consultar o nome
resultado = consultar_nome(nome)

# Exibe os resultados no formato desejado
if resultado:
    if isinstance(resultado['results'], list) and len(resultado['results']) > 0:
        for resultado_individual in resultado['results']:
            dados_formatados = {
                "CPF": substituir_valor_vazio(resultado_individual['CPF']),
                "DATA DE NASCIMENTO": formatar_data(resultado_individual['NASC']),
                "NOME DA MÃE": substituir_valor_vazio(resultado_individual['NOME_MAE']),
                "NOME DO PAI": substituir_valor_vazio(resultado_individual['NOME_PAI']),
                "SEXO": substituir_valor_vazio(resultado_individual['SEXO'])
            }

            emails = resultado_individual.get('emails')
            if emails:
                dados_formatados["EMAIL"] = [
                    substituir_valor_vazio(email.get('EMAIL'))
                    for email in emails
                ]

            telefones = resultado_individual.get('telefones')
            if telefones:
                dados_formatados["TELEFONE"] = [
                    f"({telefone.get('DDD')}) {substituir_valor_vazio(telefone.get('TELEFONE'))}"
                    for telefone in telefones
                ]

            enderecos = resultado_individual.get('enderecos')
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

            dados_formatados["ORGÃO EMISSOR"] = substituir_valor_vazio(resultado_individual['ORGAO_EMISSOR'])
            dados_formatados["TITULO DE ELEITOR"] = substituir_valor_vazio(resultado_individual['TITULO_ELEITOR'])
            dados_formatados["NACIONALIDADE"] = substituir_valor_vazio(resultado_individual['NACIONALID'])
            dados_formatados["RENDA"] = substituir_valor_vazio(resultado_individual['RENDA'])

            pp = pprint.PrettyPrinter(indent=4)
            pp.pprint(dados_formatados)
            print("-------------")  # Separador entre os resultados individuais
    else:
        print('Não foram encontrados dados para o nome', nome)
else:
    print('Não foi possível obter os dados do nome', nome)
