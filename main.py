from database import DatabaseConta
from account import Conta
import service


def iniciar():
    # Inicializa o banco e garante que a tabela exista
    data = DatabaseConta()
    data.criar_tabela()
    # Recupera o último saldo salvo para continuar de onde parou
    saldo_inicial = data.buscar_ultimo_saldo()
    conta = Conta(saldo_inicial)

    # FLUXOS DO MENU PRINCIPAL
    # Cada função abaixo representa uma operação do sistema.
    # Aqui acontece a interação direta com o usuário (input) antes de chamar o service.
    def fluxo_deposito():
        while True:
            valor = input("Digite o valor do depósito (ou VOLTAR): ")
            resultado = service.depositar(conta, data, valor)

            if resultado in ("VOLTAR", "SUCESSO"):
                return

    def fluxo_saque():
        while True:
            valor = input("Digite o valor do saque (ou VOLTAR): ")
            resultado = service.sacar(conta, data, valor)

            if resultado in ("VOLTAR", "SUCESSO"):
                return

    def fluxo_ver_saldo():
        saldo = data.buscar_ultimo_saldo()
        print(f"Saldo atual: R$ {saldo:.2f}")

    
    # FLUXOS DO SUBMENU DE BUSCA
    # Aqui ficam os fluxos relacionados às buscas de transações.
    # Cada opção direciona para um tipo específico de filtro.
    def fluxo_buscar_por_tipo():
        tipo = input("Digite (deposito/saque) ou VOLTAR: ")
        service.buscar_por_tipo(data, tipo)

    def fluxo_buscar_por_valor():
        valor = input("Digite o valor ou VOLTAR: ")
        service.buscar_por_valor(data, valor)

    def fluxo_buscar_por_data():
        data_input = input("Digite a data (YYYY-MM-DD) ou VOLTAR: ")
        service.buscar_por_data(data, data_input)

    def fluxo_buscar_por_periodo():
        inicio = input("Data início (YYYY-MM-DD) ou VOLTAR: ")
        if inicio.upper() == "VOLTAR":
            return

        fim = input("Data fim (YYYY-MM-DD): ")
        service.buscar_por_periodo(data, inicio, fim)

    # Submenu responsável por direcionar para os tipos de busca
    def fluxo_menu_busca():
        opcoes = {
            "1": fluxo_buscar_por_tipo,
            "2": fluxo_buscar_por_valor,
            "3": fluxo_buscar_por_data,
            "4": fluxo_buscar_por_periodo,
            "0": None
        }

        while True:
            print("\n=== BUSCAR TRANSAÇÕES ===")
            print("1 - Por tipo")
            print("2 - Por valor")
            print("3 - Por data")
            print("4 - Por período")
            print("0 - Voltar")

            opcao = input("Escolha: ")

            if opcao == "0":
                return

            funcao = opcoes.get(opcao)

            if funcao:
                funcao()
            else:
                print("Opção inválida")

    # MENU PRINCIPAL 
    # Controla o fluxo geral do programa e redireciona para cada funcionalidade
    opcoes_menu = {
        "1": fluxo_deposito,
        "2": fluxo_saque,
        "3": fluxo_ver_saldo,
        "4": fluxo_menu_busca,
        "0": None
    }

    while True:
        print("\n=== CONTA BANCÁRIA ===")
        print("1 - Depositar")
        print("2 - Sacar")
        print("3 - Ver saldo")
        print("4 - Buscar transações")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "0":
            data.fechar_conexao()
            print("Saindo...")
            break

        funcao = opcoes_menu.get(opcao)

        if funcao:
            funcao()
        else:
            print("Opção inválida")


if __name__ == "__main__":
    iniciar()