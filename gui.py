import tkinter as tk
from tkinter import ttk

import config

class About:
    #About this program
    def __init__(self):
        win = tk.Toplevel()
        win.geometry('625x250')
        win.attributes('-topmost', True)
        win.title('About')

        settingsTitle = tk.Label(win, text="ReInput")
        settingsTitle.config(font=("Segoe UI", 15))
        settingsTitle.pack()
        
        label = ttk.Label(win, text="ReInput v1.1", style='Bold.TLabel').pack(pady=(10,0))
        webpage = ttk.Label(win, text="https://github.com/quadroopl/ReInput", style='my.TLabel').pack(pady=(0,0))

        about1 = ttk.Label(win, text="Mouse + Keyboard Logging and Playback Tool", style='my.TLabel').pack(pady=(10,0))

        #changelog_frame = tk.Frame(win)
        #changelog_frame.pack()
        #changelog_label = ttk.Label(changelog_frame, text="Version History", style='Bold.TLabel', anchor='w').pack(pady=(5,0))
        #v100 = ttk.Label(changelog_frame, text="v1.0 - \nInitial Release", style='my.TLabel').pack(pady=(10,0))
        #v101 = ttk.Label(changelog_frame, text="v1.1 - \nAdded File Menu\nUpdated Links", style='my.TLabel').pack(pady=(10,0))


        disclaimer_label = ttk.Label(win, text="Disclaimer", style='Bold.TLabel').pack(pady=(30,0))
        disclaimer = ttk.Label(win, text="ReInput cannot hold responsibility for any damages from the use/failure to use this program", style='small.TLabel').pack(pady=(5,0))
        disclaimer2 = ttk.Label(win, text="ReInput playback may add latency and is unsuitable for sensitive/millisecond precise actions.\nThe latency added will depending on CPU performance.", style='small.TLabel').pack(pady=(0,5))

