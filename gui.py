import tkinter as tk
from tkinter import ttk, messagebox
import activate, recorder, status, functions
import threading

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
              

        self.play = ttk.Button(self.Frame1, text="Play", width=13, command=functions.play_button)
        self.play.pack(side=tk.LEFT, padx=5, ipady=29)

        self.FrameWithin = tk.Frame(self.Frame1)
        self.FrameWithin.pack(side=tk.LEFT)

        self.save = ttk.Button(self.FrameWithin, text="Save", width=15, command=functions.save_button)
        self.save.pack(side=tk.TOP, padx=5, pady=2, ipady=0)

        self.load = ttk.Button(self.FrameWithin, text="Load", width=15, command=functions.load_button)
        self.load.pack(side = tk.TOP, padx=5, pady=3, ipady=0)
        
        self.settings = ttk.Button(self.FrameWithin, text="Settings", width=15, command=functions.settings_button)
        self.settings.pack(padx=5, pady=2, ipady=0)

        self.record = ttk.Button(self.Frame1, text="Record", width=13, command=functions.record_button)
        self.record.pack(side=tk.RIGHT, padx=5, ipady=29)

        self.HotkeyDisplay = ttk.Label(self.Frame2, text="Record = HK   |   Playback = HK")
        self.HotkeyDisplay.pack()

        self.LoadedDisplay = ttk.Label(self.Frame2, text= "Loaded File = XYZ")
        self.LoadedDisplay.pack()



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




