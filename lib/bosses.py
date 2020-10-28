import random 
# an array of boss enemy dictionaries
# will include boss name, helath points, and attack value

bosses = [{
    "name": "Orc Berserker",
    "health": 40,
    "attack": 9
},{
    "name": "Goblin Assassin",
    "health": 34,
    "attack": 4 * 3
},{
    "name": "Ogre Captain",
    "health": 45,
    "attack": 7
}]

class Boss:

    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
    
    def scan(self):
        print(f'{self.name} with {self.health} HP & {self.attack} AP')

    def fight(self):
        bHP = int(self.health)
        bAP = int(self.attack)
        bHP -= 10
        print(f'{bHP} HP')
        if bHP <= 31:
            bAP += 3
            print(bAP)
        if bAP >= 12:
            bAP -= 9
            print(f'The {self.name} has exhausted their strength and now has {bAP} AP.')
        print(f'The {self.name} now has {bHP} HP!')

me = Boss(bosses[0].setdefault('name'),bosses[0].setdefault('health'),bosses[0].setdefault('attack'))

me.scan()
me.fight()