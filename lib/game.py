# import random method to use for attacks
import random
import time
# from hero import hero
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
    print('Hello there brave adventurer, what is your name?')
    name = input()
    print(f"""
                  Hello { name }, welcome to Adventures in Python!!
                  In this game you take control of a lone hero and
                  Try escape the forested area from which you awoke    """)
    time.sleep(1)
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
    """)
    print(f'Are you ready to continue {name}?')
    res = input()
    if res == 'Yes' or 'yes':
        for enemy in (trash):
            print(f"""
            A {enemy['name']} has ambushed {name}!!
            Do you want to fight or flee?
            """)
            res = input()
            if res == 'fight':
                # def fight():
                # hero_attack = roll
                values = {enemy['attack']}
                values = ''.join(map(str, {enemy['attack']}))
                enemy_attack = int(values)
                for enemy_hp in ({enemy['health']}):
                    while enemy_hp > 0:
                        # global stage
                        # print(f"==============================[STAGE {stage}]==============================")
                        enemy_hp -= hero_attack
                        print(f"""
            {name} delivers a strike to the {enemy['name']}
            The {enemy['name']} receives {hero_attack} damage!
            The {enemy['name']} has [{enemy_hp}: HP] remaining
                                """)
                    time.sleep(1)
                    global HP
                    HP -= enemy_attack
                    print(f"""
            The {enemy['name']} hits {name}
            {name} receives {enemy_attack} damage!
            {name} has [{HP}: HP] remaining!
                                """)
                    # stage += 1
                    time.sleep(1)
                    if enemy_hp <= 0:
                        print(f"{name} defeated the {enemy['name']}.")
                    if HP <= 0:
                        print(f"""
            You Lose!
            Sorry {name}, you did not escape please try again!
                                    """)
                        restart()
                    # fight()
                        # bossFight()
            elif res == 'flee':
                print(f"While deciding to flee {name} receives 5 damage!!")
                HP -= 5
                print(f'{name}\'s current HP is [{HP}: HP]!')
            else:
                print("Goodbye!")
                exit()

    # def bossFight():
        print("Press any key to continue to Boss Fight")
        input()
        print(f"""
            ==================================================================
              The {bosses[0]['name']} has emerged onto the battlefield.
              {name} did not have an opportunity to avoid the encounter,
              preparing thierself, {name} attacks the {bosses[0]['name']}!
            ==================================================================
                    """)
        print("Press any key to continue to Boss Fight")
        input()
        bHP = bosses[0]['health']
        boss_attack = bosses[0]['attack']
        while bHP > 0:
            bHP -= hero_attack
            print(
                "==============================[BOSS]==============================")
            print(
                f"""
        {name} swings thier sword and hits the {bosses[0]['name']} for {hero_attack} damage!
        The {bosses[0]['name']} has [{bHP}: HP] remaining!
                    """)
            print(time.sleep(2))
            HP -= boss_attack
            print(f"""
        The {bosses[0]['name']}, delivers a powerful blow to {name}!
        {name} takes {boss_attack} damage from the {bosses[0]['name']}!
        {name} has [{HP}: HP] remaining!""")
            time.sleep(2)
            if bHP <= 0 and HP > 0:
                print(f"""
        {name} has defeated the deadly {bosses[0]['name']}!
        Congratulations, you defeated the {bosses[0]['name']} and escaped the Dark Forest!
                        """)
                print('''Would you like to play again?
                            Yes or No?''')
            elif HP <= 0:
                print(f"""
            You Lose!
            Sorry {name}, you did not escape please try again!
                        """)
                return restart()


def restart():
    print('''Would you like to play again?
                Yes or No?''')
    res = input()
    if res == 'Yes' or 'yes':
        start()
        restart()
    elif res == 'No' or 'no':
        print('Please come back soon!')

# print(trash)
global HP
HP = 50
global roll
roll = random.randint(4, 9)
global hero_attack
hero_attack = roll

start()
