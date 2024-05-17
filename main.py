#-----------------------------------------------------------------------------
# Title: Mining RPG
# Name: Drew McGregor
# Class: CS30
# Assignment: Object-Orientated Programming: RPG - Classes
# Version: 0.1
#-----------------------------------------------------------------------------
'''
   Here is the headers docString 
   this is where you explain what the program does
'''
#-----------------------------------------------------------------------------
#-Imports and Global Variables------------------------------------------------
from tabulate import tabulate
import user_inputs as u

#-Functions ------------------------------------------------------------------


#-Main -----------------------------------------------------------------------
class Map:
    def __init__(self):
        self.layout = [['shaft', 'weak_stone', 'stone', 'stone'],
          ['shaft', 'weak_stone', 'gas_pockets', 'abandoned_shaft'], 
          ['shaft', 'damp_cave', 'flooded_cave', 'crystal_cave']]
        self.clearedrooms = [[True, False, False, False], 
                            [True, False, False, False], 
                            [True, False, False, False]]
        self.rooms = {'shaft': {'description': 'the mineshaft. '
                         + 'The shaft is the only place you can move vertically',
                         'dangers': [], 'tools': 'basic pickaxe', 'treasure': 0}, 
          'weak_stone': {'description': 'an area of weak stone. '
                         + 'You can mine through it with just a basic pickaxe. ',
                         'dangers': ['cave-in'], 'tools': 'basic pickaxe', 
                         'treasure': 1}, 
          'stone': {'description': 'an area of hardened stone. '
                      + 'You can only mine through it with an upgraded pickaxe',
                      'dangers': [], 'tools': 'upgraded pickaxe', 'treasure': 1}, 
          'gas_pockets': {'description': 'an area of weak stone. You can hear' +
                        'a hissing from somewhere close. You can mine through the                       stone with just a basic pickaxe. ',
                        'dangers': ['cave-in', 'suffocation'], 
                        'tools': 'basic pickaxe', 'treasure': 1},
          'abandoned_shaft': {'description': 'an old abandoned mineshaft. It appears deserted. ',
                            'dangers': ['unstable_floor', 'cave-in'], 
                            'tools': 'basic pickaxe', 'treasure': 3}, 
          'damp_cave': {'description': 'dimly lit cave. '
                  + 'There are puddles in low spots, '
                  + 'stalagtites and stalagmites extend from '
                  + 'the ceiling and floor. ',
          'dangers': ['slipping'], 'tools': 'basic pickaxe', 'treasure': 1},
          'crystal_cave': {'description': 'a large cave with waist '
                      + ' high water. Crystals grow from the '
                      + 'ceilings and floors. ',
          'dangers': [], 'tools': 'basic pickaxe', 'treasure': 3}, 
          'flooded_cave': {'description': 'a flooded cave. '
                      + 'You will need scuba gear to pass '
                      + 'through it. ',
          'dangers': ['drowning'], 'tools': 'scuba gear', 'treasure': 2}}

    def load(self):
        '''exports map as external file. final_msg = message print
        after function runs'''
        try:
            with open('mining_map.txt', 'w') as m:
                m.write(tabulate(self.layout, tablefmt = 'outline'))
        except:
            print('The map failed to write. ')
        else:
            print('map loaded')

    def view(self):
        '''attempts to print map'''
        try:
            with open('mining_map.txt') as m:
                print(m.read())
        except:
            print('map failed to load')
        else:
            print('you open your map')
        finally:
            print('good luck')

