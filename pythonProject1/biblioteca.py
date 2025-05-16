class Atleta():
    def __init__(self, nome, idade, peso):
        self.nome=nome
        self.peso=peso
        self.idade=idade
        self.aposentado=False
        self.aquecer = False


    def apresentar(self):
        print(f" Olá! Meu nome é {self.nome}, tenho {self.idade} anos.\n Hoje em dia estou acima do peso, pesando {self.peso} quilos e ando precisando me aquecer.")
    def aposentar(self):
        print(f"O atleta {self.nome} está {self.aposentado}")
    def aquecer(self):
      if self.aposentado:
          print(f"{self.nome} está aposentado(a) e não pode mais aquecer")
      else:
          self.aquecido = True
          print(f"{self.nome} está aquecido(a).")
    def aposentar(self):
        self.aposentado=True
        print(f"{self.nome} se aposentou ")


class Corredor(Atleta):
    def __init__(self,nome,idade,peso):
        super().__init__(nome,idade,peso)
    def correr(self):
            if self.aposentado:
                print(f"{self.nome} está aposentado e não pode mais correr")
            elif not self.aquecido:
                print(f"{self.nome} precisa se aquecer para poder correr")
            else:
                print(f"{self.nome} está correndo")

class Nadador(Atleta):
    def __init__(self,nome,idade,peso):
        super().__init__(nome,idade,peso)
    def nadar(self):
        if self.aposentado:
            print(f"{self.nome} não pode nadar porque está aposentado")
        elif not self.aquecido:
            print(f"{self.nome} precisa se aquecer antes de nadar")
        else:
            print(f"{self.nome} está nadando")

class Ciclista(Atleta):
    def __init__(self, nome, idade, peso):
        super().__init__(nome, idade, peso)
    def pedalar(self):
        if self.aposentado:
            print(f"{self.nome} não pode pedalar porque está aposentado")
        elif not self.aquecido:
            print(f"{self.nome} precisa se aquecer antes de pedalar.")
        else:
            print(f"{self.nome} está pedalando.")

class TriAtleta(Corredor, Nadador, Ciclista):
    def __init__(self, nome, idade, peso):
        super().__init__(nome, idade, peso)
    def competir(self):
        if self.aposentado:
            print(f"{self.nome} não pode competir porque está aposentado.")
        elif not self.aquecido:
            print(f"{self.nome} precisa se aquecer antes de competir.")
        else:
            print(f"{self.nome} está competindo em um triatlo!")






