import json


carros_list=["Chevrolet", "Honda"]
carros_tupla=("Chevrolet", "Honda")

carros_j=json.dumps(carros_list, indent=4, separators=("C","="), sort_keys=True)

print(carros_j)

jogador_j='{"Nome":"Irlan", "Time":"Espacial", "Vivo":"True"}'

jogador=json.loads(jogador_j)

#keys

for k in jogador:
    print(k)

# Items

for i in jogador.items():
    print(i)

#Values

for v in jogador.values():
    print(v)

print(jogador["Nome"])