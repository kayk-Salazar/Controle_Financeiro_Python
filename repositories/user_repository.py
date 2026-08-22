
class UserRepository:
    def __init__(self,connection):
        self.connection = connection
        

    def create_user(self, user):
        cursor =  self.connection.get_cursor()

        cursor.execute(
            """
            INSERT INTO users (first_name, last_name, cpf, birth_date, email, phone, password_hash)
            VALUES (%s,%s,%s,%s,%s,%s,%s)
            RETURNING id 
            """,
            (
             user.first_name,
             user.last_name,
             user.cpf,
             user.birth_date,
             user.email,
             user.phone,
             user.password))
        
        user_id= cursor.fetchone()
        cursor.close()
        return user_id['id']

    def find_by_cpf(self, cpf):
        cursor = self.connection.get_cursor()
        cursor.execute(
            """
            SELECT * 
            FROM users
            WHERE cpf = %s
            """,
            (cpf,))
        
        user = cursor.fetchone()
        cursor.close()
        return user
    
    def find_by_id(self, user_id):
        cursor = self.connection.get_cursor()

        cursor.execute(
            """
            SELECT * 
            FROM users
            WHERE id = %s
            """,
            (user_id,))
            
        user = cursor.fetchone()
        cursor.close()
        return user 


    def find_by_name(self, name):
        cursor = self.connection.get_cursor()
    
        cursor.execute(
            """
            SELECT *
            FROM users
            WHERE unaccent(first_name) 
            ILIKE unaccent(%s)
            """,
            (f"%{name}%",))
        
        users = cursor.fetchall()
        cursor.close()
        return users

    def find_by_phone(self, phone):
        cursor = self.connection.get_cursor()

        cursor.execute(
            """
            SELECT * 
            FROM users 
            WHERE phone = %s
            """,
            (phone,))

        user = cursor.fetchone()
        cursor.close()
        return user 


    def find_by_email(self, email):
        cursor = self.connection.get_cursor()

        cursor.execute(
            """
            SELECT * 
            FROM users 
            WHERE email = %s
            """,
            (email,))

        user = cursor.fetchone()
        cursor.close()
        return user 


    def find_by_period(self, start_date, end_date):
        cursor = self.connection.get_cursor()

        cursor.execute(
            """
            SELECT * 
            FROM users 
            WHERE created_at >= %s 
                AND created_at < %s
            ORDER BY created_at DESC
            """,
            (start_date, end_date))

        users = cursor.fetchall()
        cursor.close()
        return users


    def count_users(self):
        cursor = self.connection.get_cursor()

        cursor.execute(
            """
            SELECT COUNT(*) 
            FROM users
            """)
        
        user = cursor.fetchone()
        cursor.close()
        return user 



