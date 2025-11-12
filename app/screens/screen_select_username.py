from app.display import (
    clear_terminal,
    letter_by_letter
)
from app.utils import (
    validate_choice
)
import re

def select_username() -> str:
    '''
    This function allows user to enter his username.
    '''
    
    letter_by_letter("Qui ose défier Georges le Malin ?!\n")
    wait_for_username: bool = True
    while wait_for_username:
        letter_by_letter("Entre ton nom : ")
        player_name: str = input().strip()
        
        # regex : at least one caracter, are allowed : "-", "_", letters and numbers
        if re.fullmatch(r"[\w-]+", player_name):
            if len(player_name) > 20:
                print("Ton nom est bien trop long ! il doit être de 20 caractères maximum !")
                continue
        else:
            print("Ton nom est invalide ! Caractères acceptés : lettres, chiffres, tirets ou underscores.")
            continue
            
        user_choice: str = validate_choice(["oui","non"], f"\nTu te nommes-tu {player_name}, c'est bien cela ?\n")

        if user_choice == "oui":
            clear_terminal()
            wait_for_username = False
            return player_name
        elif user_choice == "non":
            continue
        else:
            clear_terminal()
            wait_for_username = False
            return player_name
        