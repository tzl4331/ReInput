class UserSettings:
    def __init__(self):
        self.sampling_method = "Hybrid"
        self.looping_method = "Single"
        self.play_key = "F12"
        self.record_key = "F8"
        self.antiban = 0

john = UserSettings()
print(john.hotkey)