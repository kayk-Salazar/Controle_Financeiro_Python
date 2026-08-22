from validators.validator import Validator
from exceptions.custom_exceptions import InvalidEmailError
from email_validator import validate_email

class EmailValidator(Validator):

    def validate(self, email):

        email = self.validate_text(email)

        try:
            valid = validate_email(email)
            return valid.normalized

        except:
            raise InvalidEmailError('O e-mail informado não está em um formato válido.') 
