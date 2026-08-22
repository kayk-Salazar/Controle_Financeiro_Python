from validators.validator import Validator
from exceptions.custom_exceptions import InvalidAmountError
from decimal import Decimal

class AmountValidator(Validator):

    def validate(self, amount):

        amount = self.validate_text(amount).replace(".", "").replace(",", ".")

        try:
            num_decimal = Decimal(amount)
        except:
            raise InvalidAmountError("O formato do valor informado é inválido.")

        if not num_decimal > 0:
            raise InvalidAmountError("O valor deve ser maior que zero.")

        return num_decimal