# import random

class Hero:

    def __init__(self, name, health, armor, attack):
        self.name = name
        self.health = health
        self.armor = armor
        self.attack = attack
    
    def heroName(self):
            print('Hello there brave adventurer, what is your name?')
            name = input()
            print(f"""
                  Hello {name}, welcome to Adventures in Python!!
                  In this game you take control of a lone hero and
                  Try escape the forested area from which you awoke    """)

    def armorChoice(self):
            armor = 0
            attack = 0
            print('''
                     What armor will you be using for your adventure?
                     Light = Armor 3 with Attack 8
                     Medium = Armor 5 with Attack 5
                     Heavy = Armor 10 with Attack 3
                     ''')
            res = input()
            if res == 'light':
                armor += 3
                attack += 8
                print(f'You have selected and equipped light armor, raising your armor to {armor} and your attack to {attack}!')
            elif res == 'medium':
                armor += 5
                attack += 5
                print(f'You have selected and equipped medium armor, raising your armor to {armor} and you attack to {attack}!')
            elif res == 'heavy':
                armor += 10
                attack += 3
                print(f'You have selected and equipped heavy armor, raising your armor to {armor} and your attack to {attack}!')


me = Hero('', 100, 0, 0)
me.heroName()
me.armorChoice()