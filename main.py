#-----------------------------------------------------------------------------
# Title: Mining RPG
# Name: Drew McGregor
# Class: CS30
# Assignment: Object-Orientated Programming: RPG - Classes
# Version: 0.5
#-----------------------------------------------------------------------------
'''
   Game with the goal of 'escaping the mine' Exit floor is is randomized.
'''
#-----------------------------------------------------------------------------
#-Imports and Global Variables------------------------------------------------
import random
import player as p
import user_inputs as u
game_intro = ('Welcome to escape the mine. Find the passage out of the mine'
            + ' to win.')
player = p.Player()
#-Functions ------------------------------------------------------------------
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
    '''Essentially a main() function, controls start and end of game'''
    winning_y = random.choice(range(len(player.layout)))
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
                print(" There's a dim pocket of sunight on the other end"
                      + " of the cave. \nYou win the game! Congrats!")
                exit()
        elif stop == 'q':
            print('shutting down')
            exit()
        else:
            print('invalid input, please try again')
            stop  = input('press enter to start or "q" to quit.')
            continue


#-Main -----------------------------------------------------------------------
main_menu()