class Settings:
    #This is a copy and paste of the settings buttion function in maus48 public main.py. This could do with some upgrades
    def __init__(self):

        win = tk.Toplevel()
        win.geometry('1150x760')
        win.attributes('-topmost', True)
        win.title('Settings for ReInput')

        settingsTitle = tk.Label(win, text="Settings")
        settingsTitle.config(font=("Segoe UI", 15))
        settingsTitle.pack()
        
        label = ttk.Label(win, text="ReInput v1.0", style='Bold.TLabel').pack(pady=(10,0))
        labeltop = ttk.Button(win, text="Currently saved settings: {} Sampling, {} Playback Loop, {} Playback Hotkey, {} Recording Hotkey, Antiban = {}.".format(config.Configured_sampling_method, config.Configured_looping_method, config.Configured_playkey_temp, config.Configured_recordkey_temp, config.Configured_antiban), style='my.TButton')
        labeltop.pack(pady=(5,8))

        ################# FUNCTIONS FOR SAMPLING METHOD ##############################
        def fidelityButton():
            button_fidelity["state"]="disabled"
            button_efficiency["state"]="normal"
            button_hybrid["state"]="normal"

            config.User_sampling_method = "Fidelity"

            button_apply["text"]="Save and apply changes"
            button_apply["state"]="normal"

        def efficiencyButton():
            button_efficiency["state"]="disabled"
            button_fidelity["state"]="normal"
            button_hybrid["state"]="normal"


            config.User_sampling_method = "Efficiency"

            button_apply["text"]="Save and apply changes"
            button_apply["state"]="normal"

        def hybridButton():
            button_hybrid["state"]="disabled"
            button_fidelity["state"]="normal"
            button_efficiency["state"]="normal"

            config.User_sampling_method = "Hybrid"

            button_apply["text"]="Save and apply changes"
            button_apply["state"]="normal"

        ################# FUNCTIONS FOR PLAYBACK LOOPING ##############################
        def singleButton():
            button_single["state"]="disabled"
            button_infinite["state"]="normal"
            #button_custom["state"]="normal"

            button_single["text"]="[Single]"
            button_infinite["text"]="Infinite"
            #button_custom["text"]="Custom"
            config.User_looping_method = "Single"

            button_apply["text"]="Save and apply changes"
            button_apply["state"]="normal"

        def infiniteButton():
            button_single["state"]="normal"
            button_infinite["state"]="disabled"
            #button_custom["state"]="normal"

            button_single["text"]="Single"
            button_infinite["text"]="[Infinite]"
            #button_custom["text"]="Custom"
            config.User_looping_method = "Infinite"

            button_apply["text"]="Save and apply changes"
            button_apply["state"]="normal"

        def customButton():
            button_single["state"]="normal"
            button_infinite["state"]="normal"
            #button_custom["state"]="disabled"

            button_single["text"]="Single"
            button_infinite["text"]="Infinite"
            #button_custom["text"]="[Custom]"
            config.User_looping_method = "Custom"

            button_apply["text"]="Save and apply changes"
            button_apply["state"]="normal"
        
        ######### FUNCTIONS FOR OSRS ANTIBAN / RANDOMIZATION ############
        def antibanOnButton():
            #button_antibanOn["state"]="disabled"
            #button_antibanOff["state"]="normal"
            #button_antibanOn["text"]="Antiban is enabled"
            #button_antibanOff["text"]="Turn off OSRS Randomize Antiban"

            config.User_antiban = 1

            button_apply["text"]="Save and apply changes"
            button_apply["state"]="normal"
        
        def antibanOffButton():
            #button_antibanOff["state"]="disabled"
            #button_antibanOn["state"]="normal"
            #button_antibanOff["text"]="Antiban is disabled"
            #button_antibanOn["text"]="Turn on OSRS Randomize Antiban"

            config.User_antiban = 0

            button_apply["text"]="Save and apply changes"
            button_apply["state"]="normal"

        #Packing the Frames in Settings
        ############ FRAMES FOR SAMPLING METHOD ###############
        WinFrame1 = tk.Frame(win)
        WinFrame1.pack()

        WinFrame2 = tk.Frame(win)
        WinFrame2.pack(pady=10)

        #Window Frame 1
        WinFrame1Labels = tk.Frame(WinFrame1)
        WinFrame1Labels.pack(side=tk.TOP)
        Samplinglabel = ttk.Label(WinFrame1Labels, text="Sampling Method", style='Bold.TLabel', anchor='w').pack(side=tk.LEFT, padx=(5,15))
        SamplingDescription = ttk.Label(WinFrame1Labels, text="This controls how frequently cursor movements are logged.\nMore logs per second = more smooth cursor but more latency\nNOTE: Fidelity playback may run impractically slow on low-end PCs or Virtual Machines\n", style='my.TLabel').pack(side=tk.BOTTOM)

        button_fidelity= ttk.Button(WinFrame2, text="Fidelity\n200 logs/sec", width=17, command=fidelityButton, style='my.TButton' )
        button_fidelity.pack(side=tk.LEFT, padx=8, ipady=20)

        button_efficiency = ttk.Button(WinFrame2, text='Efficiency\n40 logs/sec', width=17, command=efficiencyButton, style='my.TButton' )
        button_efficiency.pack(side=tk.LEFT, padx=8, ipady=20)

        button_hybrid = ttk.Button(WinFrame2, text="Hybrid\n70 logs/sec", width=17, command=hybridButton, style='my.TButton' )
        button_hybrid.pack(side=tk.RIGHT, padx=8, ipady=20)

        ############ FRAMES FOR PLAYBACK LOOPING ###############
        WinFrame3 = tk.Frame(win)
        WinFrame3.pack()

        WinFrame4 = tk.Frame(win)
        WinFrame4.pack(pady=10)

        WinFrame3Labels = tk.Frame(WinFrame3)
        WinFrame3Labels.pack(side=tk.TOP)
        LoopLabel = ttk.Label(WinFrame3Labels, text="Playback Looping", style='Bold.TLabel', anchor='w').pack(side=tk.LEFT, padx=(5,15))
        
        LoopDescription = ttk.Label(WinFrame3Labels, text="\nSingle:  Plays the loaded script once\nInfinite:  Plays the loaded script until the Stop Hotkey is pressed\n", style='my.TLabel').pack(side=tk.BOTTOM, fill=tk.X)

        button_single= ttk.Button(WinFrame4, text="Single", width=10, command=singleButton, style='my.TButton' )
        button_single.pack(side=tk.LEFT, padx=8, ipady=20)

        button_infinite = ttk.Button(WinFrame4, text='Infinite', width=10, command=infiniteButton, style='my.TButton' )
        button_infinite.pack(side=tk.LEFT, padx=8, ipady=20)

        #button_custom = ttk.Button(WinFrame4, text="Custom", width=10, command=customButton, style='my.TButton' )
        #button_custom.pack(side=tk.RIGHT, padx=8, ipady=20)



        ############ FRAMES FOR HOTKEY SETTINGS ###############
        WinFrame5 = tk.Frame(win)
        WinFrame5.pack()

        WinFrame6 = tk.Frame(win)
        WinFrame6.pack(pady=20)

        WinFrame5Labels = tk.Frame(WinFrame5)
        WinFrame5Labels.pack(side=tk.TOP)
        HKLabel = ttk.Label(WinFrame5Labels, text="Hotkey Preferences", style='Bold.TLabel', anchor='w').pack(side=tk.LEFT, padx=(5,15))
        
        HKDescription = ttk.Label(WinFrame5Labels, text="Note: Your playback and recording hotkey cannot be the same.\nYour hotkeys are also displayed on the main window.", style='my.TLabel').pack(side=tk.BOTTOM, fill=tk.X)

        #PlayHotkey Menu
        def changePlayHotkey(PHKResult):
            play_hotkey_choice = PlayHotkeyChoice.get()
            #list_of_rec_hotkeys.pop(play_hotkey_choice)
            if not play_hotkey_choice == "Choose Playback Hotkey":
                if not play_hotkey_choice == config.User_recordkey_temp:
                    config.User_playkey_temp = play_hotkey_choice
                    button_apply["text"]="Save and apply changes"
                    button_apply["state"]="normal"
                else:
                    tk.messagebox.showwarning("Hotkey In Use", "Your playback and recording hotkey cannot be the same.\n\nPlease choose another hotkey.\n")
                    PlayHotkeyChoice.set("Choose Recording Hotkey")
                    pass
            #RecHotkey.configure(ttk.OptionMenu(WinFrame6, RecHotkeyChoice, *list_of_rec_hotkeys, command=changeRecHotkey).pack(side=tk.LEFT))
            print(play_hotkey_choice)
        PlayHotkeyChoice = tk.StringVar(value="Select Playback Hotkey...")
        list_of_hotkeys = {'Choose Playback Hotkey':1,'F1':2,'F2':3,'F3':4,'F4':5,'F5':6,'F6':7,'F7':8,'F8':9,'F9':10,'F10':11,'F11':12,'F12':13}
        
        PHKDescription = ttk.Label(WinFrame6, text="Playback:  ", style='Bold.TLabel').pack(side=tk.LEFT, padx = 15)
        PlayHotkey = ttk.OptionMenu(WinFrame6, PlayHotkeyChoice, *list_of_hotkeys, command=changePlayHotkey).pack(side=tk.LEFT)

        #RecordingHotkey Menu
        def changeRecHotkey(RHKResult):
            rec_hotkey_choice = RecHotkeyChoice.get()
            if not rec_hotkey_choice == "Choose Recording Hotkey":
                if not rec_hotkey_choice == config.User_playkey_temp:
                    config.User_recordkey_temp = rec_hotkey_choice
                    button_apply["text"]="Save and apply changes"
                    button_apply["state"]="normal"
                else:
                    tk.messagebox.showwarning("Hotkey In Use", "Your playback and recording hotkey cannot be the same.\n\nPlease choose another hotkey.\n")
                    RecHotkeyChoice.set("Choose Recording Hotkey")
                    pass
            print(rec_hotkey_choice)
        RecHotkeyChoice = tk.StringVar(value="F6")
        list_of_rec_hotkeys = {'Choose Recording Hotkey':1,'F1':2,'F2':3,'F3':4,'F4':5,'F5':6,'F6':7,'F7':8,'F8':9,'F9':10,'F10':11,'F11':12,'F12':13}

        RHKDescription = ttk.Label(WinFrame6, text="Recording:  ", style='Bold.TLabel').pack(side=tk.LEFT, padx=15)
        RecHotkey = ttk.OptionMenu(WinFrame6, RecHotkeyChoice, *list_of_rec_hotkeys, command=changeRecHotkey).pack(side=tk.LEFT)

        
        ##########winframe 7 and 8
        WinFrame7 = tk.Frame(win)
        WinFrame7.pack()

        WinFrame8 = tk.Frame(win)
        WinFrame8.pack(pady=10)

        '''
        WinFrame7Labels = tk.Frame(WinFrame7)
        WinFrame7Labels.pack(side=tk.TOP)
        LoopLabel = ttk.Label(WinFrame7Labels, text="OSRS Anti-ban Mode", style='Bold.TLabel').pack(side=tk.LEFT, padx=(5,15))
        
        LoopDescription = ttk.Label(WinFrame7Labels, text="This enables more game anti-ban features                                                                                                                                                      \nTime Randomize:  A varying small delay is added on top of the existing recording delays\nThis means even when looping infinitely there will never be an identical timing pattern").pack(side=tk.BOTTOM, fill=tk.X)

        button_antibanOn= ttk.Button(WinFrame8, text="Anti-ban mode is not yet available", width=35, command=antibanOnButton, style='my.TButton', state="disabled")
        button_antibanOn.pack(side=tk.LEFT, padx=8, ipady=20)

        button_antibanOff = ttk.Button(WinFrame8, text="Einstein is still thinking...", width=35, command=antibanOffButton, style='my.TButton', state="disabled" )
        button_antibanOff.pack(side=tk.LEFT, padx=8, ipady=20)
        '''
        WinFrameEND = tk.Frame(win)
        WinFrameEND.pack(pady=8)
        SettingsInfo = ttk.Label(WinFrameEND, text="Even if your old settings don't show here yet, they are still saved unless changed.\nSettings will only save once applied. If 'settings.48' is deleted, settings will be defaulted on next launch.",).pack()

        def applyButton():
            #Save all settings
            config.UserPressedSave()
            button_apply["state"]="disabled"
            button_apply["text"]="Settings saved"

            labeltop["text"]="Currently saved settings: {} Sampling, {} Playback Loop, {} Playback Hotkey, {} Recording Hotkey, Antiban = {}.".format(config.Configured_sampling_method, config.Configured_looping_method, config.Configured_playkey_temp, config.Configured_recordkey_temp, config.Configured_antiban)


        WinFrame9 = tk.Frame(win)
        WinFrame9.pack(pady=10)

        button_apply= ttk.Button(WinFrame9, text="Save and apply changes", width=28, command=applyButton, state="disabled" )
        button_apply.pack(side=tk.BOTTOM, padx=8, ipady=5)

class WindowTest:
    def __init__(self, master):
        self.master = master

        self.greeting = tk.Label(master, text="This is a test to see if the button works.")
        self.greeting.pack(pady=(5,0))

