from pynput import mouse
from pynput.mouse import Button, Controller as mouseController, Listener as mouseListener
from pynput.keyboard import Controller as keyboardController, Listener as keyboardListener, Key
from datetime import datetime
import logging
import time
import gui, status
import config


class Playback:

    def __init__(self,  dictionary): #Takes a dictionary and plays it back. Dictionary must be valid
        self.play_count = 0
        self.required_playbacks = 1
        self.dicty = dictionary
        self.request_stop = False
    #Make  this place store the variables like number and shit. Then make the start() use these values. so it doesnt have a unboundlocalerror
    
    def start(self):
        maus = mouseController()
        kb = keyboardController()
        
        self.input = self.dicty

        def parse_boolean(b):
            return b == "True"
        
        required_playbacks = config.loopingPlaybacks()
        plays = 0
        while plays < required_playbacks:
            print('Increasing playback count by 1.')
            plays+=1
            print(status.number < 1 and (status.playback_stop_hotkey_pressed == False))
            for key in self.input:
                print('Working with this entry: ' + str(self.input[key]))
                if status.number < 1 and (status.playback_stop_hotkey_pressed == False):
                    if self.input[key]['whichButton'] == 'Button.middle':
                        pass
                    else:
                        if self.input[key]['whichButton'] == 'CM' or (self.input[key]['whichButton'] == 'Button.left' or self.input[key]['whichButton'] == 'Button.right'):
                                time.sleep(self.input[key]['delay'] / 1000)
                                
                                #Relocates cursor to destination
                                maus.position=(self.input[key]['x'], self.input[key]['y'])
            
                                #Determines whether to Left click or Right click, using the analysed data
                                if parse_boolean(self.input[key]['press']):
                                    if self.input[key]['whichButton'] == 'Button.left':
                                        maus.press(Button.left)
                                    elif self.input[key]['whichButton'] == 'Button.right':
                                        maus.press(Button.right)
                                else:
                                    if self.input[key]['whichButton'] == 'Button.left':
                                        maus.release(Button.left)
                                    elif self.input[key]['whichButton'] == 'Button.right':
                                        maus.release(Button.right)
                        else:
                            #KEYBOARD INPUTS
                                #Makes the timing between clicks and mouse movements equal to the User recording's timing.
                            time.sleep(self.input[key]['delay'] / 1000)
                            
                            #Determines whether to press Down or Up on a key, using the analysed data
                            if self.input[key]['press'] == 'DOWN':
                                try:
                                    buttontopress = self.input[key]['whichButton']
                                    print(buttontopress)
                                    #In pynput, non alphanumeric keys are formatted as Key.enter, Key.esc, Key.shift etc..., so check for this so they can be activated properly
                                    if self.input[key]['whichButton'][0:3] == 'Key':
                                        
                                        if (self.input[key]['whichButton'] == 'Key.ctrl_l') or (self.input[key]['whichButton'] == 'Key.ctrl_r'):
                                            kb.press(Key.ctrl)
                                        else:
                                            kb.press(eval(buttontopress))
                                    
                                    else:
                                        kb.press(buttontopress[1:-1])
                                except Exception as e: 
                                    print(e)
                            elif self.input[key]['press'] == 'UP':
                                try:
                                    buttontopress = self.input[key]['whichButton']
                                    if self.input[key]['whichButton'][0:3] == 'Key':
                                        
                                        if (self.input[key]['whichButton'] == 'Key.ctrl_l') or (self.input[key]['whichButton'] == 'Key.ctrl_r'):
                                            kb.release(Key.ctrl)
                                        else:
                                            kb.release(eval(buttontopress))
                                    else:
                                        kb.release(buttontopress[1:-1])
                                except Exception as e: 
                                    print(e)
                else:
                    break
            if status.playback_stop_hotkey_pressed == True:
                print('Massively increasing the play counter to stop playback')
                plays+=99999999999999999999
    
        print('Resetting "status.number" and "plays"...')
        status.number = 0
        plays = 0
        print('Done. Number and Playcount reset. Ready for next activation')


class Analyser:

    #TODO: make something to test if its valid here!

    #later will make filename equal to the currently active file. for now we test on prologbeta

    def analyse():
        filename = status.current_filename
        count = 0

        with open(filename, 'r') as f:
            first_line = f.readline()
            initial_time = first_line.split()[0]
            
            click_history = {}

            for line in f:
                count += 1

                (timestamp, posx, posy, buttonName, press, End) = line.split(' ')

                if count > 1:
                    delay = float(timestamp) - click_history[count-1]['timestamp']
                else:
                    delay = 0
                
                click_history[count] = {'delay':float(delay), 'whichButton':buttonName, 'x':int(posx), 'y':int(posy), 'timestamp':float(timestamp), 'press':press,}
        
            return click_history
    
    def validcheck(userfile):
        count = 0 

        with open(userfile, 'r') as f:
            #Reads the first line to see the Initial Starting Time
            first_line = f.readline()
            initial_time = first_line.split()[0]
            temp_click_history = {}

            for line in f:
                count+=1
                (timestamp, posx, posy, buttonName, press, End) = line.split(' ')
                #For each line after the first, the delay will be the Difference in Recorded Time between the current and previous line. First line delay is fixed 0.5 for smoothness.
                if count > 1:
                    Delay = float(timestamp) - temp_click_history[count - 1]['timestamp']
                else:
                    Delay = 0
                #Adds a dictionary entry for each line in the Text File
                temp_click_history[count] = {'delay':float(Delay), 'whichButton':buttonName, 'x':int(posx), 'y':int(posy), 'timestamp':float(timestamp), 'press':press,}
        print(temp_click_history)




