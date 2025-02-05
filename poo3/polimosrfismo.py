class Animal:
    def __init__(self, nome):
        self.nome = nome
    def som(self):
        return "Som de animal genérico"

class Mamifero (Animal):
    def som(self):
        return "Som de mamífero"

class Ave(Animal):
    def som(self):
        return "Som de ave"

class Cachorro (Mamifero):
    def som(self):
        return "Latido"

class Gato (Mamifero):
    def som(self):
        return "Miado"

class Papagaio (Ave):
    def som(self):
        return "Fala"

# Criando instâncias das classes
animais = [
    Cachorro ("Rex"),
    Gato ("Mia"),
    Papagaio ("Louro")
]

# Exibindo os sons dos animais
for animal in animais:
    print(f" {animal.nome}: {animal.som()}")

def descrever_som(animal):
    print(f"{animal.nome} faz: {animal.som()}")

# Usando a função para exibir os sons
for animal in animais:
    descrever_som(animal)