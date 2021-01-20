from goblin import Goblin
from hero import Hero
from zombie import Zombie
from Character import Character
"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""

def main():
    my_hero = Hero()
    goblin = Goblin()
    zombie = Zombie()

    while goblin.alive() and my_hero.alive():
        my_hero.print_status()
        goblin.print_status()
        zombie.print_status()
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. fight zombie")
        print("4. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            # Hero attacks goblin
            my_hero.attack_goblin(goblin)
            if goblin.health <= 0:
                print("The goblin is dead.")
            # Goblin attacks hero
            else:
                goblin.attack(my_hero)
            if my_hero.health <= 0:
                print("You are dead.")
                goblin.print_status()
        elif user_input == "2":
            pass
        elif user_input == "3":
            # Hero attacks zombie
            my_hero.attack_zombie(zombie)
            if zombie.health == 0:
            # zombie attacks hero
                zombie.attack(my_hero)
            # goblin attacks hero
                goblin.attack(my_hero)
            if my_hero.health <= 0:
                print("You are dead.")
        elif user_input == "4":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

main()
