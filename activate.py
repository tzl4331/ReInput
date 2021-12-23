from pynput import mouse
from pynput.mouse import Button, Controller as mouseController, Listener as mouseListener
from pynput.keyboard import Controller as keyboardController, Listener as keyboardListener, Key
from datetime import datetime
import logging
import time
import gui, status


bill = 56
stop_hotkey_pressed = 0
counting = int(0)
number  = 0

class StartTime:
    def __init__(self):
        self.time = time.time()
    
    def getTime(self):
        return self.time


class Playback:

    def __init__(self,  dictionary): #Takes a dictionary and plays it back. Dictionary must be valid
        self.stop_number = 0
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
        
        while self.play_count < self.required_playbacks:
            for key in self.input:
                print('Working with this entry: ' + str(self.input[key]))
                if self.stop_number < 1 and status.playback_stop_hotkey_pressed == False:
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
            print('Increasing playback count by 1.')
            self.play_count+=1
        print('Resetting "stop_number" and "play_count"...')
        self.stop_number = 0
        self.play_count = 0
        print('Done. Number and Playcount reset. Ready for next activation')


class Analyser:

    #TODO: make something to test if its valid here!

    #later will make filename equal to the currently active file. for now we test on prologbeta

    def analyse():
        filename = 'prologbeta.maus'
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

'''
john = Analyser.analyse()
print(john)
jill = Playback(john)
jill.start()
print('worked')
'''
#Recorder.runListener()

'''
print("sleepin")
time.sleep(10)
Recorder.runListener()
'''

