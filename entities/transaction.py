class Transaction:
    def __init__(
        self,
        account_id, 
        type,
        amount, 
        balance_after,
        created_at = None,
        id=None
    ):

        self.id = id
        self.account_id = account_id
        self.type = type
        self.amount = amount
        self.balance_after = balance_after
        self.created_at = created_at 
