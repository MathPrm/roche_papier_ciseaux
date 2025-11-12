from app.display import (
    clear_terminal
)
from app.utils import (
    press_enter
)
from app.screens.screen_title import (show_screen_title)
from app.screens.screen_select_username import (select_username)
from app.screens.screen_select_attack import (player_choose_attack)

def main():
    '''main loop of the game'''

    # starting screen
    show_screen_title()
    
    press_enter()
    clear_terminal()

    # select username screen
    player_name = select_username()
    
    press_enter()
    
    # select attack screen
    player_choose_attack(player_name)
    
   
        


# entry point
if __name__ == "__main__":
    main()