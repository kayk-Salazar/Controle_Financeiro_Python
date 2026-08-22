from exceptions.custom_exceptions import AlreadyExistsError
from exceptions.custom_exceptions import AuthenticationError
from exceptions.custom_exceptions import InvalidInputError

class UserUI:
    def __init__(
        self,  
        authentication_service, 
        user_account_service, 
        banking_service, 
        transaction_service, 
        user_service, 
        first_name_validator, 
        last_name_validator,
        date_validator, 
        cpf_validator, 
        email_validator, 
        phone_validator, 
        password_validator
        ):

        self.user_account_service = user_account_service
        self.user_service = user_service
        self.authentication_service = authentication_service
        self.banking_service = banking_service
        self.transaction_service = transaction_service
        self.cpf_validator = cpf_validator
        self.date_validator = date_validator
        self.email_validator = email_validator
        self.first_name_validator = first_name_validator
        self.last_name_validator = last_name_validator
        self.password_validator = password_validator
        self.phone_validator = phone_validator


    def user_menu(self):
        while True:
            print("\n=== USUÁRIO ===")
            print("1 - Cadastrar-se")
            print("2 - Login")
            print("0 - Voltar")

            menu_of_options = {
                "1": self.register,
                "2": self.login
            }
            option = input("Escolha: ")

            if option == '0':
                return
            
            result = None

            get = menu_of_options.get(option)

            if get:
                result = get()
                
            else:
                print("Opcão inválida")

            if result:
                self.logged_user_menu(result)
    
            
    def login(self):
        cpf = self._get_validated_input(
            "Digite seu CPF: ",
            self.cpf_validator
        )
        password = input("Digite sua Senha: ")

        try:
            user = self.authentication_service.login(cpf, password)
            return user

        except AuthenticationError as error:
            print("\n======== ERROR ========")
            print(error)
            print("-"*25)


    def logged_user_menu(self, user_id):
        while True:
            user = self.user_account_service.find_user_and_account_by_id(user_id)

            print("\n")
            print("="*20)
            print(f"BEM VINDO, {user["first_name"].upper()}")
            print("="*20)

            print("\nDADOS PESSOAIS")
            print(f"Nome: {user["first_name"].capitalize()}")
            print(f"Sobrenome: {user["last_name"].capitalize()}")
            print(f"E-mail: {user["email"]}")
            print(f"Telefone: {user["phone"]}")

            print("-"*20)
            print("CONTA")
            print(f"Número da conta: {user["account_number"]}")
            print(f"Saldo: {user["balance"]}")
            print(f"Status: {user["status"]}")
            print("-"*20)

            print("1.Depositar")
            print("2.Sacar")
            print("3.Extrato")
            print("0.Sair")
            print("-"*20)

            menu_of_options = {
                "1": self.deposit,
                "2": self.withdraw,
                "3": self.transactions_menu,
            }
        
            option = input("Escolha uma opção: ")

            if option == "0":
                return

            get = menu_of_options.get(option)

            if get:
                get(user)
            else:
                print("Opção inválida")


    def deposit(self, user):
        while True:
            amount = input("Digite o valor do depósito: R$")
            try:
                self.banking_service.deposit(user, amount)
                print("DEPÓSITO REALIZADO")
                return
            except InvalidInputError as error:
                print("\n======== ERROR ========")
                print(error)
                print("-"*25)


    def withdraw(self, user):
        while True:
            amount = input("Digite o valor do saque: R$")
            try:
                self.banking_service.withdraw(user, amount)
                print("SAQUE REALIZADO")
                return
            except InvalidInputError as error:
                print("\n======== ERROR ========")
                print(error)
                print("-"*25)


    def transactions_menu(self, user):
        while True:

            print("\n==== MENU DE EXTRATO ====")
            print("1 - Extratos dos últimos 30 dias")
            print("2 - Extratos dos últimos 90 dias")
            print("3 - Extratos de depósitos")
            print("4 - Extratos de saques")
            print("5 - Extrato completo")
            print("0 - Voltar")

            menu_of_options = {
                "1":self.search_my_transactions_last_30_days,
                "2":self.search_my_transactions_last_90_days,
                "3":self.search_my_deposit,
                "4":self.search_my_withdrawals,
                "5":self.search_my_all_transactions
            }
            option = input("Escolha uma opção: ")

            if option == "0":
                return

            get = menu_of_options.get(option)

            if get:
                get(user)
            else:
                print("Opção inválida")

    
    def search_my_transactions_last_30_days(self, user):
        transactions = self.transaction_service.find_by_account_and_period(user["account_id"], "1")

        for transaction in transactions:
            print("\n")
            print(20*"-")
            print(f"Tipo: {transaction["type"]}")
            print(f"Valor: {transaction["amount"]}")
            print(f"Saldo após:{transaction["balance_after"]}")
            print(f"Data: {transaction["created_at"]}")
            

    def search_my_transactions_last_90_days(self, user):
        transactions = self.transaction_service.find_by_account_and_period(user["account_id"], "2")

        for transaction in transactions:
            print("\n")
            print(20*"-")
            print(f"Tipo: {transaction["type"]}")
            print(f"Valor: {transaction["amount"]}")
            print(f"Saldo após:{transaction["balance_after"]}")
            print(f"Data: {transaction["created_at"]}")
            

    def search_my_all_transactions(self, user):
        transactions = self.transaction_service.find_by_account(user["account_id"])

        for transaction in transactions:
            print("\n")
            print(20*"-")
            print(f"Tipo: {transaction["type"]}")
            print(f"Valor: {transaction["amount"]}")
            print(f"Saldo após:{transaction["balance_after"]}")
            print(f"Data: {transaction["created_at"]}")


    def search_my_deposit(self, user):
        transactions = self.transaction_service.find_by_account_and_type(user["account_id"], "1")

        for transaction in transactions:
            print("\n")
            print(20*"-")
            print(f"Tipo: {transaction["type"]}")
            print(f"Valor: {transaction["amount"]}")
            print(f"Saldo após:{transaction["balance_after"]}")
            print(f"Data: {transaction["created_at"]}")
            
            
    def search_my_withdrawals(self, user):
        transactions = self.transaction_service.find_by_account_and_type(user["account_id"], "2")

        for transaction in transactions:
            print("\n")
            print(20*"-")
            print(f"Tipo: {transaction["type"]}")
            print(f"Valor: {transaction["amount"]}")
            print(f"Saldo após:{transaction["balance_after"]}")
            print(f"Data: {transaction["created_at"]}")


    def _get_validated_input(self, message, validator):
        while True:
            try:
                value = input(message)
                return validator.validate(value)

            except InvalidInputError as error:
                print("\n======== ERROR ========")
                print(error)
                print("-"*25)


    def register(self):

        first_name = self._get_validated_input(
            "Digite seu primeiro nome: ",
            self.first_name_validator
        )

        last_name = self._get_validated_input(
            'Digite seu sobrenome: ',
            self.last_name_validator
        )

        birth_date = self._get_validated_input(
            "Digite sua data de nascimento (AAAA-MM-DD, ex.: 2000-08-15): ",
            self.date_validator
        )

        cpf = self._get_validated_input(
            "Digite seu cpf: ",
            self.cpf_validator
        )

        email = self._get_validated_input(
            "Digite seu e-mail: ",
            self.email_validator
        )

        phone = self._get_validated_input(
            "Digite seu telefone (DDD + número)"
            "\n(ex.: 21999999999): ",
            self.phone_validator
        )

        password = self._get_validated_input(
            "\nDigite sua senha (mínimo 8 caracteres, com pelo menos "
            "\n1 letra maiúscula, 1 número e 1 caractere especial): ",
            self.password_validator
        )

        try:
            self.user_service.register_user(first_name, last_name, cpf, birth_date, email, phone, password)
            print("Usuário cadastrado com sucesso! Agora faça login para acessar sua conta.")

        except AlreadyExistsError as error:
            print("\n======== ERROR ========")
            print(error)
            print("-"*25)