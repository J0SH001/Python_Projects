#Parent class
class Organism:
    name = "Unknown"
    species = "Unknown"
    legs = None
    arms = None
    DNA = "Sequence A"
    origin = "Unkown"
    Carbon_based = True

    def information(self):
        msg = "\nName: {}\nSpecies: {}\nLegs: {}\nArms: {}\nDNA: {}\nOrigin: {}\nCarbo Based: {}".format(self.name, self.species, self.legs, self.arms, self.DNA, self.origin, self.Carbon_based)
        return msg

# child class instance
class Human(Organism):
    name = "Gravy"
    species = "Homo"
    legs = 2
    arms = 2
    origin = "Earth"
    
    def ingenuity(self):
        msg = "\nCreates a deadly weapon using only a paperclip, chewing gum, and a roll of duct tape!"
        return msg

#another child class instance
class Dog(Organism):
    name = "Spot"
    species = "Canine"
    legs = 4
    arms = 0
    DNA = "Sequence B"
    origin = "Earth"

    def bit(self):
        msg = "\nEmits a loud menacing growl and bites down ferociously on it's target!"
        return msg

#another child class instance
class Bacterium(Organism):
    name = "X"
    species = "Bacteria"
    legs = 0
    arms = 0
    DNA = "Sequence C"
    origin = "Mars"

    def replication(self):
        msg = "\nThe cells begin to divide and multiplyinto two separate organisms!"
        return msg










if __name__ == "__main__":
    human = Human()
    print(human.information())
    print(human.ingenuity())

    dog = Dog()
    print(dog.information())
    print(dog.bit())

    bacterium = Bacterium()
    print(bacterium.information())
    print(bacterium.replication())
