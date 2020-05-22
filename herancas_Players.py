class NPC: #Base, PAI, Super
    def __init__(self, nome, time,  forca, municao):
        self.nome=nome
        self.time=time
        self.forca=forca
        self.municao=municao
        self.vivo=True
        self.energia=100
    def info(self):
        print(f"Nome.....: {self.nome}")
        print(f"Time.....: {self.time}")
        print(f"Forca....: {self.forca}")
        print(f"Municao..: {self.municao}")
        print(f"Vivo.....: "+ ('Sim' if self.vivo else 'Não'))
        print(f"Energia..: {self.energia}")
        print("==================================================")

class Soldado(NPC):
    def __init__(self, nome, time):
        self.forca=200
        self.municao=200
        super().__init__(nome, time,self.forca,self.municao)

class Guarda(NPC):
     def __init__(self, nome, time):
        self.forca=100
        self.municao=20
        super().__init__(nome, time,self.forca,self.municao)

class Elite(NPC):
     def __init__(self, nome, time):
        self.forca=400
        self.municao=500
        super().__init__(nome, time,self.forca,self.municao)

s1=Guarda("Olho vivo", 1)
s2=Soldado("Bala na agulha", 1)
s3=Guarda("Elite", 1)
s4=Guarda("Super Atento", 2)
s5=Guarda("Tiro certo", 2)
s6=Guarda("Samurai", 2)

s1.info()
s2.info()
s3.info()
s4.info()
s5.info()
s6.info()
