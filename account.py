class Conta:
    # Inicializa a conta com saldo e histórico; cria lista vazia se não houver transações

    def __init__(self,saldo = 0):
        self.saldo = saldo
        
    # Garante que o valor seja numérico e maior que zero
    def validar_valor(self,valor):
        if not isinstance(valor,(float,int)):
            raise ValueError('Entrada inválida: o valor deve ser numérico')
        
        if valor <= 0:
            raise ValueError('Valor inválida: o valor não pode ser negativo')
    
    # Realiza depósito e registra a transação
    def depositar(self,valor): 
        self.validar_valor(valor)
        self.saldo += valor
        return self.saldo
     
    # Realiza saque se houver saldo suficiente e registra a transação
    def sacar(self,valor):
        self.validar_valor(valor)
       
        if valor <= self.saldo:
            self.saldo -= valor
            return self.saldo
    
        # Impede saque maior que o saldo disponível
        else:
            raise ValueError('Valor inválida: o valor do saque não pode ser maior que saldo')
        

    def ver_saldo(self):
        return self.saldo


    