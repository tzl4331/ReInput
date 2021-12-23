from pynput.keyboard import Listener as test42
from pynput.mouse import Listener as ml, Controller as mc
import time
import logging

terec = test42()

#Pynput 1.6.4 is the sweet spot! https://github.com/moses-palmer/pynput/archive/refs/tags/v1.6.4.zip


def on_keypress(key):
    logging.info('{0} {1} {2} {3}'.format(0,0, terec._normalize(key), 'DOWN'))
    print('{0} pressed DOWN'.format(BILL._normalize(key)))
    #TODO: except if key pressed = hotkey, then don't log it. and this will be handled somewhere else

def key_release(key):
    logging.info('{0} {1} {2} {3}'.format(0,0, BILL._normalize(key), 'UP'))
    print('{0} released UP'.format(BILL._normalize(key)))

with test42(on_press=on_keypress, on_release=key_release) as BILL:
    BILL.join()




