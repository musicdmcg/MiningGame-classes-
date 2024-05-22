#-----------------------------------------------------------------------------
# Title: Mining RPG
# Name: Drew McGregor
# Class: CS30
# Assignment: Object-Orientated Programming: RPG - Classes
# Version: 0.3
#-----------------------------------------------------------------------------
'''
   Here is the headers docString 
   this is where you explain what the program does
'''
#-----------------------------------------------------------------------------
#-Imports and Global Variables------------------------------------------------
import random
import rooms as r
import user_inputs as u
from tabulate import tabulate
game_intro = '''Welcome to escape the mine. Find the passage out of the mine to win.'''
#-Functions ------------------------------------------------------------------


#-Main -----------------------------------------------------------------------
class Map:
    def __init__(self):
        self.layout = [[r.shaft, r.weak_stone, r.stone, r.stone],
          [r.shaft, r.weak_stone, r.gas_pockets, r.abandoned_shaft], 
          [r.shaft, r.damp_cave, r.flooded_cave, r.crystal_cave]]
        self.clearedrooms = [[True, False, False, False], 
                            [True, False, False, False], 
                            [True, False, False, False]]

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
        self.treasure = 0
        self.inventory = ['basic pickaxe']
        self.action_options = ['move', 'mine', 'view_map', 'open shop']

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
            if self.current_room.tools not in self.inventory:
                self.movement_opts.remove('right')
                print('Your only option is back. You need the '
                      + 'correct tools to progress further')
        except:
            pass

    def mine(self):
        '''Checks whether room is cleared, if not adds rooms treasure
         to player treasure. '''
        if self.clearedrooms[self.ypos][self.xpos]:
            print("There's nothing left to mine in this room")
        else:
            if self.current_room.tools in self.inventory:
                self.treasure += self.current_room.treasure
                self.clearedrooms[self.ypos][self.xpos] = True
                print(f'You mine out the room and find '
                      + f'{self.current_room.treasure} treasure.')
                print(self.clearedrooms)
            else:
                print(f'You need {self.layout[self.ypos][self.xpos].tools}'
                      + 'to clear this room. ')

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
        print(f"""You enter {self.current_room.description}""")

    def shop(self):
        stock = ['upgraded pickaxe (3 treasure)',
                 'scuba gear (5 treasure)', 'cancel']
        overlap = []
        for item in stock:
            if item[:-13] in self.inventory:
                overlap.append(item)
        for item in overlap:
            stock.remove(item)
        if len(stock)-1 > 0:    
            buying = u.offer_options(stock, 'What would you like to buy? ',
                                     'invalid input, please try again')
            if buying == 'upgraded pickaxe (3 treasure)' and (self.treasure
                                                              >= 3):
                self.inventory.append('upgraded pickaxe')
                self.treasure -= 3
            elif buying == 'scuba gear (5 treasure)' and self.treasure >= 5:
                self.inventory.append('scuba gear')
                self.treasure -= 5
            elif buying == 'cancel':
                print('Please return again later!')
            else:
                print(f"""You only have {self.treasure} treasure. You don't
                    have enough treasure to buy {buying},  Check out the
                    other items or come back when you can buy {buying}""")
        else:
            print('Store out of stock. ')


player = Player()
def main_options():
    '''offers player possible options'''
    choice = u.offer_options(player.action_options,
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
    winning_y = random.choice(range(len(player.layout)))
    print(winning_y)
    print('MAIN MENU\n')
    player.load()
    stop  = input('press enter to start or "q" to quit.').lower()
    while stop != '' or stop != 'q':
        if stop == '':
            print('game starting')
            print(game_intro)
            while player.xpos != 3 or player.ypos != winning_y:
                print(player)
                main_options()
            else:
                print(" There's a dim pocket of sunight on the other end "
                      + "of the cave. \nYou win the game! Congrats!")
        elif stop == 'q':
            print('shutting down')
            exit()
        else:
            print('invalid input, please try again')
            stop  = input('press enter to start or "q" to quit.')
            continue
#-Main -----------------------------------------------------------------------
main_menu()