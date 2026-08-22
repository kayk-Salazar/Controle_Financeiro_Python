from validators.validator import Validator
from exceptions.custom_exceptions import InvalidCPFError
from validate_docbr import CPF

class CpfValidator(Validator):

    def validate(self, cpf):

        valid = CPF()
        cpf = self.validate_text(cpf)

        if not valid.validate(cpf):
            raise InvalidCPFError("O CPF informado é inválido.")

        clean_cpf = cpf.replace(".", "").replace("-", "")
        return clean_cpf