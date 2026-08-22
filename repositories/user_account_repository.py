class UserAccountRepository:
    def __init__(self, connection):
        self.connection = connection


    def find_user_and_account_by_id(self, user_id):
        cursor = self.connection.get_cursor()

        cursor.execute(
            """
            SELECT 
                users.id AS user_id,
                users.first_name,
                users.last_name,
                users.email,
                users.phone,
                users.cpf,
                users.created_at,
            
                accounts.id AS account_id,
                accounts.account_number,
                accounts.balance,
                accounts.status,
                accounts.created_at
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




    