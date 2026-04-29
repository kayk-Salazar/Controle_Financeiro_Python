class Conta:
    def __init__(self):
        self.saldo = 500

    def depositar(self,valor):
        valor = float(valor)
        if valor > 0:
            self.saldo += valor 
    
        else:
            raise ValueError('O valor do deposito não pode ser negativo') 
        
    def sacar(self,valor):
        valor = float(valor)
        if valor <= self.saldo:
            self.saldo -= valor 
                 
        else:
            raise ValueError('Você não pode sacar valores maiores que seu saldo')
        
    def ver_saldo(self):
        return f'Saldo: {self.saldo}'
    
    

    