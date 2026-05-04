import sqlite3

class DatabaseConta:
    # Responsável por toda comunicação com o banco de dados (SQLite)
    def __init__(self):
        self.conexao = sqlite3.connect("banco.db")
        self.cursor = self.conexao.cursor()

    def criar_tabela(self):
        # Cria a tabela de transações caso ainda não exista
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS transacoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tipo TEXT NOT NULL,
            valor REAL NOT NULL,
            saldo REAL NOT NULL,
            data TIMESTAMP DEFAULT (datetime('now', 'localtime'))
        )
        """)
        self.conexao.commit()

    def registrar_transacoes(self, tipo, valor, saldo):
        # Insere uma nova transação no banco
        self.cursor.execute("""
        INSERT INTO transacoes (tipo, valor, saldo)
        VALUES (?, ?, ?)
        """, (tipo, valor, saldo))
        self.conexao.commit()

    def buscar_ultimo_saldo(self):
        # Recupera o saldo mais recente registrado
        self.cursor.execute(" SELECT saldo FROM transacoes ORDER BY id DESC LIMIT 1")
        resultado = self.cursor.fetchone()
        if resultado:
            return resultado[0]
        else:
            return 0

    # CONSULTAS 
    # Métodos responsáveis por buscar transações com diferentes filtros
    def buscar_por_tipo(self, tipo):
        self.cursor.execute("SELECT * FROM transacoes WHERE tipo = ?", (tipo,))
        return self.cursor.fetchall()

    def buscar_por_valor(self, valor):
        self.cursor.execute("SELECT * FROM transacoes WHERE valor = ? ", (valor,))
        return self.cursor.fetchall()

    def buscar_por_data(self, data):
        self.cursor.execute("SELECT * FROM transacoes WHERE date(data) = date(?)", (data,))
        return self.cursor.fetchall()

    def buscar_por_periodo(self, inicio, fim):
        # Busca dentro de um intervalo de datas
        self.cursor.execute("""
        SELECT * FROM transacoes
        WHERE date(data) BETWEEN date(?) AND date(?)
        """, (inicio, fim))
        return self.cursor.fetchall()
    
    def fechar_conexao(self):
        # Fecha a conexão com o banco
        self.conexao.close()

