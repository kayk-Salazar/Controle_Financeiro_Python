from validators.validator import Validator
from exceptions.custom_exceptions import InvalidLastNameError
import re

class LastNameValidator(Validator):

    def validate(self, last_name):
    
        last_name = self.validate_text(last_name)

        if  bool(re.search(r'[^a-zA-Z ]', last_name)):
            raise InvalidLastNameError("O sobrenome não pode conter números ou caracteres especiais.")
        
        return last_name