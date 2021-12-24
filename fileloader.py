import tkinter as tk
from tkinter import filedialog
import shutil

import activate
import status

def file_to_load(): #User chooses a file. If this is a valid script file, changes the current_filename variable in status.py to the selected file directory. Otherwise, doesn't.
    try:
        filename = filedialog.askopenfilename(initialdir = "/", title="Select a Script", filetypes = [('MAUS48 File', '*.maus')])
        with open(filename, 'r') as f:
            #Reads the first line to see the Initial Starting Time
            LineOne = f.readline()
            if len(LineOne)==0:
                tk.messagebox.showwarning("Warning", "The file you selected was likely empty (the first line seemed empty, which is odd).\n\nNothing interesting happens.")
            else:
                try:
                    activate.Analyser.validcheck(filename)
                    status.current_filename = filename
                    print(status.current_filename)
                except:
                    tk.messagebox.showwarning("Warning", "Nothing interesting happens.\n\nThe file you selected is invalid. Please check your file.")
    except:
        pass


def file_to_save(): #Makes a copy of the current_filename, to a place and name the user decides.
    temporary_save = status.current_filename
    user_destination = filedialog.asksaveasfilename(initialdir = "/", title="Save Script As", filetypes=[("Maus48 File", "*.maus")])
    try:
        if len(user_destination)>0:
            shutil.copyfile(temporary_save, user_destination+'.maus')
        else:
            tk.messagebox.showwarning("Warning", "Nothing interesting happens.\n")
    except:
        pass