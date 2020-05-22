import os
import random
from colorama import Fore, Back

jogarNovamente="s"
jogadas=0
quemJoga=2
maxJogadas=9
vit="n"
velha=[
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]
]

def tela():
    os.system("cls")
    print(f"    {velha[0][0]} | {velha[0][1]} | {velha[0][2]}")
    print("  -------------")
    print(f"    {velha[1][0]} | {velha[1][1]} | {velha[1][2]}")
    print("  -------------")
    print(f"    {velha[2][0]} | {velha[2][1]} | {velha[2][2]}")
    print()
    print(f"Jogadas: " + Fore.GREEN +  str(jogadas) +  Fore.RESET)
    print()

def jogadorJoga():
    global jogadas
    global quemJoga
    global maxJogadas
    if quemJoga==2 and jogadas<maxJogadas:       
        try:
            l=int(input("Linha...: "))
            c=int(input("Coluna..: "))
            while velha[l][c] != " ":
                l=int(input("Linha...: "))
                c=int(input("Coluna..: "))
            velha[l][c]="X"
            quemJoga=1
            jogadas+=1
        except:
            print("Linha e/ou coluna inváida")
            os.system("pause")
            
def cpuJoga():
    global jogadas
    global quemJoga
    global maxJogadas
    if quemJoga==1 and jogadas<maxJogadas:
        l=random.randrange(0,3)
        c=random.randrange(0,3)
        while velha[l][c] != " ":
            l=random.randrange(0,3)
            c=random.randrange(0,3)
        velha[l][c]="O"
        jogadas+=1
        quemJoga=2

while True:
    tela()
    jogadorJoga()
    cpuJoga()

    

