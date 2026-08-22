from entities.user import User
from exceptions.custom_exceptions import CPFAlreadyExistsError
from exceptions.custom_exceptions import EmailAlreadyExistsError
from exceptions.custom_exceptions import PhoneAlreadyExistsError
from exceptions.custom_exceptions import UserNotFoundError


class UserService:
    def __init__(
        self, 
        connection,
        user_repository,
        account_repository,
        password_hash,
        first_name_validator, 
        last_name_validator, 
        cpf_validator, 
        date_validator, 
        email_validator, 
        phone_validator, 
        password_validator,
        id_validator, 
        ):
        
        self.connection = connection
        self.user_repository = user_repository
        self.account_repository = account_repository
        self.password_hash = password_hash
        self.first_name_validator = first_name_validator
        self.last_name_validator = last_name_validator
        self.cpf_validator = cpf_validator
        self.date_validator = date_validator
        self.email_validator = email_validator
        self.phone_validator = phone_validator
        self.password_validator = password_validator
        self.id_validator = id_validator


    def register_user(self,first_name, last_name,cpf, date, email, phone, password ):
        user = User(first_name, last_name, cpf, date, email, phone, password)

        user.first_name = self.first_name_validator.validate(user.first_name)
        user.last_name = self.last_name_validator.validate(user.last_name)
        user.cpf = self.cpf_validator.validate(user.cpf)
        user.date = self.date_validator.validate(user.birth_date)
        user.email = self.email_validator.validate(user.email)
        user.phone = self.phone_validator.validate(user.phone)
        user.password = self.password_validator.validate(user.password)
        
        if self.user_repository.find_by_cpf(user.cpf):
            raise CPFAlreadyExistsError("Error, cpf já cadastrado")

        if self.user_repository.find_by_phone(user.phone):
            raise PhoneAlreadyExistsError("Error, telefone já cadastrado")

        if self.user_repository.find_by_email(user.email):
            raise EmailAlreadyExistsError("Error, e-mail já cadastrado")
        
        user.password = self.password_hash.hash(user.password)

        try:
            user_id = self.user_repository.create_user(user)
            self.account_repository.create_account(user_id)
            self.connection.commit()
            
        except Exception:
            self.connection.rollback()
            raise 


    def find_by_email(self, email):

        email = self.email_validator.validate(email)

        user = self.user_repository.find_by_email(email)

        if user is None:
            raise UserNotFoundError("Nenhum usuário encontrado com esse e-mail.")

        return user

    def find_by_phone(self, phone):

        phone = self.phone_validator.validate(phone)

        user = self.user_repository.find_by_phone(phone)

        if user is None:
            raise UserNotFoundError("Nenhum usuário encontrado com esse telefone")

        return user

    def find_by_id(self, user_id):

        user_id = self.id_validator.validate(user_id)

        user = self.user_repository.find_by_id(user_id)

        if user is None:
            raise UserNotFoundError("Nenhum usuário encontrado com esse id")

        return user 

    def find_by_cpf(self, cpf):
    
        cpf = self.cpf_validator.validate(cpf)

        user = self.user_repository.find_by_cpf(cpf)

        if user is None:
            raise UserNotFoundError("Nenhum usuário encontrado com esse id")

        return user 


    def find_by_period(self, start_date, end_date):

        start_date = self.date_validator.validate(start_date)
        end_date = self.date_validator.validate(end_date)

        user = self.user_repository.find_by_period(start_date, end_date)

        if not user:
            raise UserNotFoundError("Nenhum usuário encontrado nesse período.")

        return user 


    def find_by_name(self, name):

        name = self.first_name_validator.validate(name)    

        user = self.user_repository.find_by_name(name)

        if not user:
            raise UserNotFoundError("Nenhum usuário encontrado com esse nome")

        return user

    

