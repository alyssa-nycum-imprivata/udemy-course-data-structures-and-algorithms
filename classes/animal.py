class Animal:

    def __init__(self, name, species, continent):
        self.name = name
        self.species = species
        self.continent = continent

    def describe(self):
        print(f"{self.name} is a(n) {self.species} who lives in {self.continent}.")



