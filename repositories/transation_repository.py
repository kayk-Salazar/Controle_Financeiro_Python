class TransactionRepository:
    def __init__(self, connection):
        self.connection = connection

    def creat_transaction(self, transaction):
        cursor = self.connection.get_cursor()

        cursor.execute(
            """
            INSERT INTO transactions (account_id, type, amount, balance_after)
            VALUES (%s, %s, %s, %s) 
            """,
            (transaction.account_id, 
             transaction.type, 
             transaction.amount, 
             transaction.balance_after))

        cursor.close()

    def find_by_account(self, account_id):#usado
        cursor = self.connection.get_cursor()

        cursor.execute(
            """
            SELECT * 
            FROM transactions 
            WHERE account_id = %s
            """,
            (account_id,))

        transaction = cursor.fetchall()
        cursor.close()
        return transaction

    def find_by_account_and_period(self, account_id, start_date, end_date):#usado
        cursor = self.connection.get_cursor()

        cursor.execute(
            """
            SELECT * 
            FROM transactions 
            WHERE account_id = %s
               AND created_at >= %s
               AND created_at < %s
            """, 
            (account_id , start_date, end_date))

        transaction = cursor.fetchall()
        cursor.close()
        return transaction

    def find_by_account_and_type(self, account_id,transaction_type):#usado
        cursor = self.connection.get_cursor()

        cursor.execute(
            """
            SELECT * 
            FROM transactions 
            WHERE account_id = %s 
               AND type = %s
            """,
            (account_id, transaction_type))

        transaction = cursor.fetchall()
        cursor.close()
        return transaction

    def find_by_period(self, start_date, end_date):#usado
        cursor = self.connection.get_cursor()

        cursor.execute(
            """
            SELECT * 
            FROM transactions 
            WHERE created_at >= %s 
               AND created_at < %s
            ORDER BY created_at DESC
            """,
            (start_date, end_date))

        transaction = cursor.fetchall()
        cursor.close()
        return transaction

    def find_by_type(self, transaction_type):#usado
        cursor = self.connection.get_cursor()

        cursor.execute(
            """
            SELECT * 
            FROM transactions
            WHERE type = %s 
            """,
            (transaction_type,))

        transaction = cursor.fetchall()
        cursor.close()
        return transaction

    def find_all(self):#usado
        cursor = self.connection.get_cursor()
        
        cursor.execute(
            """
            SELECT * 
            FROM transactions 
            """
            )

        transaction = cursor.fetchall()
        cursor.close()
        return transaction