class Player(Map):
    def __init__(self):
        Map.__init__(self)
        self.xpos = 0
        self.ypos = 0
        self.current_room = self.layout[self.ypos][self.xpos]
        self.movement_opts = []
        self.treasure = 500
        self.inventory = ['basic pickaxe']

    def __str__(self):
        return f'''xpos: {self.xpos}
                ypos: {self.ypos}
                treasure: {self.treasure}
                inventory: {self.inventory}'''

    def update_mvmt_options(self):
        '''Modifies player['movement_options'] assuming player is at xpos, ypos'''
        self.movement_opts.clear()
        if self.xpos == 0:
            self.movement_opts.extend(['up', 'down', 'right'])
        elif self.xpos == 1 or self.xpos == 2:
            self.movement_opts.extend(['left', 'right'])
        elif self.xpos == 3:
            self.movement_opts.append('left')
        try:
            if self.ypos == 0:
                self.movement_opts.remove('up')
            elif self.ypos == 2:
                self.movement_opts.remove('down')
        except:
            pass
        try: 
             # Removing options that need correct tools. 
            if self.rooms[self.current_room]['tools'] not in self.inventory:
                self.movement_opts.remove('right')
                print('Your only option is back. You need the correct tools to progress further')
        except:
            pass

    def mine(self):
        '''Checks whether room is cleared, if not adds rooms treasure
         to player treasure. '''
        if self.clearedrooms[self.ypos][self.xpos]:
            print("There's nothing left to mine in this room")
        else:
            if self.rooms[self.current_room]['tools'] in self.inventory:
                self.treasure += self.rooms[self.current_room]['treasure']
                self.clearedrooms[self.ypos][self.xpos] = True
                print(f'You mine out the room and find {self.rooms[self.current_room]["treasure"]} treasure.')
                print(self.clearedrooms)
            else:
                print(f'''You need {self.rooms[self.layout[self.ypos][self.xpos]]['tools']} to clear this room. ''')

    def move(self):
        '''Lets a user move the player around the map'''
        self.update_mvmt_options()
        choice = u.offer_options(self.movement_opts, 
                      'Where would you like to move? ', 
                      'invalid input, please try again')
        if choice == 'up':
            self.ypos -= 1
        elif choice == 'down':
            self.ypos += 1
        elif choice == 'right':
            self.xpos += 1
        elif choice == 'left':
            self.xpos -= 1
        self.current_room = self.layout[self.ypos][self.xpos]
        print(f"""You enter {self.rooms[self.current_room]['description']}""")

    def shop(self):
        stock = ['upgraded pickaxe (3 treasure)', 'scuba gear (5 treasure)', 'cancel']
        overlap = []
        for item in stock:
            if item[:-13] in self.inventory:
                overlap.append(item)
        for item in overlap:
            stock.remove(item)
        if len(stock)-1 > 0:    
            buying = u.offer_options(stock, 'What would you like to buy? ', 'invalid input, please try again')
            if buying == 'upgraded pickaxe (3 treasure)' and self.treasure >= 3:
                self.inventory.append('upgraded pickaxe')
                self.treasure -= 3
            elif buying == 'scuba gear (5 treasure)' and self.treasure >= 5:
                self.inventory.append('scuba gear')
                self.treasure -= 5
            elif buying == 'cancel':
                print('Please return again later!')
            else:
                print(f"You only have {self.treasure} treasure. You don't have enough treasure to buy {buying},  Check out the other items or come back when you can buy {buying}")
        else:
            print('Store out of stock. ')
####################################
player = Player()
def main_options():
    '''offers player possible options'''
    choice = u.offer_options(['move', 'mine', 'view_map', 'open shop'],
                           'What would you like to do? ',
                           "That's not a valid option, try again").lower()
    if choice == 'move':
        player.move()
    elif choice == 'mine':
        player.mine()
    elif choice == 'view_map':
        player.view()
    elif choice == 'open shop':
        player.shop()


def main_menu():
    '''Essentially a main() function'''
    print('MAIN MENU\n')
    player.load()
    stop  = input('press enter to start or "q" to quit.').lower()
    while stop != '' or stop != 'q':
        if stop == '':
            print('game starting')
            while player.xpos != 3 or player.ypos != 2:
                print(player)
                main_options()
            else:
                print('You win the game! Congrats!')
                break
        elif stop == 'q':
            print('shutting down')
            break
        else:
            print('invalid input, please try again')
            stop  = input('press enter to start or "q" to quit.')
            continue

#-Main -----------------------------------------------------------------------
main_menu()