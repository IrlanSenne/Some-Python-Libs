import json
#Json to Dictionary
carros_json='{"marca":"honda","modelo":"HRV","cor":"Prata" }'

carro=json.loads(carros_json)

print(carro["marca"])
print(carro["modelo"])

for x in carro.values():
    print(x)

for k,v in carro.items():
    print(f"k {k} - v {v}")

#Dictionary to JSON
carros2_json={
    "marca":"Chevrolet","modelo":"Onix","cor":"Branco"
     }

carro2=json.dumps(carros2_json)

print(carro2)
