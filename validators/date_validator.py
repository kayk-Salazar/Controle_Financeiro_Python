from validators.validator import Validator
from exceptions.custom_exceptions import InvalidDateError
from datetime import datetime

class DateValidator(Validator):

    def validate(self, date):

        date = self.validate_text(date)

        try:
               date = datetime.strptime(date,"%Y-%m-%d").date()
               return date.isoformat()
            
        except:
            raise InvalidDateError('A data informada não está em um formato válido.')
