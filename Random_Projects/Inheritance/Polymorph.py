#Parent Class
class Witch:
    height = "4.9\'"
    aesthetic = "Large nose with mole"

    def Alchemy():
        text = "\nCooking done poorly."
        return text

#Polymorphed child class
class Daughter_of_witch(Witch):
    age = 14
    education = "Homeschooled"
    height = "4.8\'"
    aesthetic = "Slightly smaller nose with the same mole"

    def Alchemy():
        text = "\nScience class."
        return text

#Polymorphed child class
class Mother_of_witch(Witch):
    memory = "All but gone"
    Alzheimers = True
    height = "4.2\'"
    aesthetic = "Cartoonishly large nose with no mole"

    def Alchemy():
        text = "\nNo one values the old traditions nowadays."
        return text
