from Character import Character

class Zombie(Character):
    def __init__(self, health = 0, power = 2):
        self.health = health
        self.power = power

    def print_status(self):
        print(f"The zombie has {self.health} health and {self.power} power.")

    def attack(self, hero):
        hero.health -= self.power
        print(f"The zombie does {self.power} damage to you.")
