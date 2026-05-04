def tratar_valor(valor):
    # Trata a entrada do usuário e tenta converter para número
    # Aceita formato brasileiro e permite cancelar com "VOLTAR"
    valor = valor.strip().upper()

    if valor == "VOLTAR":
        return "VOLTAR"

    valor = valor.replace(".", "").replace(",", ".")

    try:
        valor = float(valor)
    except ValueError:
        print("Valor inválido")
        return "ERRO"

    if valor <= 0:
        print("Valor deve ser positivo")
        return "ERRO"

    return valor


def depositar(conta, data, valor):
    # Realiza o depósito após validar a entrada
    valor = tratar_valor(valor)

    if valor in ("VOLTAR", "ERRO"):
        return valor
    try:

        saldo = conta.depositar(valor)

    except ValueError as erro:
        print(erro)
        return 'ERRO'

    data.registrar_transacoes("deposito", valor, saldo)
    print("Depósito realizado")
    return "SUCESSO"


def sacar(conta, data, valor):
    # Realiza o saque, validando o valor e saldo disponível
    valor = tratar_valor(valor)

    if valor in ("VOLTAR", "ERRO"):
        return valor
    
    try:
        saldo = conta.sacar(valor)

    except ValueError as erro:
        print(erro)
        return 'ERRO'
    
    data.registrar_transacoes("saque", -valor, saldo)
    print("Saque realizado")
    return "SUCESSO"

# EXIBIÇÃO DE RESULTADOS 
# Função responsável por mostrar as transações de forma organizada
def mostrar_busca(resultados):
    
    if not resultados:
        print('\nNenhuma transação encontrada')
    else:
        print('\nTransações encontradas:')
        for transacoes in resultados:
            id, tipo, valor, saldo, data = transacoes
            print(f"\nId : {id} \ntipo : {tipo} \nvalor : {valor} \nsaldo : {saldo} \ndata : {data}")

# BUSCAS
# Funções responsáveis por aplicar filtros nas transações
def buscar_por_tipo(data, tipo):
    tipo = tipo.strip().lower()

    if tipo == "voltar":
        return

    if tipo not in ("deposito", "saque"):
        print("Tipo inválido")
        return

    resultados = data.buscar_por_tipo(tipo)
    mostrar_busca(resultados)


def buscar_por_valor(data, valor):
    valor = tratar_valor(valor)

    if valor in ("VOLTAR", "ERRO"):
        return

    resultados = data.buscar_por_valor(valor)
    mostrar_busca(resultados)


def buscar_por_data(data, data_input):
    if data_input.strip().upper() == "VOLTAR":
        return

    resultados = data.buscar_por_data(data_input)
    mostrar_busca(resultados)


def buscar_por_periodo(data, inicio, fim):

    resultados = data.buscar_por_periodo(inicio, fim)
    mostrar_busca(resultados)
