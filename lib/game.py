# import random method to use for attacks
import random
from hero import hero
from monsters import trash
from bosses import bosses


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
    random.shuffle(trash)
    random.shuffle(bosses)
    roll = random.randint(4, 8)
    print('Hello there brave adventurer, what is your name?')
    name = input()
    print(f"""
        =========================================================================================
        || INSTRUCTIONS:                                                                       ||
        || The objective is to defeat all five enemies plus one boss enemy.                    ||
        || Your hero has Health Points (HP) that diminish when receiving attacks.              ||
        || Your HP will be displayed after the start of your adventure and before every fight. ||
        || You will be asked to fight or flee before every fight, excluding the boss fight.    ||
        || Fighting will commence the fight between you and the enemy.                         ||
        || Attacks will be entered with "Hit/hit" and will do random damage to an enemy.       ||
        || Fleeing will cause you to avoid the fight at the cost of 7 HP.                      ||
        || VICTORY: You defeat all five enemies and the boss.                                  ||
        || DEFEAT: You lose all of your HP.                                                    ||
        =========================================================================================                  
        ||                 Hello { name }, welcome to Adventures in Python!!                   ||
        ||                 In this game you take control of a lone hero and                    ||
        ||                 Try escape the forested area from which you awoke                   ||
        =========================================================================================
    """)
    print(f'Are you ready to continue {name}?')
    res = input()
    if (res == 'Yes' or res == 'yes'):
        for enemy in (trash):
            print(f"You have encountered the {enemy['name']}")
            print(f"Do you want to fight or flee?")
            res = input()
            if (res == 'Fight' or 'fight'):
                # eHP = {enemy['health']}
                # print(eHP)
                hero_attack = roll
                print(hero_attack)
                values = {enemy['attack']}
                values = ''.join(map(str, {enemy['attack']}))
                enemy_attack = int(values)
                print(enemy_attack)
                for enemy_hp in ({enemy['health']}):
                    print({enemy['health']})
                    print(enemy_hp, '->', enemy_hp)
                    while enemy_hp > 0:
                        enemy_hp -= hero_attack
                        print(enemy_hp)
                        print(f"{hero_attack} // {enemy_hp}")
                        print(
                            f"The {enemy['name']} has [{enemy_hp}: HP] remaining!")
                        global HP
                        HP -= enemy_attack
                        print(f"{name}, you have [{HP}: HP] remaining!")
                        if enemy_hp <= 0:
                            print(f"{name} defeated the {enemy['name']}.")
            elif (res == "Flee" or res == 'flee'):
                print('lose')
                HP -= 5
                print(f'Your current HP is [{HP}: HP]!')
        for boss in (bosses):
            print(f"{boss}")
            print(f"{bosses}")
            print(f""" The {boss['name']} has emerged onto the battlefield.
                       {name} did not have the opportunity to avoid the encounter,
                       preparing thierself, {name} attacks the {boss['name']}! """)
            print("===================================================================")
            bHP = {boss['health']}
            print(bHP)
            boss_attack = {boss['health']}
            print(boss_attack)
            while bHP > 0:
                bHP -= hero_attack
                print(
                    f"{name} swings thier sword and hits the {boss['name']} for {hero_attack} damage!")
                HP -= boss_attack
                print(f"""The {boss['name']}, delivers a powerful blow to {name}!
                          {name} takes {boss_attack} damage from the {boss['name']}!
                          {name} has [{HP}: HP] remaining!""")
                if bHP <= 0:
                    print(f"{name} has defeated the deadly {boss['name']}!")

                    def restart():
                        print(
                            f"Congratulations, you defeated the {boss['name']} and escaped the Dark Forest!")
                        print('''Would you like to play again? 
                        Yes or No?''')
                        res = input()
                        if res == 'Yes' or 'yes':
                            start()
                            restart()
                        else:
                            print('Please come back soon!')
    else:
        print(f'Farewell {name}, see you soon!')


global HP
HP = 50

start()
