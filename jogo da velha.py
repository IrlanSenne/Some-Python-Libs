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

def verificarVitoria():
    global velha
    vitoria="n"
    simbolos=["X","O"]
    for s in simbolos:
        vitoria="n"
        il=ic=0
        while il<3:
            soma=0
            ic=0
            while ic<3:
                if velha[il][ic]==s:
                    soma+=1
                ic+=1
            il+=1
            if soma == 3:
                vitoria=s
                break
        if vitoria != "n":
            break
        il=ic=0
        while ic<3:
            soma=0
            il=0
            while il<3:
                if velha[il][ic]==s:
                    soma+=1      
                il+=1          
            if soma == 3:
                vitoria=s
                break
            ic+=1
        if vitoria != "n":
            break
        soma=0
        idiag=0
        while idiag<3:
             if velha[idiag][idiag]==s:
                 soma+=1
             idiag+=1
        if soma == 3:
                vitoria=s
                break
        soma=0
        idiagl=0
        idiagc=2
        while idiagc>=0:
             if velha[idiagl][idiagc]==s:
                 soma+=1
             idiagl+=1
             idiagc-=1
        if soma == 3:
                vitoria=s
                break
    return vitoria

def redefinir():
    global velha
    global jogadas
    global quemJoga
    global maxJogadas
    global vit
    jogadas=0
    quemJoga=2
    maxJogadas=9
    vit="n"
    velha=[
        [" "," "," "],
        [" "," "," "],
        [" "," "," "]
    ]

while jogarNovamente == "s":
    while True:
        tela()
        jogadorJoga()
        cpuJoga()
        tela()
        vit=verificarVitoria()
        if vit != "n" or jogadas>=maxJogadas:
            break

    print(Fore.RED + "Fim de Jogo" + Fore.YELLOW)
    if(vit == "X" or vit == "O"):
        print(f"Resultado: Jogador {vit} venceu")
    else:
        print("Resultado: Empate")
    jogarNovamente=input(Fore.BLUE + "Jogar novamente (s- sim | n- não) "+ Fore.RESET)
    redefinir()

print(Fore.BLUE + "======================" + Fore.BLUE)
print(Fore.GREEN + "   Thank you !!!" + Fore.GREEN)
print(Fore.BLUE + "======================" + Fore.RESET)



    

