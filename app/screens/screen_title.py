from app.display import (
    show_title,
    blinking_text
)
import threading

def show_screen_title():
    '''
    This function shows the starting  screen.
    '''
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