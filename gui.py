import tkinter as tk
from tkinter import ttk, messagebox
import activate, recorder, status
import threading

currently_playing = False
currently_recording = False

request_play_stop = False
request_record_stop = False

class MainApplication():
    def __init__(self, master):
        self.master = master
        master.title("maus48 Pro Version")

        self.Frame1 = tk.Frame(master)
        self.Frame1.pack()

        self.Frame2 = tk.Frame(master)
        self.Frame2.pack()

        self.greeting = tk.Label(self.Frame1, text="maus48 Pro Version v0.0", font=("Segoe UI", 15))
        self.greeting.pack()

        

        self.play = ttk.Button(self.Frame1, text="Play", width=13, command=self.play_button)
        self.play.pack(side=tk.LEFT, padx=5, ipady=29)

        self.FrameWithin = tk.Frame(self.Frame1)
        self.FrameWithin.pack(side=tk.LEFT)

        self.save = ttk.Button(self.FrameWithin, text="Save", width=15, command=self.save_button)
        self.save.pack(side=tk.TOP, padx=5, pady=2, ipady=0)

        self.load = ttk.Button(self.FrameWithin, text="Load", width=15, command=self.load_button)
        self.load.pack(side = tk.TOP, padx=5, pady=3, ipady=0)
        
        self.settings = ttk.Button(self.FrameWithin, text="Settings", width=15, command=self.settings_button)
        self.settings.pack(padx=5, pady=2, ipady=0)

        self.record = ttk.Button(self.Frame1, text="Record", width=13, command=self.record_button)
        self.record.pack(side=tk.RIGHT, padx=5, ipady=29)

        self.HotkeyDisplay = ttk.Label(self.Frame2, text="Record = HK   |   Playback = HK")
        self.HotkeyDisplay.pack()

        self.LoadedDisplay = ttk.Label(self.Frame2, text= "Loaded File = XYZ")
        self.LoadedDisplay.pack()


    def play_button(self):
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

    def save_button(self):
        pass

    def load_button(self):
        pass

    def settings_button(self):

        settingsUI = tk.Toplevel()
        settingsUI.geometry("1000x800")
        settingsUI.title('Settings')
        settings_gui = Settings(settingsUI)

    def record_button(self):
        def initialize_recording():
            self.play['state']='disabled'
            self.save['state']='disabled'
            self.load['state']='disabled'
            self.settings['state']='disabled'
            self.record['state']='disabled'

            status.currently_recording = True
            recorder.Recorder()
            status.currently_recording = False

            self.play['state']='enabled'
            self.save['state']='enabled'
            self.load['state']='enabled'
            self.settings['state']='enabled'
            self.record['state']='enabled'
        
        TRecord = threading.Thread(target=initialize_recording)
        TRecord.start()


class Settings():
    def __init__(self, master):
        self.master = master

        self.greeting = tk.Label(master, text="this is a test to see if the button works.")
        self.greeting.pack(pady=(5,0))

'''
root = tk.Tk()
root.geometry('380x170')
root.attributes("-topmost", True)
my_gui = MainApplication(root)
root.mainloop()
'''




