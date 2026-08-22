import os
from dotenv import load_dotenv
import psycopg
from psycopg.rows import dict_row

load_dotenv()

class Connection:

    def __init__(self):
        self.conn = None

    def open_connection(self):
        self.conn = psycopg.connect(
        host = os.getenv("DB_HOST"),
        port = os.getenv("DB_PORT"),
        dbname = os.getenv("DB_NAME"),
        user = os.getenv("DB_USER"),
        password = os.getenv("DB_PASSWORD"))
        print('conexao aberta')

    def close_connection(self):
        if self.conn:
            self.conn.close()
            self.conn = None
            print('Conexão encerrada !')

    def commit(self):
        self.conn.commit()
        
    def get_cursor(self):
        return self.conn.cursor(row_factory=dict_row)

    def rollback(self):
        self.conn.rollback()

