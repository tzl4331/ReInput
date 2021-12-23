import tkinter as tk
from pynput.mouse import Controller as mc, Listener as ml
from pynput.keyboard import Controller as kc, Listener as kl, Key
from tkinter import ttk, messagebox
import activate, recorder, status, functions, gui
import threading
import time

root = tk.Tk()
root.geometry('380x170')
root.attributes("-topmost", True)
root.title("maus48 Pro Version")


Frame1 = tk.Frame(root)
Frame1.pack()

Frame2 = tk.Frame(root)
Frame2.pack()

greeting = tk.Label(Frame1, text="maus48 Pro Version v0.0", font=("Segoe UI", 15))
greeting.pack()
        
def play_button():
        analysed_dict = activate.Analyser.analyse()
        run = activate.Playback(analysed_dict)
        
        #TODO: add a new keyboard lister to activate/stop the thread when the hotkeys are pressed 
        #TODO: block all buttons if recording or playback

        def start_playback():
            status.currently_playing = True
            run.start()
        
        start_thread = threading.Thread(target=start_playback)
        start_thread.start()
        start_thread.join()
        
        status.playback_stop_hotkey_pressed = False

        status.currently_playing = False

def save_button():
    pass

def load_button():
    pass

def settings_button():

    settingsUI = tk.Toplevel()
    settingsUI.geometry("1000x800")
    settingsUI.title('Settings')
    settings_gui = gui.Settings(settingsUI)

def record_button():
    
    def initialize_recording():
        play['state']='disabled'
        save['state']='disabled'
        load['state']='disabled'
        settings['state']='disabled'
        record['state']='disabled'

        status.currently_recording = True
        recorder.Recorder()

        status.currently_recording = False

        play['state']='enabled'
        save['state']='enabled'
        load['state']='enabled'
        settings['state']='enabled'
        record['state']='enabled'
    
    TRecord = threading.Thread(target=initialize_recording)
    TRecord.start()


play = ttk.Button(Frame1, text="Play", width=13, command=play_button)
play.pack(side=tk.LEFT, padx=5, ipady=29)

FrameWithin = tk.Frame(Frame1)
FrameWithin.pack(side=tk.LEFT)

save = ttk.Button(FrameWithin, text="Save", width=15, command=save_button)
save.pack(side=tk.TOP, padx=5, pady=2, ipady=0)

load = ttk.Button(FrameWithin, text="Load", width=15, command=load_button)
load.pack(side = tk.TOP, padx=5, pady=3, ipady=0)

settings = ttk.Button(FrameWithin, text="Settings", width=15, command=settings_button)
settings.pack(padx=5, pady=2, ipady=0)

record = ttk.Button(Frame1, text="Record", width=13, command=record_button)
record.pack(side=tk.RIGHT, padx=5, ipady=29)

HotkeyDisplay = ttk.Label(Frame2, text="Record = HK   |   Playback = HK")
HotkeyDisplay.pack()

LoadedDisplay = ttk.Label(Frame2, text= "Loaded File = XYZ")
LoadedDisplay.pack()



def PermanentRecorder(): 
    #Requires pynput 1.6.4 for normalize function
    #This function will be used for LISTENING TO HOTKEYS
           
    print('Starting Master Keyboard Listener...')

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
                    time.sleep(0.1)
                    play_button()

                
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
                record_button()
                
        else:
            pass

    listener = kl(on_release=on_release)
    listener.start()
    

hotkey_thread = threading.Thread(target=PermanentRecorder())
hotkey_thread.start()


root.mainloop()