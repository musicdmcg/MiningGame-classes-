#-----------------------------------------------------------------------------
# Module: User Inputs
#-----------------------------------------------------------------------------
'''User input Functions'''
# Imports and Global Variables------------------------------------------------
#-Functions-------------------------------------------------------------------
def get_YesNo(msg, error_msg):
    '''Asks user yes no question, outputs true for yes, false for no.
    msg = yes/no question'''
    answer = input(msg).lower()
    if answer == 'yes' or answer == 'y':
        return True
    elif answer == 'no' or answer == 'n':
        return False
    else:
        print(error_msg)
        get_YesNo(msg, error_msg)


def get_choice(valid_inputs, msg, error_msg):
    ''' asks user question until a valid input is given, presenting error
    msg on bad input
    valid_inputs = list of valid items
    msg = message given to user on run
    error_msg = msg on bad input
    '''
    choice = input(msg).lower()
    if choice == 'q':
        if get_YesNo('Are you sure you want to quit?', 
                     'The only valid otions are yes or no'):
            raise Exception('Game ended')
        else:
            choice = get_choice(valid_inputs, msg, error_msg)
    if choice not in valid_inputs:
        print(error_msg)
        choice = get_choice(valid_inputs, msg, error_msg)
    return choice


def offer_options(original_options, msg, error_msg):
    """Assign and print numerical values to items in a list"""
    print('\n')
    for item in original_options:
        print(f"{original_options.index(item)+1}. {item}")
    numbers = [str(number+1) for number in range(len(original_options))]
    full_options = original_options.copy()
    full_options.extend(numbers)
    choice = get_choice(full_options, msg, error_msg)
    if choice not in full_options:
        print(error_msg)
        choice = get_choice(full_options, msg, error_msg)
    elif choice.isnumeric():
        choice = full_options[int(choice)-1]
    return choice