from sistema import Conta
carteira = Conta()

def depositar2(carteira):
    valor = input('Insira o valor do depósito (Caso queira voltar ao menu, digite " SAIR "): ').strip().upper()
    if valor == 'SAIR':
        menu(carteira)
    else:
        try:
            valor = valor.replace(',','.')
            carteira.depositar(valor)
            print('Deposito realizado com sucesso')
            
        except ValueError:
            print('Não foi possivel realizar a operação')

def sacar2(carteira):     
        valor = input('Insira o valor do saque (Caso queira voltar ao menu, digite " SAIR " ): ').strip().upper()
        if valor == 'SAIR':
            menu(carteira)
        else:
            try:
                valor = valor.replace(',','.')
                carteira.sacar(valor)
                print('Saque realizado com sucesso')

            except ValueError:
                print('Não foi possivel realizar a operação')
     
def ver_saldo2(carteira):
    print(carteira.ver_saldo())

def menu(carteira):
    while True:
        print('-'*40)
        print('MENU DE OPÇÃO')
        print('1 - [ DEPOSITAR ] \n2 - [SACAR] \n3 - [VER SALDO] \n4 - [SAIR]')

        try:
            opcao = int(input('Escolha uma opção: '))
            print('-'*40)
            if opcao == 1:
                depositar2(carteira)

            elif opcao == 2:
                sacar2(carteira)
            
            elif opcao == 3:
                ver_saldo2(carteira)

            elif opcao == 4:
                print('Programa encerrado')
                break

            else:
                print('Esse número não esta no menu de opção')
            
        except ValueError:
            print('Apenas números são permitidos')
        
menu(carteira)
