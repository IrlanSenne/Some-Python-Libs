import random
import os

erros=0
sorteado=random.randrange(0, 100)
jogador=int(input("Digite seu número: "))
while (sorteado != jogador):
    os.system("cls")
    if sorteado > jogador:
        print("Errou, o número é maior que ", jogador)
    elif sorteado < jogador:
        print("Errou,  o número é menor que ",jogador)
    erros+=1
    jogador=int(input("Digite seu número"))

print(f"Acertou em {erros} tentativas... o número é {sorteado}")