import sys
import time
import os
import threading

def show_title():
    '''
    This function display game's title.
    '''
    
    print('''\033[31m
     (       )          )       (            (   (       (            (   (                       )
     ))\\ ) ( /(   (   ( /(       )\\ )   (     )\\ ))\\ )    )\\ )     (   )\\ ))\\ )     (           ( /(
     (()/( )\\())  )\\  )\\())(    (()/(   )\\   (()/(()/((  (()/(     )\\ (()/(()/((    )\\       (  )\\())
     /(_)|(_)\\ (((_)((_)\\ )\\    /(_)|(((_)(  /(_))(_))\\  /(_))  (((_) /(_))(_))\\((((_)(     )\\((_)\\
     (_))   ((_))\\___ _((_|(_)  (_))  )\\ _ )\\(_))(_))((_)(_))    )\\___(_))(_))((_))\\ _ )\\ _ ((_)_((_)
     | _ \\ / _ ((/ __| || | __| | _ \\ (_)_\\(_) _ \\_ _| __| _ \\  ((/ __|_ _/ __| __(_)_\\(_) | | \\ \\/ /
     |   /| (_) | (__| __ | _|  |  _/  / _ \\ |  _/| || _||   /   | (__ | |\\__ \\ _| / _ \\ | |_| |>  <
     |_|_\\ \\___/ \\___|_||_|___| |_|   /_/ \\_\\|_| |___|___|_|_\\    \\___|___|___/___/_/ \\_\\ \\___//_/\\_\\\
     ''')

def blinking_text(blinking_text: str, fixed_text: str, interval: float, stop_event: threading.Event):
    '''
    This function makes blinking effect on text.
    
    Params:
        - text (str): The text that should blink.
        - interval (float): The interval between each blink.
    '''
    
    # detects os system, nt stands for modern windows versions
    if os.name == 'nt':
        # init virtual windows console to detetct ANSI
        os.system('')
        
    try:
        # Tente de récupérer la taille du terminal
        columns = os.get_terminal_size().columns
    except OSError:
        # Cas de repli si la taille ne peut pas être déterminée (ex: environnement sans terminal)
        columns = full_text_length
    
    full_text_length = len(blinking_text) + len(fixed_text)
        
    padding = max(0, (columns - full_text_length) // 2)
    
    center_space = ' ' * padding
    
    print('\n')
    
    while not stop_event.is_set():
        # display text
        sys.stdout.write('\r' + center_space + blinking_text + fixed_text)
        sys.stdout.flush()
        time.sleep(interval)
        
        # hide text
        sys.stdout.write('\r' + center_space + ' ' * len(blinking_text) + fixed_text)
        sys.stdout.flush()
        time.sleep(interval)
        
    # make sure text is erased in the end
    sys.stdout.write('\r' + ' ' * (padding + len(blinking_text)) + '\n')
    sys.stdout.flush()

def clear_terminal():
    '''
    Clear terminal.
    'cls' is for Windows and 'clear' is for Linux.macOS
    '''
    os.system('cls' if os.name == 'nt' else 'clear')