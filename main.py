from validators import (
    AccountNumberValidator,
    AmountValidator,
    CpfValidator,
    DateValidator,
    FirstNameValidator,
    EmailValidator,
    IdValidator,
    LastNameValidator,
    PasswordValidator,
    PhoneValidator,
    NumberValidator,
)

from services.account_service import AccountService
from services.transaction_service import TransactionService
from services.user_sevice import UserService
from services.admin_service import AdminService
from services.authentication_service import AuthenticationService
from services.banking_service import BankingService
from services.user_account_service import UserAccountService

from database.connection import Connection
from database.initializer import DatabaseInitializer

from repositories.admin_repository import AdminRepository
from repositories.account_repository import AccountRepository
from repositories.user_repository import UserRepository
from repositories.transation_repository import TransactionRepository
from repositories.user_account_repository import UserAccountRepository

from security.password_hash import PasswordHasher

from ui.main_ui import MainUI
from ui.user_ui import UserUI
from ui.admin_ui import AdminUI

def main():
    connection = Connection()

    try:
        connection.open_connection()

        initializer = DatabaseInitializer(connection)
        initializer.initializer()


        #Repositories
        user_repository = UserRepository(connection)
        account_repository = AccountRepository(connection)
        transaction_repository = TransactionRepository(connection)
        admin_repository = AdminRepository(connection)
        user_account_repository = UserAccountRepository(connection)


        #Vlidators
        account_number_validator = AccountNumberValidator()
        amount_validator = AmountValidator()
        cpf_validator = CpfValidator()
        date_validator = DateValidator()
        first_name_validator = FirstNameValidator()
        email_validator = EmailValidator()
        id_validator = IdValidator()
        last_name_validator = LastNameValidator()
        password_validator = PasswordValidator()
        phone_validator = PhoneValidator()
        number_validator = NumberValidator()
        

        #Securities
        password_hash = PasswordHasher()


        #Services
        user_service = UserService(
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
            id_validator
        )

        admin_service = AdminService(
            connection,
            id_validator,
            admin_repository
        )

        account_service = AccountService(
            connection,
            account_repository,
            id_validator,
            account_number_validator,
            date_validator
        )

        authentication_service = AuthenticationService(
            connection,
            user_repository,
            password_hash
        )

        banking_service = BankingService(
            connection,
            amount_validator,
            account_repository,
            transaction_repository
        )

        transaction_service = TransactionService(
            connection,
            transaction_repository,
            id_validator,
            number_validator
        )
        user_account_service = UserAccountService(
            connection,
            id_validator,
            user_account_repository
        )

        user_ui = UserUI( 
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
                )
        
        admin_ui = AdminUI(
            transaction_service,
            user_service,
            user_account_service,
            account_service,
            user_ui
        )
        
        main_ui = MainUI(
            user_ui,
            admin_ui
        )
        
        main_ui.start()

    finally:
        connection.close_connection()

if __name__ == "__main__":
    main()

