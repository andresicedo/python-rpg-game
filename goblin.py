from Character import Character
class Goblin(Character):
    def __init__(self, health = 6, power = 2):
        self.health = health
        self.power = power

    def print_status(self):
        print("The goblin has %d health and %d power." % (self.health, self.power))

    def attack(self, hero):
        hero.health -= self.power
        print("The goblin does %d damage to you." % self.power)
    