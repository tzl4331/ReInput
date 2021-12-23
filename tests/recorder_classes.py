from pynput.keyboard import Listener as kl, Key
from pynput.mouse import Listener as ml, Controller as mc, Button
import tkinter as tk
import time
import logging
import threading
import gui, recorder, status


#Pynput 1.6.4 is the sweet spot! https://github.com/moses-palmer/pynput/archive/refs/tags/v1.6.4.zip

stop_hotkey_pressed = 0
counting = int(0)

class AlwaysOnRecord:

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('380x170')
        self.root.attributes("-topmost", True)
        self.the_gui = gui.MainApplication(self.root)

        TRecorder = threading.Thread(target=self.Recorder)
        TRecorder.start()

        self.root.mainloop()


    def Recorder(self):
        
        print('The Master Keyboard Listener has started')

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
                        abc = threading.Thread(target=self.the_gui.play_button())
                        abc.start()
                        abc.join()
                        #self.the_gui.play_button()
                    
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
                    #AlwaysOnRecord.t
                    self.the_gui.record_button()
                    pass
            else:
                pass

        listener = kl(on_release=on_release)
        listener.start()




class betaRecord:

    def Recorder():
        #THE REASON CTRL HOTKEYS DONT WORK IS BECAUSE IT GETS SAVED AS A HEXADECIMAL, SO  IT DOESNT WORK. NEED TO FIND A WAY TO FIX THIS, OR BRUTE FORCE FIX IT

        def on_keypress(key):
            logging.info('{0} {1} {2} {3}'.format(0,0, key, 'DOWN'))
            print('{0} pressed DOWN'.format(key))
            #TODO: except if key pressed = hotkey, then don't log it. and this will be handled somewhere else

        def key_release(key):
            logging.info('{0} {1} {2} {3}'.format(0,0, key, 'UP'))
            print('{0} released UP'.format(key))

        def removeLogging():
            logger = logging.getLogger()
            for handler in logger.handlers[:]:
                logger.removeHandler(handler)

        def on_move(x, y):
            if stop_hotkey_pressed == 1:
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
                
                logging.basicConfig(filename='Newprologbeta.maus', filemode='w', level=logging.DEBUG, force=True, format='%(relativeCreated)d %(message)s E')

                listener.join()
            
        removeLogging()

class Record:

    def Recorder():
        #THE REASON CTRL HOTKEYS DONT WORK IS BECAUSE IT GETS SAVED AS A HEXADECIMAL, SO  IT DOESNT WORK. NEED TO FIND A WAY TO FIX THIS, OR BRUTE FORCE FIX IT

        def on_keypress(key):
            logging.info('{0} {1} {2} {3}'.format(0,0, kListener._normalize(key), 'DOWN'))
            print('{0} pressed DOWN'.format(kListener._normalize(key)))
            #TODO: except if key pressed = hotkey, then Pass

        def key_release(key):
            logging.info('{0} {1} {2} {3}'.format(0,0, kListener._normalize(key), 'UP'))
            print('{0} released UP'.format(kListener._normalize(key)))
            #TODO: except if key pressed = hotkey, then return False (To ensure if theres input after this key, but before code runs to stop, it still wont log)

        def removeLogging():
            logger = logging.getLogger()
            for handler in logger.handlers[:]:
                logger.removeHandler(handler)

        def on_move(x, y):
            if stop_hotkey_pressed == 1:
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
                logging.basicConfig(filename='Eprologbeta.maus', filemode='w', level=logging.DEBUG, force=True, format='%(relativeCreated)d %(message)s E')

                listener.join()
            
        removeLogging()



class AlternateRecord:

    State = False
    def Recorder():
        betamaus = mc()
        
        def on_move():
            while not AlternateRecord.State:
                time.sleep(0.015)
                x, y = betamaus.position
                logging.info("{0} {1} {2} {3}".format(x, y, 'CM', 'idle'))
        TMove = threading.Thread(target=on_move)
        
        def on_keypress(key):
            logging.info('{0} {1} {2} {3}'.format(0,0, kListener._normalize(key), 'DOWN'))
            print('{0} pressed DOWN'.format(kListener._normalize(key)))
            #TODO: except if key pressed = hotkey, then don't log it. and this will be handled somewhere else

        def key_release(key):
            logging.info('{0} {1} {2} {3}'.format(0,0, kListener._normalize(key), 'UP'))
            print('{0} released UP'.format(kListener._normalize(key)))

        def removeLogging():
            logger = logging.getLogger()
            for handler in logger.handlers[:]:
                logger.removeHandler(handler)
        
        def on_click(x, y, button, pressed):
            logging.info('{0} {1} {2} {3}'.format(x,y, button, pressed))
            if button == Button.middle:
                print("MB3 pressed")
                AlternateRecord.State = True
                return False

        logging.basicConfig(filename='prologbeta.maus', filemode='w', level=logging.DEBUG, force=True, format='%(relativeCreated)d %(message)s End')
        
        with ml(on_click=on_click) as listener:
            TMove.start()
            with kl(on_press=on_keypress, on_release=key_release) as kListener:
                
                listener.join()
            
        removeLogging()
    

#john=betaRecord
#john.Recorder()
#AlternateRecord.Recorder()

