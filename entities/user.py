class User:
    def __init__(
        self,
        first_name, 
        last_name, 
        cpf, 
        birth_date, 
        email, 
        phone, 
        password, 
        created_at = None,
        id=None
    ):

        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.cpf = cpf
        self.birth_date = birth_date
        self.email = email
        self.phone = phone 
        self.password = password
        self.created_at = created_at 
    
    
    