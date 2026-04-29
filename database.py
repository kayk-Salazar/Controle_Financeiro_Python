# Responsável pela persistência dos dados da aplicação (leitura e escrita em JSON)
import json

ARQUIVO = 'data.json'
# Carrega os dados do arquivo JSON (saldo e histórico de transações)
def carrregar_dados():
    try:
        with open(ARQUIVO,'r') as arquivo:
            dados = json.load(arquivo)
            return{
                'saldo': dados.get('saldo',0),
                'transacoes':dados.get('transacoes',[])
            }
# Retorna valores padrão caso o arquivo não exista ou esteja inválido        
    except (FileNotFoundError, json.JSONDecodeError):
        return {'saldo': 0, 'transacoes': []}

# Salva o estado atual da conta no arquivo JSON
def salvar_dados(carteira):
    dados = {
        'saldo': carteira.saldo,
        'transacoes': carteira.transacoes
    }
    with open(ARQUIVO, 'w') as arquivo:
        json.dump(dados, arquivo, indent=4)


