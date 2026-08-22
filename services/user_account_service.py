from exceptions.custom_exceptions import UserNotFoundError
class UserAccountService:
    def __init__(
        self, 
        connection, 
        id_validator, 
        user_account_repository
        ):

        self.connection = connection
        self.id_validator = id_validator
        self.user_account_repository = user_account_repository

    def find_user_and_account_by_id(self, user_id):
        user_id = str(user_id)
        user_id = self.id_validator.validate(user_id)

        user = self.user_account_repository.find_user_and_account_by_id(user_id)

        if not user:
            raise UserNotFoundError("Usuário não encontrado")
        
        return user
    