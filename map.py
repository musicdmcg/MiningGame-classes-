#-----------------------------------------------------------------------------
# Module: Map
#-----------------------------------------------------------------------------
'''Map Class.'''
#-----------------------------------------------------------------------------
#-Imports and Global Variables------------------------------------------------
import rooms as r
import user_inputs as u
from tabulate import tabulate
#-----------------------------------------------------------------------------
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