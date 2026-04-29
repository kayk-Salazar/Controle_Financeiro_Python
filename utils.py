# Funções auxiliares para entrada e validação de dados do usuário

# Lê um valor numérico do usuário, permitindo saída com "SAIR"
def ler_valor(mensagem):
    while True:
        valor = input(f'{mensagem} (ou "SAIR"): ').strip()
# Retorna None para sinalizar cancelamento da operação
        if valor.upper() == 'SAIR':
            return None
# Ajusta formato brasileiro (ex: 1.000,50 -> 1000.50)
        valor = valor.replace('.', '').replace(',', '.')

        try:
            return float(valor)
        except ValueError:
            print('Digite um valor numérico válido (ex: 1050,50)')
            print('-'*40)


