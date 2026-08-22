class AdminRepository:
    def __init__(self, connection):
            self.connection = connection
    
    def find_user_and_account_by_user_id(self, user_id):
        cursor = self.connection.get_cursor()

        cursor.execute(
            """
            SELECT *
            FROM users
            INNER JOIN accounts
                ON accounts.user_id = users.id
            WHERE users.id = %s
            """,
            (user_id,)
            )

        result = cursor.fetchone()
        cursor.close()
        return result
    
    def find_user_and_account_by_account_id(self, account_id):
          cursor = self.connection.get_cursor()
   
          cursor.execute(
            """
            SELECT *
            FROM accounts
            INNER JOIN users
                ON accounts.user_id = users.id
            WHERE accounts.id = %s
            """,
            (account_id,)
            )

          result = cursor.fetchone()
          cursor.close()
          return result