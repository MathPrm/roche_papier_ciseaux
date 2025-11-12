from app.display import (
    clear_terminal,
    letter_by_letter
)
from app.utils import (
    validate_choice,
    press_enter
)
import re

def select_username():
    '''
    This function allows user to enter his username.
    '''
    
    letter_by_letter("Qui ose défier Georges le Malin ?!\n")
    wait_for_username = True
    while wait_for_username:
        letter_by_letter("Entres ton nom : ")
        player_name = input().strip()
        
        if re.fullmatch(r"[\w-]+", player_name):
            if len(player_name) > 20:
                print("Ton nom est bien trop long ! il doit être de 20 caractères maximum !")
                continue
        else:
            print("Ton nom est invalide ! Caractères acceptés : lettres, chiffres, tirets ou underscores.")
        wait_for_username = False
            
        user_choice = validate_choice(["oui","non"], f"\nTu te nommes-tu {player_name}, c'est bien cela ?\n")
        print(user_choice)
        if user_choice == "oui":
            clear_terminal()
        else:
            clear_terminal()
            select_username()