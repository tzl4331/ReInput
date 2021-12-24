from tkinter import ttk


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

