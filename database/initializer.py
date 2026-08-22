class DatabaseInitializer:
    def __init__(self,connection):
        self.connection = connection

    def _table_users(self,cursor):
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
            id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            first_name VARCHAR(80) NOT NULL,
            last_name VARCHAR(120) NOT NULL,
            cpf VARCHAR(11) NOT NULL UNIQUE
                CHECK (LENGTH(CPF) = 11),
            birth_date  DATE  NOT NULL, 
            email VARCHAR(100) UNIQUE NOT NULL,
            phone  VARCHAR(20) UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            created_at TIMESTAMPTZ(0) NOT NULL DEFAULT NOW()) 
            """)
        
    def _table_accounts(self,cursor):
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS accounts (
            id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            user_id BIGINT NOT NULL,
            account_number BIGINT UNIQUE NOT NULL
                DEFAULT nextval('account_number_seq'),
            balance NUMERIC(15,2) NOT NULL DEFAULT 0.00,
            status VARCHAR(20) NOT NULL DEFAULT 'ACTIVE'
                CHECK (status IN ('ACTIVE', 'BLOCKED')),
            created_at TIMESTAMPTZ(0) NOT NULL DEFAULT NOW(),
            CONSTRAINT fk_accounts_users
                FOREIGN KEY (user_id)
                REFERENCES users(id))
            """)
        
    def _table_transactions(self,cursor):
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS transactions (
            id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            account_id BIGINT NOT NULL,
            type VARCHAR(20) NOT NULL,
            amount NUMERIC(15,2) NOT NULL,
            balance_after  NUMERIC(15,2) NOT NULL,
            created_at TIMESTAMPTZ(0) NOT NULL DEFAULT NOW(),
            CONSTRAINT fk_transactions_accounts
                FOREIGN KEY (account_id)
                REFERENCES accounts(id))
            """)
    def _table_admin(self,cursor):
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS admins (
            id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            username VARCHAR(20) NOT NULL UNIQUE,
            password_hash TEXT NOT NULL,
            created_at TIMESTAMPTZ(0) NOT NULL DEFAULT NOW())
            """)

    def _creat_sequence(self,cursor):
        cursor.execute(
            """
            CREATE SEQUENCE IF NOT EXISTS account_number_seq
                START WITH 10001
                INCREMENT BY 1 
            """)
        
    def initializer(self):
        cursor =  self.connection.get_cursor()
        try:
            self._creat_sequence(cursor)
            self._table_users(cursor)
            self._table_accounts(cursor)
            self._table_transactions(cursor)
            self._table_admin(cursor)
            
            self.connection.commit()

        except Exception:
            self.connection.rollback()

        finally:
            cursor.close()

        
        