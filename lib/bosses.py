import random 
# an array of boss enemy dictionaries
# will include boss name, helath points, and attack value

def attack():
    random.randint(2,5)
    # print(random.randint(2,5))
    random.randint(1,7)
    # print(random.randint(1,7))

boss = [{
    "name": "Orc Berserker",
    "health": 30,
    "attack": attack()
},{
    "name": "Goblin Assassin",
    "health": 24,
    "attack": 3 * 3
},{
    "name": "Ogre Captain",
    "health": 35,
    "attack": 8
}]

# attack()