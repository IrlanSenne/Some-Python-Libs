import re

texto="Cálculo binário painel NASA"

# pesq=input("Search : ")

# res=re.findall(pesq, texto)
# res=re.search(pesq, texto)
# res=re.split("\s", texto)
res=re.sub("\s","#", texto)
"""
print(res)
print(len(res))

print(res.start())
print(res.end())
"""

print(res)