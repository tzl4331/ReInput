from pynput.keyboard import Listener as kl, Key
from pynput.mouse import Listener as ml, Controller as mc, Button
import time
import logging
import threading
import status


counting = 0

def Recorder():
    #Requires pynput 1.6.4 for normalize function
    #This function will be used for RECORDING

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


def PermanentRecorder():        
    print('Starting Master Keyboard Listener')

    def on_press(key):
        print('MENU Listener: {} pressed.'.format(listener._normalize(key)))
    
    def on_release(key):
        #TODO: add something here to figure out which Hotkeys the user has set. 
        #playKeyCombo = "keyboard.Key." + SETTINGS.Configured_playkey_temp.lower()
        #recordKeyCombo = "keyboard.Key." + SETTINGS.Configured_recordkey_temp.lower()

        #if key == eval(play_hotkey):
        if key == eval("Key.f12"):
            print('Hotkey for playback detected...')
            if status.currently_playing:
                #TODO: stop the playback
                status.playback_stop_hotkey_pressed = True
            else:
                if status.currently_recording:
                    print("Currently recording a script, cannot start playback right now. Use the Recording Hotkey to control recordings.")
                    pass
                else: # start the playback
 
                    pass
                
            #Do something here.
        elif key == eval("Key.f8"):
            print('Hotkey for recording detected')
            if status.currently_playing:
                "Currently playing back a script, cannot start recording right now. The playback has to stop first, or you need to stop it."
                pass
            elif status.currently_recording:
                #TODO: stop the recording
                status.recorder_stop_hotkey_pressed = True
                adjustment = mc()
                adjustment.move(0,1)
                adjustment.move(0,-1)
            else:
                #TODO: start the recording

                pass
        else:
            pass

    listener = kl(on_release=on_release)
    listener.start()
    