from validators.validator import Validator
from exceptions.custom_exceptions import InvalidPasswordError
import re

class PasswordValidator(Validator):

    def validate(self, password):

        password= self.validate_text(password)
        if not len(password) >= 8:
            raise InvalidPasswordError ("A senha deve ter no mínimo 8 caracteres.")
        
        if not any(char.isupper() for char in password):
            raise InvalidPasswordError("A senha deve conter pelo menos uma letra maiúscula.")

        if not any(char.isdigit() for char in password):
            raise InvalidPasswordError("A senha deve conter pelo menos um número.")
       
    
        if not  bool(re.search(r'[^a-zA-Z0-9]', password)):
            raise InvalidPasswordError ("A senha deve conter pelo menos um caractere especial.")
        return password


