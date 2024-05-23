#-----------------------------------------------------------------------------
# Module: Player
#-----------------------------------------------------------------------------
'''Player Class (child of map class in map.py)'''
#-----------------------------------------------------------------------------
#-Imports and Global Variables------------------------------------------------
import map as m
import user_inputs as u
from tabulate import tabulate
#-Main -----------------------------------------------------------------------
class Player(m.Map):
    def __init__(self):
        m.Map.__init__(self)
        self.xpos = 0
        self.ypos = 0
        self.current_room = self.layout[self.ypos][self.xpos]
        self.movement_opts = []
        self.treasure = 0
        self.inventory = ['basic pickaxe']
        self.action_options = ['move', 'mine', 'view_map', 'open shop']

    def __str__(self):
        return tabulate([['xpos', self.xpos], ['ypos', self.ypos], 
    ['treasure', self.treasure], ['inventory', self.inventory]])

    def update_mvmt_options(self):
        '''Updates player.movement_opts to players position'''
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
        # Removing progression option if missing required tools. 
        if self.current_room.tools not in self.inventory:
            self.movement_opts.remove('right')
            print('Your only option is back. You need the '
                  + 'correct tools to progress further')

    def mine(self):
        '''Checks whether room is cleared, if not adds rooms treasure
         to player treasure. '''
        if self.clearedrooms[self.ypos][self.xpos]:
            print("There's nothing left to mine in this room")
        else:
            if self.current_room.tools in self.inventory:
                self.treasure += self.current_room.treasure
                self.clearedrooms[self.ypos][self.xpos] = True
                print('You mine out the room and find '
                      + f'{self.current_room.treasure} treasure.')
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
        print(f'You enter {self.current_room.description}')

    def shop(self):
        stock = ['upgraded pickaxe (3 treasure)',
                 'scuba gear (5 treasure)', 'cancel']
        # Removes item from store if player has it.
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