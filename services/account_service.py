from exceptions.custom_exceptions import AccountNotFoundError

class AccountService:
    def __init__(
        self, 
        connection,
        account_repository,
        id_validator, 
        account_number_validator,
        date_validator
        ):
        
        self.connection = connection
        self.account_repository = account_repository
        self.id_validator = id_validator
        self.account_number_validator = account_number_validator
        self.date_validator = date_validator


    def find_by_account_number(self, account_number):

        account_number = self.account_number_validator.validate(account_number)

        account = self.account_repository.find_by_account_number(account_number)

        if account is None:
            raise AccountNotFoundError("Conta não encontrada")

        return account

    def find_by_id(self, account_id):

        account_id = self.id_validator.validate(account_id)

        account = self.account_repository.find_by_id(account_id)

        if account is None:
            raise AccountNotFoundError("Conta não encontrada") 

        return account

    def block_account(self, account_id):
        account_id = str(account_id)

        account_id = self.id_validator.validate(account_id)

        self.account_repository.block_account(account_id)

    def activate_account(self, account_id):
        account_id = str(account_id)

        account_id = self.id_validator.validate(account_id)

        self.account_repository.activate_account(account_id)

    def get_status(self, account_id):
        account_id = str(account_id)

        account_id = self.id_validator.validate(account_id)

        status = self.account_repository.find_by_id(account_id)

        return status["status"]

    def find_by_status(self, account_status):

        accounts = self.account_repository.find_by_status(account_status)

        if not accounts:
            raise AccountNotFoundError("Nenhuma conta encontrada")

        return accounts

    def find_by_period(self, start_date, end_date):

        start_date = self.date_validator.validate(start_date)
        end_date = self.date_validator.validate(end_date)

        accounts = self.account_repository.find_by_period(start_date, end_date)

        if not accounts:
            raise AccountNotFoundError("Nenhuma conta encontrada Nesse Periodo")
        
        return accounts

