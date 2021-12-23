import tkinter as tk
from tkinter import ttk, messagebox
import activate, recorder, status
import threading, gui


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
    import main

    def initialize_recording():
        main.play['state']='disabled'
        main.save['state']='disabled'
        main.load['state']='disabled'
        main.settings['state']='disabled'
        main.record['state']='disabled'

        status.currently_recording = True
        recorder.Recorder()

        status.currently_recording = False

        main.play['state']='enabled'
        main.save['state']='enabled'
        main.load['state']='enabled'
        main.settings['state']='enabled'
        main.record['state']='enabled'
    
    initialize_recording()
