import threading
import time
import tkinter as tk
from tkinter import ttk
import os

from pynput.mouse import Controller as mc, Listener as ml
from pynput.keyboard import Controller as kc, Listener as kl, Key

import activate
import recorder
import status
import gui
import fileloader
import config

root = tk.Tk()
root.geometry('380x170')
root.attributes("-topmost", True)
root.title("ReInput")

config.loadUserSettings()

Frame1 = tk.Frame(root)
Frame1.pack()

Frame2 = tk.Frame(root)
Frame2.pack()

greeting = tk.Label(Frame1, text="ReInput v1.0", font=("Segoe UI", 15))
greeting.pack()

### TTK Styles for Label and Buttons ###
#UI: Information Styles
s1 = ttk.Style()
s1.configure('my.TLabel', font=('Segoe UI', 10,))
s1.theme_use()

s2 = ttk.Style()
s2.configure('Bold.TLabel', font=('Segoe UI', 10, 'bold'))
s2.theme_use()

sS = ttk.Style()
sS.configure('my2.TLabel', font=('Segoe UI', 10,))
sS.theme_use()

#UI: Button Styles
s = ttk.Style()
s.configure('my.TButton', font=('Segoe UI', 10, 'bold'))
s.theme_use()

def disable_buttons():
    play['state']='disabled'
    save['state']='disabled'
    load['state']='disabled'
    settings['state']='disabled'
    record['state']='disabled'

def enable_buttons():
    play['state']='enabled'
    save['state']='enabled'
    load['state']='enabled'
    settings['state']='enabled'
    record['state']='enabled'

def update_hotkeys():
    while True:
        time.sleep(1)
        HotkeyDisplay["text"]=f"Record = {config.Configured_recordkey_temp}    |    Playback = {config.Configured_playkey_temp}"

def play_button():
    def start():
        disable_buttons()
        try:
            analysed_dict = activate.Analyser.analyse()
            run = activate.Playback(analysed_dict)
            LoadedDisplay["text"]="Playback In Progress = {0}".format(os.path.basename(status.current_filename))
            status.currently_playing = True
            run.start()
            status.playback_stop_hotkey_pressed = False
            status.currently_playing = False
            LoadedDisplay["text"]="Loaded File = {0}".format(os.path.basename(status.current_filename))
        except:
            print("Playback was attempted but not successful. Most likely no file was loaded, otherwise the file is corrupt.")
            pass
        enable_buttons()
    T1 = threading.Thread(target=start)
    T1.start()

def save_button():
    fileloader.file_to_save()

def load_button():
    fileloader.file_to_load()
    LoadedDisplay["text"] = "Loaded File = {0}".format(os.path.basename(status.current_filename))
 
def settings_button():
    global settings_window
    settings_window = gui.Settings()

def record_button():
    def initialize_recording():
        disable_buttons()
        LoadedDisplay["text"]="Recording in Progress...".format('Stopwatch')
        status.currently_recording = True
        recorder.Recorder()
        status.currently_recording = False
        enable_buttons()
        LoadedDisplay["text"]="Temporary Save = {0} ()".format(status.current_filename)
    TRecord = threading.Thread(target=initialize_recording)
    TRecord.start()

play = ttk.Button(Frame1, text="Play", width=13, command=play_button, style='my.TButton')
play.pack(side=tk.LEFT, padx=5, ipady=29)

FrameWithin = tk.Frame(Frame1)
FrameWithin.pack(side=tk.LEFT)

save = ttk.Button(FrameWithin, text="Save", width=15, command=save_button)
save.pack(side=tk.TOP, padx=5, pady=2, ipady=0)

load = ttk.Button(FrameWithin, text="Load", width=15, command=load_button)
load.pack(side = tk.TOP, padx=5, pady=3, ipady=0)

settings = ttk.Button(FrameWithin, text="Settings", width=15, command=settings_button)
settings.pack(padx=5, pady=2, ipady=0)

record = ttk.Button(Frame1, text="Record", width=13, command=record_button, style='my.TButton')
record.pack(side=tk.RIGHT, padx=5, ipady=29)

HotkeyDisplay = ttk.Label(Frame2, text="Record = {}    |    Playback = {}".format(config.Configured_recordkey_temp, config.Configured_playkey_temp), style='my.TLabel')
HotkeyDisplay.pack()

LoadedDisplay = ttk.Label(Frame2, text= "Loaded File = {}".format(status.current_filename), style='Bold.TLabel')
LoadedDisplay.pack()

def permanent_recorder(): 
    #Requires pynput 1.6.4 for normalize function. Any other version of pynput WILL NOT WORK
    #This function will be used for LISTENING TO HOTKEYS
    #This function will run alongside the GUI, as long as it is open
    #This function does not log anything to user save files
           
    print('Starting Master Keyboard Listener...')
    
    def on_release(key):
        #TODO: add something here to figure out which Hotkeys the user has set. 
        play_hotkey= "Key." + config.Configured_playkey_temp.lower()
        record_hotkey = "Key." + config.Configured_recordkey_temp.lower()

        if key == eval(play_hotkey):
            print('Hotkey for playback detected...')
            if status.currently_playing: #If currently playing, stop the playback.
                #TODO: stop the playback
                status.playback_stop_hotkey_pressed = True
            elif status.currently_recording: #If currently recording, then let the user know but do nothing.
                    print("Currently recording a script, cannot start playback right now. Use the Recording Hotkey to control recordings.")
            else: #If currently not playing or recording, then start the playback.
                play_button()
        
        elif key == eval(record_hotkey):
            print('Hotkey for recording detected...')
            if status.currently_playing: #If currently playing, let the user know but do nothing.
                print("Currently playing back a script, cannot start recording right now. The playback has to stop first, or you need to stop it.")
            elif status.currently_recording: #If currently recording, then stop the recording. Make an adjustment to make sure it activates.
                status.recorder_stop_hotkey_pressed = True
                adjust_control = mc()
                adjust_control.move(0,1)
                adjust_control.move(0,-1)
                print('Adjustment finished')
            else: #If currently not playing or recording, then start the recording.
                record_button() 
        else:
            pass

    listener = kl(on_release=on_release)
    listener.start()
    
hotkey_thread = threading.Thread(target=permanent_recorder)
hotkey_thread.start()

hotkey_updater = threading.Thread(target=update_hotkeys)
hotkey_updater.start()

menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="About", command=gui.About)
filemenu.add_separator()
filemenu.add_command(label="Preferences", command=settings_button)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)
root.mainloop()