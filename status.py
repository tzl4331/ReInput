#from time import sleep
#import threading

### DO NOT EDIT MANUALLY
### File should always be accessible

# This is the currently loaded filename
# When the user starts playback, this file will be the one that gets analyzed and replayed.
# After each recording, it is set to tempsave.maus, because that is always the name of the file recordings are saved to.
# If the user loads a custom file, then this will change to the user selected file, until they start a recording (then, tempsave.maus will come back.)
current_filename = None


recorder_stop_hotkey_pressed = False
playback_stop_hotkey_pressed = False

counting = 0

currently_playing = False
currently_recording = False

stopwatch_on = False
stored_duration = None

number = 0
