from entities.transaction import Transaction
from exceptions.custom_exceptions import InvalidWithdrawalError

class BankingService:
    def __init__(
        self, 
        connection,
        amount_validator,
        account_repository,
        transaction_repository
        ):

        self.connection = connection
        self.amount_validator = amount_validator
        self.account_repository = account_repository
        self.transaction_repository = transaction_repository


    def deposit(self, login, amount):
        amount = self.amount_validator.validate(amount)
        account_id = login['account_id']
        type = 'Deposit'
        balance = login['balance']

        balance_after = balance + amount

        transaction = Transaction(account_id, type, amount, balance_after)

        try:
            self.account_repository.set_balance(balance_after, account_id)
            self.transaction_repository.creat_transaction(transaction)
            self.connection.commit()
            return 

        except Exception:
            self.connection.rollback()
            raise
        

    def withdraw(self, login, amount):

        amount = self.amount_validator.validate(amount)

        account_id = login['account_id']
        type = 'Withdraw'
        balance = login['balance']

        if amount >= balance:
            return InvalidWithdrawalError("Valor de saque maior que saldo")

        balance_after = balance - amount

        transaction = Transaction(account_id, type, -amount, balance_after)

        try:
            self.account_repository.set_balance(balance_after,account_id)
            self.transaction_repository.creat_transaction(transaction)
            self.connection.commit()

        except Exception:
            self.connection.rollback()
            raise
        
        


