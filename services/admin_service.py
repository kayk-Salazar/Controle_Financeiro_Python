from exceptions.custom_exceptions import UserNotFoundError

class AdminService:
    def __init__(
        self, 
        connection,
        id_validator,
        admin_repository
        ):
        
        self.connection = connection
        self.id_validator = id_validator
        self.admin_repository = admin_repository

    def find_user_and_account_by_user_id(self, user_id):

        user_id = self.id_validator.validate(user_id)

        result = self.admin_repository.find_user_and_account_by_user_id(user_id)

        if result is None:
            raise UserNotFoundError('Usuário e conta não encontrado')

        return result

    def find_user_and_account_by_account_id(self, account_id):

        account_id = self.id_validator.validate(account_id)

        result = self.admin_repository.find_user_and_account_by_account_id(account_id)

        if result is None:
            raise UserNotFoundError("Usuário e Conta não encontrado")

        return result

        