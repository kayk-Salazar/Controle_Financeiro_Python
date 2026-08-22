from abc import ABC, abstractmethod
from exceptions.custom_exceptions import InvalidTextError
class Validator(ABC):

    def validate_text(self, value):

        if not isinstance(value, str):
            raise InvalidTextError ('A entrada deve ser um texto')

        if not value.strip():
            raise InvalidTextError ('A entrada não pode esta vazia')

        return value.strip()

    @abstractmethod
    def validate(self, value):
        pass