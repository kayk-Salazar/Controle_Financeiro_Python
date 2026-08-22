from validators.validator import Validator
from exceptions.custom_exceptions import InvalidAccountNumberError

class AccountNumberValidator(Validator):

    def validate(self, account_number):

        account_number = self.validate_text(account_number)

        if not account_number.isnumeric():
            raise InvalidAccountNumberError("O número da conta deve conter apenas números.")

        if not len(account_number) >= 5:
            raise InvalidAccountNumberError("O número da conta deve ter no mínimo 5 dígitos.")

        return int(account_number)