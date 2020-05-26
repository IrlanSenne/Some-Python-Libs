import sqlite3
from sqlite3 import Error

#### CONNECTION ####
def ConexaoBanco():
    caminho="C:\\Users\\imsen\\OneDrive\\Área de Trabalho\\Development\\python\\agenda.db"
    con=None
    try:
        con=sqlite3.connect(caminho)
    except Error as er:
        print(er)
    return con
vcon=ConexaoBanco()

def criarTabela(conexao, sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        print("Tabela criada cm sucesso")
    except Error as er:
        print(f"Erro ---- {er}")


vcon.close()