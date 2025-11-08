import sys
import threading
from app.display import *

def main():
    '''main loop of the game'''
    
    arrow: str = "\u25B6"
    stop_blink_event = threading.Event()
    
    show_title();
    
    # thread to excute blinking action without disrupting the program
    blinking_thread = threading.Thread(
        target = blinking_text,
        args = (arrow, '  start', 0.5, stop_blink_event)
    )
    blinking_thread.start()
    
    input()
    
    stop_blink_event.set()
    
    blinking_thread.join()
    
    clear_terminal()
    
    print("prout")
    

# entry point
if __name__ == "__main__":
    main()