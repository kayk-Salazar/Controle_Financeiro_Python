from validators.validator import Validator
from exceptions.custom_exceptions import InvalidFirstNameError
import re

class FirstNameValidator(Validator):

    def validate(self, first_name):
              
        first_name = self.validate_text(first_name)

        if bool(re.search(r'[^a-zA-Z]', first_name)):
            raise InvalidFirstNameError("O primeiro nome não pode conter números ou caracteres especiais.")

        return first_name