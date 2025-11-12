# This file contains mathematical and generic functions.
import sys
import os
from readchar import (
    key,
    readkey
)
from app.display import (
    letter_by_letter,
    clear_terminal
)

def clear_selection(number_options: int):
    '''
    This function clear and refresh the content displayed.
    '''
    
    for _ in range(number_options):
        # \x1b[1A: Move cursor up 1 line
        # \x1b[K: Erase to end of line
        sys.stdout.write('\x1b[1A\x1b[K')
    sys.stdout.flush()

if os.name == 'nt':
    os.system('') 

def validate_choice(options: list[str], start_message: str, end_message: str = ''):
    '''
    This function allow the user to choose between multiple choice.
    
    Params:
        - options (list): The choices offered to the user.
        - message (str): The message proposing choices.
    '''
    
    letter_by_letter(start_message)
    
    number_options = len(options)
    current_selection: int = 0
    key_down = key.DOWN
    key_up = key.UP
    is_run = True
    
    while is_run:
        
        for i in range(number_options):
            arrow = "\u25B6" if i == current_selection else " "
            print(f" {arrow}  {options[i]}")
        
        key_pressed = readkey()
        
        if key_pressed == key_down:
            current_selection = (current_selection + 1) % number_options
            clear_selection(number_options)
        elif key_pressed == key_up:
            current_selection = (current_selection - 1) % number_options
            clear_selection(number_options)
        else:
            press_enter()
            is_run = False
    return options[current_selection]
    
def press_enter():
    key.ENTER
            
        
    
    
    
    
    