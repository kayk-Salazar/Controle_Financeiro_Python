class AccountRepository:
    def __init__(self, connection):
        self.connection = connection

    def create_account(self, user_id):
        cursor = self.connection.get_cursor()

        cursor.execute(
            """
            INSERT INTO  accounts (user_id) 
            VALUES (%s)
            """,
            (user_id,))
        
        cursor.close()

    def find_by_id(self, account_id):
        cursor = self.connection.get_cursor()

        cursor.execute(
            """
            SELECT * 
            FROM accounts 
            WHERE id = %s
            """,
            (account_id,))

        account = cursor.fetchone()
        cursor.close()
        return account

    def find_by_user_id(self, user_id):
        cursor = self.connection.get_cursor()

        cursor.execute(
            """
            SELECT * 
            FROM accounts
            WHERE user_id = %s
            """,
            (user_id,))

        account = cursor.fetchone()
        cursor.close()
        return account

    def find_by_account_number(self, account_number):
        cursor = self.connection.get_cursor()

        cursor.execute(
            """
            SELECT * 
            FROM accounts 
            WHERE account_number = %s
            """,
            (account_number,))
        
        account = cursor.fetchone()
        cursor.close()
        return account
        
    def block_account(self, account_id):
        cursor = self.connection.get_cursor()

        cursor.execute(
            """
            UPDATE accounts 
            SET status = 'BLOCKED' 
            WHERE id = %s
              AND status = 'ACTIVE'
            """,
            (account_id,))

        self.connection.commit()
        cursor.close()

    def activate_account(self, account_id):
        cursor = self.connection.get_cursor()

        cursor.execute(
            """
            UPDATE accounts 
            SET status = 'ACTIVE' 
            WHERE id = %s
              AND status = 'BLOCKED'
            """,
            (account_id,))

        self.connection.commit()
        cursor.close()

    def set_balance(self, balance, account_id):
        cursor = self.connection.get_cursor()

        cursor.execute(
            """
            UPDATE accounts
            SET balance = %s
            WHERE id = %s
            """,
            (balance, account_id))

        cursor.close()

    def find_by_status(self, status):
        cursor = self.connection.get_cursor()
        cursor.execute( 
            """
            SELECT * 
            FROM accounts 
            WHERE status = %s
            """,
            (status,))
  
        accounts = cursor.fetchall()
        cursor.close()
        return accounts

    def find_by_period(self, start_date, end_date):
        cursor = self.connection.get_cursor()

        cursor.execute(
            """
            SELECT * 
            FROM accounts 
            WHERE created_at >= %s 
                AND created_at < %s
            ORDER BY created_at DESC
            """,
            (start_date, end_date))

        accounts = cursor.fetchall()
        cursor.close()
        return accounts
