import os
carros=[]

class Carro:
    nome=""
    pot=0
    velMax=0
    ligado=False
    def __init__(self, nome, pot):
        self.nome=nome
        self.pot=pot
        self.velMax=int(pot)*2
        self.ligado=False
    def ligar(self):
        self.ligado=True

    def desligar(self):
        self.ligado=False

    def info(self):
        print(f"Nome...........:{self.nome}")
        print(f"Potência.......:{self.pot}")
        print(f"Vel. Máxima....:{self.velMax}")
        print(f"Ligado.........:", ("Sim" if self.ligado else "Não"))

def Menu():
    os.system("cls") or None
    print("1 - New Car")
    print("2 - Car's informations")
    print("3 - Delete Car")
    print("4 - Turn on car")
    print("5 - Turn off car")
    print("6 - List car")
    print("6 - Exit")
    print(f"7 - Quantity Cars {len(carros)}")
    opt=input("Choose an option: ")
    return opt

def newCar():
    os.system("cls") or None
    n=input("Nome do carro........: ")
    p=input("Potência do carro....: ")
    car=Carro(n,p)
    carros.append(car)
    print("Novo carro criado")
    os.system("pause")

def informacoes():
    os.system("cls") or None
    n=input("Informe o número do carro que deseja ver as informações: ")
    try:
        carros[int(n)].info()
    except:
        print("Carro não existe na lista !")
    os.system("pause")

def deleteCar():
    os.system("cls") or None
    n=input("Informe o número do carro que deseja excluir: ")   
    try:
        del carros[int(n)]
    except:
        print("Carro não existe na lista !")
    os.system("pause")

def LigarCarro():
    os.system("cls") or None
    n=input("Informe o número do carro que deseja ligar: ")   
    try:
        carros[int(n)].ligar()     
        print("Carro ligado")   
    except:
        print("Carro não existe na lista !")
    os.system("pause")

def DesligarCarro():
    os.system("cls") or None
    n=input("Informe o número do carro que deseja desligar: ")   
    try:
        carros[int(n)].desligar()     
        print("Carro desligado")   
    except:
        print("Carro não existe na lista !")
    os.system("pause")

def Listar():
    os.system("cls") or None
    p=0
    for c in carros:
        print(f"{p} - {c.nome}")
        p=p+1
    os.system("pause")

ret=Menu()
while ret < "7":
    if ret == "1":
        newCar()
    elif ret =="2":
        informacoes()
    elif ret =="3":
        deleteCar()
    elif ret =="4":
        LigarCarro()
    elif ret =="5":
        DesligarCarro()
    elif ret =="6":
        Listar()
    ret=Menu()

os.system("cls") or None
print("End")

