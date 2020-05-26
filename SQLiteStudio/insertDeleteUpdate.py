import sqlite3
from sqlite3 import Error

def ConexaoBanco():
    caminho="C:\\Users\\imsen\\OneDrive\\Área de Trabalho\\Development\\python\\agenda.db"
    con=None
    try:
        con=sqlite3.connect(caminho)
    except Error as er:
        print(er)
    return con
vcon=ConexaoBanco()

nome=input("Digite um nome..........:")
telefone=input("Digite o número de telefone..........:")
email=input("Digite o email..........:")


# vsql="INSERT INTO tb_contatos (T_NOMECONTATO, T_TELEFONECONTATO, T_EMAILCONTATO) VALUES ('"+nome+"','"+telefone+"','"+email+"')"
#INSERT
def inserir(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)    
        conexao.commit()
        print("Criado com sucesso")
    except Error as er:
        print(er)
# inserir(vcon,vsql)


#DELETE
def deletar(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)    
        conexao.commit()
        print("Registro removido")
    except Error as er:
        print(er)
# vsql="DELETE FROM tb_contatos WHERE N_IDCONTATO=1"
# deletar(vcon, vsql )

def atualizar(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)    
        conexao.commit()
        print("Registro atualizado")
    except Error as er:
        print(er)
vsql="UPDATE  tb_contatos SET T_NOMECONTATO='Alexander Curl' WHERE N_IDCONTATO=2"
# atualizar(vcon, vsql)

def consultar(conexao,sql):   
    c=conexao.cursor()
    c.execute(sql)
    resultado=c.fetchall()
    return resultado
  
vsql="SELECT * FROM tb_contatos WHERE T_NOMECONTATO LIKE 'b%' " # between % * % , Start * % , End % *
res=consultar(vcon, vsql)
for r in res:
    print(r)