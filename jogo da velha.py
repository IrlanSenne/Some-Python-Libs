import os
import random
from colorama import Fore, Back

jogarNovamente="s"
jogadas=0
quemJoga=2
maxJogada=9
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
    

tela()
