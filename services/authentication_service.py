from exceptions.custom_exceptions import InvalidLoginError

class AuthenticationService:
    def __init__(
        self,
        connection,
        user_repository,
        password_hash
        ):

        self.connection = connection
        self.user_repository = user_repository
        self.password_hash = password_hash
       

    def login(self, cpf, password):
    
            user = self.user_repository.find_by_cpf(cpf)
    
            if not user:
                raise InvalidLoginError("CPF ou senha inválidos")
    
            password_hash = user["password_hash"]
    
            if not self.password_hash.verify(password, password_hash):
                raise InvalidLoginError("CPF ou senha inválidos")

            return str(user["id"])

