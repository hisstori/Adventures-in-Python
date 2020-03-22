# import random method to use for attacks
import random
from hero import hero
from monsters import trash
from bosses import boss


# TODO G create welcome landing as table of contents with more info
# TODO G create an input to take you to an instructions script
# TODO S create an input to start the game
# start of the adventure
# shuffles trash(weak) enemies
# shuffles boss(strong) enemies
# this variable will hold the hero total health points
# welcome user to game and ask them to input thier name
# URGENT welcome user and describe here how the health and attack systems play out
# TODO S ask user to select hero armor:  light, medium, heavy
# TODO S armor type will determine health points (HP)
# accept user name and use that name for remainder of game
# TODO S user will select a weapon type: sword, dagger, hammer
# TODO S weapon type will determine power/number of attacks
# user moves forward with adventure and encounters monster
# user will choose to fight or flee, if fight attack(), else lose -7 Health Points (HP)
# user will continue to fight through four stages making fight or flee decision
# user will encounter one of three boss enemies
# user HAS to fight the BOSS there will be no flee
# game is won once user defeats boss
# game is lost if user loses all health points
# give user the option to restart the game from the beginning

def start():
    HP = 50
    random.shuffle(trash)
    random.shuffle(boss)
    print('Hello there brave adventurer, what is your name?')
    name = input()
    print(f'''
        =========================================================================================
        || INSTRUCTIONS:                                                                       ||
        || The objective is to defeat all five enemies plus one boss enemy.                    ||
        || Your hero has Health Points (HP) that diminish when receiving attacks.              ||
        || Your HP will be displayed after the start of your adventure and before every fight. ||
        || You will be asked to fight or flee before every fight, excluding the boss fight.    ||
        || Fighting will commence the fight between you and the enemy.                         ||
        || Attacks will be entered with "Hit/hit" and will do random damage to an enemy.       ||
        || Fleeing will cause you to avoid the fight at the cost of 7 HP.                      ||
        || VICTORY if you defeat all five enemies and the boss.                                ||
        || DEFEAT if you lose all of your HP.                                                  ||
        =========================================================================================
        =========================================================================================                   
        ||                  Hello {name}, welcome to Adventures in Python!                   ||
        ||                    In this game you take control of a lone hero                     ||
        ||                 Try escape the forested area from which you awoke                   ||
        =========================================================================================
    ''')
    print(f'Are you ready to continue {name}?')
    input()
    if (input == 'Yes' or input == 'yes'):
        for enemy in (trash):
            print(f"You have encountered {enemy['name']}")
            print(f"Do you want to fight or flee?")
            input()
        if (input == 'Fight' or input == 'fight'):
            fight()
        else:
            (HP - 5)
            print(f'Your current HP is {HP}!')
    else:
        print(f'Farewell {name}, see you soon!')


    def fight():
        hero_attack = (random.randint(4,8))
        enemy_attack = ({enemy['attack']})
        while {enemy['health']} >= 0:
            hero_attack - ({enemy['health']})
            enemy_attack - ({HP})
        else:
            return




start()
