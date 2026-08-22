from validators.validator import Validator
from exceptions.custom_exceptions import InvalidPhoneError
import phonenumbers
from phonenumbers import NumberParseException

class PhoneValidator(Validator):

    def validate(self, phone):

        phone = self.validate_text(phone)

        try:
            phone_number = phonenumbers.parse(phone, "BR")

        except NumberParseException:
            raise InvalidPhoneError("Telefone inválido.")

        if not phonenumbers.is_valid_number(phone_number):
            raise InvalidPhoneError("Telefone inválido.")

        return phonenumbers.format_number(
            phone_number,
            phonenumbers.PhoneNumberFormat.E164
        )

