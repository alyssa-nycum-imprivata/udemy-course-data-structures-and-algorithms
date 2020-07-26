from animal import Animal

class Mammal(Animal):

    def __init__(self, name, species, continent, legs):
        super().__init__(name, species, continent)
        self.legs = legs
        self.has_fur = True

    def describe_more(self):
        print(f"{self.name} is a mammal with {self.legs} legs and fur.")


kwasi = Mammal("Kwasi", "Okapi", "Africa", 4)
jade = Mammal("Jade", "Yellow Backed Duiker", "Africa", 4)
kuzco = Mammal("Kuzco", "Baird's Tapir", "Central and South America", 4)

kwasi.describe()
kwasi.describe_more()
jade.describe()
jade.describe_more()
kuzco.describe()
kuzco.describe_more()

