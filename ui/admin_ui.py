from exceptions.custom_exceptions import InvalidInputError
from exceptions.custom_exceptions import NotFoundError

class AdminUI:
    def __init__(
        self, 
        transaction_service,
        user_service, 
        user_account_service,
        account_service,
        user_ui
        ):

        self.transaction_service = transaction_service
        self.user_service = user_service
        self.user_account_service = user_account_service
        self.account_service = account_service
        self.user_ui = user_ui


    def admin_menu(self):
        while True:
            print("\n==== ADMINISTRADOR ====")
            print("1 - Usuários")
            print("2 - Contas")
            print("3 - Transações")
            print("0 - Voltar")

            menu_of_options = {
                "1": self.admin_user_search_menu,
                "2": self.admin_account_search_menu,
                "3": self.admin_transaction_search_menu
            }

            option = input("Escolha uma opção: ")

            if option == "0":
                return
            
            get = menu_of_options.get(option)

            if get:
                get()
            else:
                print("Opção Inválida")


    def admin_user_search_menu(self):
        while True:
            print("\n==== BUSCAR USUÁRIO ====")
            print("1 - Buscar por ID")
            print('2 - Buscar por CPF')
            print("3 - Buscar por e-email")
            print("4 - Buscar por telefone")
            print("0 - Voltar")

            options_of_menu = {
                "1":self.admin_find_user_by_id,
                "2":self.admin_find_user_by_cpf,
                "3":self.admin_find_user_by_email,
                "4":self.admin_find_user_by_phone
            }

            option = input("Escolha uma opção: ")

            if option == "0":
                return
            
            get = options_of_menu.get(option)

            if get:
                get()
            else:
                print("Opção inválida")

     
    def _admin_find_user_or_account(self, search_method, message):

        while True:
            try:
                value = input(message)

                if value.lower() == "voltar":
                    return None

                return search_method(value)

            except (InvalidInputError, NotFoundError) as error:
                print(error)


    def _admin_user_preview(self, user):

        print("\nDADOS PESSOAIS")
        print(f"ID: {user['id']}")
        print(f"Nome: {user['first_name'].capitalize()}")
        print(f"Sobrenome: {user['last_name'].capitalize()}")
        print(f"E-mail: {user['email']}")
        print(f"Telefone: {user['phone']}")
        print(f"CPF: {user['cpf']}")

        print("\n1 - Entrar")
        print("2 - Voltar")

        while True:
            option = input("Escolha uma opção: ")

            if option == "1":
                return "entrar"

            if option == "2":
                return "voltar"

            print("Opção inválida.")


    def _admin_account_preview(self, account):
    
        print("\nDADOS PESSOAIS")
        print(f"ID: {account['id']}")
        print(f"Numero da conta: {account['account_number']}")
        print(f"Saldo: {account['balance']}")
        print(f"Status: {account['status']}")
        

        print("\n1 - Entrar")
        print("2 - Voltar")

        while True:
            option = input("Escolha uma opção: ")

            if option == "1":
                return "entrar"

            if option == "2":
                return "voltar"

            print("Opção inválida.")

    
    def admin_find_user_by_id(self):

        user = self._admin_find_user_or_account(
            self.user_service.find_by_id,
            "Digite o ID (ou 'voltar' para retornar): "
        )

        if user is None:
            return

        action = self._admin_user_preview(user)

        if action == "entrar":
            self.admin_user_details(user["id"])

        elif action == "voltar":
            return


    def admin_find_user_by_cpf(self):

        user = self._admin_find_user_or_account(
            self.user_service.find_by_cpf,
            "Digite o CPF (ou 'voltar' para retornar): "
        )

        if user is None:
            return

        action = self._admin_user_preview(user)

        if action == "entrar":
            self.admin_user_details(user["id"])

        elif action == "voltar":
            return


    def admin_find_user_by_email(self):

        user = self._admin_find_user_or_account(
               self.user_service.find_by_email,
               "Digite o e-email (ou 'voltar' para retornar): "
        )

        if user is None:
            return

        action = self._admin_user_preview(user)

        if action == "entrar":
            self.admin_user_details(user["id"])

        elif action == "voltar":
            return


    def admin_find_user_by_phone(self):

        user = self._admin_find_user_or_account(
                self.user_service.find_by_phone,
                "Digite o telefone (DDD + número) ou 'voltar' para retornar: "
        )
        
        if user is None:
            return

        action = self._admin_user_preview(user)

        if action == "entrar":
            self.admin_user_details(user["id"])

        elif action == "voltar":
            return

    
    def admin_user_details(self, user):
        
        while True:
            user_details = self.user_account_service.find_user_and_account_by_id(user)
            print("\nDADOS PESSOAIS")
            print(f"Id: {user_details["user_id"]}")
            print(f"Nome: {user_details["first_name"].capitalize()}")
            print(f"Sobrenome: {user_details["last_name"].capitalize()}")
            print(f"E-mail: {user_details["email"]}")
            print(f"Telefone: {user_details["phone"]}")
            print(f"Data de criação: {user_details["created_at"]}")

            print("-"*20)
            print("CONTA")
            print(f"Id: {user_details["account_id"]}")
            print(f"Número da conta: {user_details["account_number"]}")
            print(f"Saldo: {user_details["balance"]}")
            print(f"Status: {user_details["status"]}")
            print(f"Data de criação: {user_details["created_at"]}")
            print("-"*20)
            status = user_details["status"]

            print("1 - Ver extrato")
            if status == "ACTIVE":
                print("2 - Bloquear conta")
            else:
                print("2 - Ativar conta")
            print('0 - Voltar')

            option = input("Escolha uma opção: ")

            if option == "1":
                self.user_ui.transactions_menu(user_details)

            if option == "2":
                if status == "ACTIVE":
                    self.account_service.block_account(user_details["account_id"])
                    print("Essa conta foi bloqueada")
                    
                else:
                    self.account_service.activate_account(user_details["account_id"])
                    print("Essa conta foi reativada.")
                continue
            
            if option == "0":
                return
            else:
                print("Opção Inválida")

        
    def admin_account_search_menu(self):
        while True:
            print("\n==== BUSCAR CONTA ====")
            print("1 - Buscar conta por ID")
            print('2 - Buscar conta por numero da conta')
            print("3 - Buscar contas ativas")
            print("4 - Buscar contas bloqueadas")
            # print("5 - buscar por periodo")
            print("0 - Voltar")

            options_of_menu = {
                "1":self.admin_find_account_by_id,
                "2":self.admin_find_account_by_account_number,
                "3":self.admin_find_accounts_by_status_active,
                "4":self.admin_find_accounts_by_status_blocked,
                # "5":self.admin_find_accounts_by_period
            }

            option = input("Escolha uma opção: ")

            if option == "0":
                return

            get = options_of_menu.get(option)

            if get:
                get()
            else:
                print("Opção inválida")

    def admin_find_account_by_id(self):
        
        account = self._admin_find_user_or_account(
            self.account_service.find_by_id,
            "Digite o ID (ou 'voltar' para retornar): "
        )

        if account is None:
            return

        action = self._admin_account_preview(account)

        if action == "entrar":
            self.admin_user_details(account["user_id"])

        elif action == "voltar":
            return


    def admin_find_account_by_account_number(self):

        account = self._admin_find_user_or_account(
            self.account_service.find_by_account_number,
            "Digite o numero da conta (ou 'voltar' para retornar): "
        )

        if account is None:
            return

        action = self._admin_account_preview(account)

        if action == "entrar":
            self.admin_user_details(account["user_id"])

        elif action == "voltar":
            return       


    def admin_find_accounts_by_status_active(self):

        try:
            accounts_active = self.account_service.find_by_status("ACTIVE")

        except NotFoundError as erro:
            print(erro)
            return

        for accounts in accounts_active:
            print("\nDADOS PESSOAIS")
            print(f"ID: {accounts['id']}")
            print(f"Numero da conta: {accounts['account_number']}")
            print(f"Saldo: {accounts['balance']}")
            print(f"Status: {accounts['status']}")
           
            
    def admin_find_accounts_by_status_blocked(self):

        try:
            accounts_blocked = self.account_service.find_by_status("BLOCKED")

        except NotFoundError as erro:
            print(erro)
            return


        for accounts in accounts_blocked:
            print("\nDADOS PESSOAIS")
            print(f"ID: {accounts['id']}")
            print(f"Numero da conta: {accounts['account_number']}")
            print(f"Saldo: {accounts['balance']}")
            print(f"Status: {accounts['status']}")


    def admin_transaction_search_menu(self):
        while True:
            print("\n==== BUSCA DE EXTRATO ====")
            print("1 - Extratos dos últimos 30 dias")
            print("2 - Extratos dos últimos 90 dias")
            print("3 - Extratos de depósitos")
            print("4 - Extratos de saques")
            print("5 - Extrato completo")
            print("0 - Voltar")

            options_of_menu = {

                "1":self.admin_find_transactions_last_30_days,
                "2":self.admin_find_transactions_last_90_days,
                "3":self.admin_find_deposit_transactions,
                "4":self.admin_find_withdrawals_transactions,
                "5":self.admin_find_all_transactions
            }

            option = input("Escolha uma opção: ")

            if option == "0":
                return
            
            get = options_of_menu.get(option)

            if get:
                get()
            else:
                print("Opção inválida")

            
    def admin_find_transactions_last_30_days(self):
        try:
            transactions = self.transaction_service.find_by_period("1")

        except NotFoundError as error:
            print(error)
            return

        for transaction in transactions:
            print("\n")
            print(20*"-")
            print(f"Tipo: {transaction["type"]}")
            print(f"Valor: {transaction["amount"]}")
            print(f"Saldo após:{transaction["balance_after"]}")
            print(f"Data: {transaction["created_at"]}")


    def admin_find_transactions_last_90_days(self):

        try:
            transactions = self.transaction_service.find_by_period("2")

        except NotFoundError as error:
            print(error)
            return

        for transaction in transactions:
            print("\n")
            print(20*"-")
            print(f"Tipo: {transaction["type"]}")
            print(f"Valor: {transaction["amount"]}")
            print(f"Saldo após:{transaction["balance_after"]}")
            print(f"Data: {transaction["created_at"]}")


    def admin_find_deposit_transactions(self):
        try:
            transactions = self.transaction_service.find_by_type("1")

        except NotFoundError as error:
            print(error)
            return

        for transaction in transactions:
            print("\n")
            print(20*"-")
            print(f"Tipo: {transaction["type"]}")
            print(f"Valor: {transaction["amount"]}")
            print(f"Saldo após:{transaction["balance_after"]}")
            print(f"Data: {transaction["created_at"]}")

        
    def admin_find_withdrawals_transactions(self):
        try:
            transactions = self.transaction_service.find_by_type("2")

        except NotFoundError as error:
            print(error)
            return

        for transaction in transactions:
            print("\n")
            print(20*"-")
            print(f"Tipo: {transaction["type"]}")
            print(f"Valor: {transaction["amount"]}")
            print(f"Saldo após:{transaction["balance_after"]}")
            print(f"Data: {transaction["created_at"]}")


    def admin_find_all_transactions(self):
        try:
            transactions = self.transaction_service.find_all()

        except NotFoundError as error:
            print(error)
            return

        for transaction in transactions:
            print("\n")
            print(20*"-")
            print(f"Tipo: {transaction["type"]}")
            print(f"Valor: {transaction["amount"]}")
            print(f"Saldo após:{transaction["balance_after"]}")
            print(f"Data: {transaction["created_at"]}")
        
    
