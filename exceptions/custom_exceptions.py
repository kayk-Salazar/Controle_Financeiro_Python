# EXCEPTIONS 

class InvalidInputError(Exception):
    pass


class NotFoundError(Exception):
    pass


class AlreadyExistsError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class OperationError(Exception):
    pass


# INVALID INPUT

class InvalidTextError(InvalidInputError):
    pass


class InvalidFirstNameError(InvalidInputError):
    pass


class InvalidLastNameError(InvalidInputError):
    pass


class InvalidCPFError(InvalidInputError):
    pass


class InvalidDateError(InvalidInputError):
    pass


class InvalidEmailError(InvalidInputError):
    pass


class InvalidPhoneError(InvalidInputError):
    pass


class InvalidPasswordError(InvalidInputError):
    pass


class InvalidIDError(InvalidInputError):
    pass


class InvalidAccountNumberError(InvalidInputError):
    pass


class InvalidAmountError(InvalidInputError):
    pass


class InvalidNumberError(InvalidInputError):
    pass


# NOT FOUND

class UserNotFoundError(NotFoundError):
    pass


class AccountNotFoundError(NotFoundError):
    pass


class TransactionNotFoundError(NotFoundError):
    pass


# ALREADY EXISTS

class CPFAlreadyExistsError(AlreadyExistsError):
    pass


class EmailAlreadyExistsError(AlreadyExistsError):
    pass


class PhoneAlreadyExistsError(AlreadyExistsError):
    pass


# AUTHENTICATION

class InvalidLoginError(AuthenticationError):
    pass


# OPERATION

class InvalidWithdrawalError(OperationError):
    pass
