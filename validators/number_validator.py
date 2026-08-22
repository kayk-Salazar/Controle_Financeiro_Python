from validators.validator import Validator
from exceptions.custom_exceptions import InvalidNumberError

class NumberValidator(Validator):
    def validate(self, number):

        number = self.validate_text(number)

        if not number.isnumeric():
            raise InvalidNumberError("O valor informado precisa ser um número inteiro.")

        
        return number