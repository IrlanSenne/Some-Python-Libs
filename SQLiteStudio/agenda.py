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

def MenuPricipal():
    os.system("cls")
    print("1 - Inserir novo registro")
    print("2 - Deletar registro")
    print("3 - Atualizar registro")
    print("4 - Consultar registro por ID")
    print("5 - Consultar registro por nome")
    print("6 - Sair")

def menuInserir():
    print()

def menuDeletar():
    print()

def menuAtualizar():
    print()

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
os.system("pause")
