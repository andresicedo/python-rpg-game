from Character import Character
import random
class Hero(Character):
    def __init__(self, health = 10, power = 5):
        self.health = health
        self.power = power

    def attack_goblin(self, goblin):
        goblin.health -= self.power
        print(f"You do {self.power} damage to the goblin.")
    
    def spec_atk(self, goblin):
        number = random.randint(0,6)
        if number == 1:
            goblin.health -= (self.power * 2)
            print(f"You did {self.power * 2} damage to the goblin.")
        else:
            goblin.health -= 0
            print("Your special attack missed! You did 0 damage!")

    def attack_zombie(self, zombie):
        zombie.health -= 0
        print(f"You do 0 damage to the zombie.")

    def print_status(self):
        print("You have %d health and %d power." % (self.health, self.power))
