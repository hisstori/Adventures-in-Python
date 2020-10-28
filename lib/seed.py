from main import *

# Tables saving monster information name/health/attack.

imp_scout = Trash(name='Imp Scout', health=2, attack=1).save()
goblin_scout = Trash(name='Goblin Scout', health=4, attack=1).save()
goblin_thug = Trash(name='Goblin Thug', health=5, attack=2).save()
goblin_archer = Trash(name='Goblin Archer', health=5, attack=6).save()
goblin_warrior = Trash(name='Gobline Warrior', health=10, attack=3).save()
giant_spider = Trash(name='Giant Spider', health=8, attack=5).save()

# Tables saving boss information name/health/attack.
orc_berserker = Boss(name='Orc Berserker', health=40, attack=9).save()
goblin_assassin = Boss(name='Goblin Assassin', health=40, attack=12).save()
orge_captain = Boss(name='Ogre Captain', health=45, attack=7).save()