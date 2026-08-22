from validators.validator import Validator
from exceptions.custom_exceptions import InvalidIDError

class IdValidator(Validator):
    def validate(self, id):

        id = self.validate_text(id)

        if not id.isnumeric():
            raise InvalidIDError("O ID precisa ser um número inteiro")

        return id

