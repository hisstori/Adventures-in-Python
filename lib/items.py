# import random
# a list of items containing items

class Item:

    def __init__(self, name):
        self.name = name
        # self.value = value

    def hPot(self):
        hPot = 15
        print(f'{self.name} restored {hPot} HP!')
        print(f'You now have {hPot}!')
    
    def pPot(self):
        pPot = 3
        print(f'{pPot}')

    def elix(self):
        elix = 15
        print(f'{elix}')

# test = Item('Health Potion')
# test = Item('Power Potion')
# test = Item('Elixer')
# test.hPot()
# test.pPot()
# test.elix()
