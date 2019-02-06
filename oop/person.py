class Person:
    def __init__(self, cognome, nome, eta):
        self.cognome = cognome
        self.nome = nome
        self.eta = eta

    def display(self):
        print(f"\nHi, my name is {self.cognome} {self.nome} and I'm {self.eta} years old")
    
p1 = Person("Rossi","Pippo",25)
p1.display()