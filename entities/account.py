class Account:
     def __init__(
        self,
        user_id, 
        account_number, 
        balance, 
        status = None,  
        created_at = None,
        id=None
    ):

        self.id = id
        self.user_id = user_id
        self.account_number = account_number
        self.balance = balance
        self.status = status
        self.created_at = created_at 