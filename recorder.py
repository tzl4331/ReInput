from pynput.keyboard import Listener as kl, Key
from pynput.mouse import Listener as ml, Controller as mc, Button
import time
import logging
import threading
import status

stop_hotkey_pressed = 0
counting = 0

def Recorder():
    #THE REASON CTRL HOTKEYS DONT WORK IS BECAUSE IT GETS SAVED AS A WINDOWS HEX KEY, SO  IT DOESNT WORK. NEED TO FIND A WAY TO FIX THIS, OR BRUTE FORCE FIX IT

    def on_keypress(key):
        logging.info('{0} {1} {2} {3}'.format(0,0, kListener._normalize(key), 'DOWN'))
        print('{0} pressed DOWN detected'.format(kListener._normalize(key)))
        #TODO: except if key pressed = hotkey, then don't log it. and this will be handled somewhere else

    def key_release(key):
        logging.info('{0} {1} {2} {3}'.format(0,0, kListener._normalize(key), 'UP'))
        print('{0} released UP detected'.format(kListener._normalize(key)))

    def removeLogging():
        logger = logging.getLogger()
        for handler in logger.handlers[:]:
            logger.removeHandler(handler)

    def on_move(x, y):
        if status.recorder_stop_hotkey_pressed == True:
            print('Attempting to stop...')
            return False
        else:
            global counting
            counting += 1

            if counting%12 == 0:
                logging.info("{0} {1} {2} {3}".format(x, y, 'CM', 'idle'))

    def on_click(x, y, button, pressed):
        if button == Button.middle:
            print("MB3 pressed")
            return False
        else:
            logging.info('{0} {1} {2} {3}'.format(x,y, button, pressed))

    
    with ml(on_move=on_move, on_click=on_click) as listener:       
        with kl(on_press=on_keypress, on_release=key_release) as kListener:
            logging.basicConfig(filename='prologbeta.maus', filemode='w', level=logging.DEBUG, force=True, format='%(relativeCreated)d %(message)s E')

            listener.join()
    
    status.recorder_stop_hotkey_pressed = False
    
    removeLogging()


