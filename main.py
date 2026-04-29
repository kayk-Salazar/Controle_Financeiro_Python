# Arquivo principal: controla o fluxo do sistema e interação com o usuário

from database import carrregar_dados, salvar_dados
from account import Conta
from utils import ler_valor

# Inicializa a conta com dados persistidos (saldo e histórico)
dados = carrregar_dados()
carteira = Conta(dados['saldo'],dados['transacoes'])

# Loop até o usuário inserir um valor válido ou sair
def depositar2(carteira):
    while True:
        valor = ler_valor('Insira o valor do depósito')
# Permite sair da operação digitando "SAIR"
        if valor is None:
            return

        try:
            carteira.depositar(valor)
            salvar_dados(carteira)
            print('Depósito realizado com sucesso')
            return
        
        except ValueError as erro:
            print(erro)
            print('-'*40)
            continue

# Loop até o usuário inserir um valor válido ou sair
def sacar2(carteira):
    while True:
        valor = ler_valor('Insira o valor do saque')
# Permite sair da operação digitando "SAIR"
        if valor is None:
            return

        try:
            carteira.sacar(valor)
            salvar_dados(carteira)
            print('Saque realizado com sucesso')
            return
        
        except ValueError as erro:
            print(erro)
            print('-'*40)
            continue

def transacoes(carteira):
    if not carteira.transacoes:
        print('Nenhuma transação registrada')
        return
    
    for transacao in carteira.transacoes:
        print(f'{transacao['tipo']} - R$ {transacao['valor']}')


def ver_saldo2(carteira):
    print(f'Saldo: R${carteira.ver_saldo()}')

# Mapeia as opções do menu para suas funções
def menu(carteira):
    while True:
        print('-'*40)
        print('MENU DE OPÇÃO')
        print('1 - [ DEPOSITAR ] \n2 - [ SACAR ] \n3 - [ VER SALDO ] \n4 - [ TRANSACOES ] \n5 - [ SAIR ]')
        
        opcoes = {
            1: depositar2,
            2: sacar2,
            3: ver_saldo2,
            4:transacoes
        }
        try:
            opcao = int(input('Escolha uma opção: '))
            
            if opcao == 5:
                print('Programa encerrado')
                break

            funcao = opcoes.get(opcao)
            if funcao:
                funcao(carteira)
                
            else:
                print('Opção inválida, tente novamente.')
            
        except ValueError:
            print('Apenas números são permitidos.')
        
# Garante que o menu só seja executado quando este arquivo for o principal
if __name__ == "__main__":
    menu(carteira)