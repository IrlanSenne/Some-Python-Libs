import os
import sqlite3
from sqlite3 import Error

#Connecion

def ConexaoBanco():
    caminho="C:\\Users\\imsen\\OneDrive\\Área de Trabalho\\Development\\python\\agenda.db"
    con=None
    try:
        con=sqlite3.connect(caminho)
    except Error as er:
        print(er)
    return con
vcon=ConexaoBanco()

def query(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as er:
        print(er)
    finally:
        print("Operação realizada com sucesso")
        #conexao.close()

def consultar(conexao,sql):
    c=conexao.cursor()
    c.execute(sql)
    res=c.fetchall()
    return res

def MenuPricipal():
    os.system("cls")
    print("1 - Inserir novo registro")
    print("2 - Deletar registro")
    print("3 - Atualizar registro")
    print("4 - Consultar registro por ID")
    print("5 - Consultar registro por nome")
    print("6 - Sair")

def menuInserir():
    os.system("cls")
    nome=input("Digite o nome : ")
    telefone=input("Digite o telefone : ")
    email=input("Digite o email : ")
    vsql="INSERT INTO tb_contatos (T_NOMECONTATO, T_TELEFONECONTATO, T_EMAILCONTATO) VALUES ('"+nome+"','"+telefone+"','"+email+"')"
    query(vcon, vsql)

def menuDeletar():
    os.system("cls")
    vid=input("Digite o ID do registro a ser deletado : ")
    vsql="DELETE FROM tb_contatos WHERE N_IDCONTATO="+vid
    query(vcon, vsql)

def menuAtualizar():
    os.system("cls")
    vid=input("Digite o ID do registro a ser atualizado : ")
    r=consultar(vcon,"SELECT * FROM tb_contatos WHERE N_IDCONTATO="+vid)
    rnome=r[0][1]
    rtelefone=r[0][2]
    remail=r[0][3]
    nome=input("Digite o nome : ")
    telefone=input("Digite o telefone : ")
    email=input("Digite o email : ")
    if len(nome) == 0 :
        nome=rnome
    if len(telefone)== 0:
        telefone=rtelefone
    if len(email)== 0:
        email=remail
    vsql="UPDATE tb_contatos SET T_NOMECONTATO='"+nome+"', T_TELEFONECONTATO='"+telefone+"', T_EMAILCONTATO='"+email+"' WHERE N_IDCONTATO="+vid 
    query(vcon,vsql)

def menuConsultarId():
    print()

def menuConsultarNome():
    print()



opc=0
while opc != 6:
    MenuPricipal()
    opc=int(input("Digite ma opção: "))
    if opc == 1:
        menuInserir()
    elif opc == 2:
        menuDeletar()
    elif opc == 3:
        menuAtualizar()
    elif opc == 4:
        menuConsultarId()
    elif opc == 5:
        menuConsultarNome()
    elif opc == 6:
        os.system("cls")
        print("Fim")
    else:
        os.system("cls")
        print("Opção inválida")
        os.system("pause")

vcon.close()
os.system("pause")
