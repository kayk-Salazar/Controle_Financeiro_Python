from exceptions.custom_exceptions import TransactionNotFoundError
from exceptions.custom_exceptions import InvalidNumberError
from datetime import datetime, timedelta

class TransactionService:
    def __init__(
        self,
        connection,
        transaction_repository,
        id_validator,
        number_validator
        ):

        self.connection = connection
        self.transaction_repository = transaction_repository
        self.id_validator = id_validator
        self.number_validator = number_validator

    def find_by_account_and_period(self, account_id, period):
        account_id = str(account_id)

        account_id = self.id_validator.validate(account_id)
        period = self.number_validator.validate(period)

        end_date = datetime.now()
        #30 dias
        if period == '1':
            start_date = end_date - timedelta(days=30)
        #90 dias
        elif period == '2':
            start_date = end_date - timedelta(days=90)

        else:
            raise InvalidNumberError("Opção inválida.")

        transactions = self.transaction_repository.find_by_account_and_period(account_id, start_date, end_date)

        if not transactions:
            raise TransactionNotFoundError("Nenhuma transação encontrada nesse período.")

        return transactions

    def find_by_account_and_type(self, account_id, type):
        account_id = str(account_id)
        type = self.number_validator.validate(type)
        account_id = self.id_validator.validate(account_id)

        if type == "1":
            deposit_or_withdraw = "Deposit"
            
        elif type == "2":
            deposit_or_withdraw = "Withdraw"

        else:
            raise InvalidNumberError("Opção Inválida")

        transaction = self.transaction_repository.find_by_account_and_type(account_id, deposit_or_withdraw)

        if not transaction:
            raise TransactionNotFoundError("Nenhuma transação encontrada")

        return transaction
        
    def find_by_account(self, account_id):
        account_id = str(account_id)
        account_id = self.id_validator.validate(account_id)

        transaction = self.transaction_repository.find_by_account(account_id)

        if not transaction:
            raise TransactionNotFoundError ("Nenhuma transação encontrada")

        return transaction

    def find_by_period(self, period):
        period = self.number_validator.validate(period)

        end_date = datetime.now()
        #30 dias
        if period == '1':
            start_date = end_date - timedelta(days=30) 
        #90 dias
        elif period =='2':
            
            start_date = end_date - timedelta(days=90)

        else:
            raise TransactionNotFoundError("Opção inválida")

        transaction = self.transaction_repository.find_by_period(start_date, end_date)

        if not transaction:
            raise TransactionNotFoundError("Nenhuma transação encontrada")

        return transaction      

    def find_all(self):
        transactions = self.transaction_repository.find_all()

        if not transactions:
            raise TransactionNotFoundError("Nenhuma transação encontrada")

        return transactions

    def find_by_type(self, type):
        type = self.number_validator.validate(type)

        if type == '1':
            deposit_or_withdraw = "Deposit"
            
        elif type == '2':
            deposit_or_withdraw = "Withdraw"

        else:
            raise TransactionNotFoundError("Opção Inválida")

        transaction = self.transaction_repository.find_by_type(deposit_or_withdraw)

        if not transaction:
            raise TransactionNotFoundError("Nenhuma transação encontrada")

        return transaction





    