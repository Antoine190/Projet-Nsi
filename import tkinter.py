from tkinter import *
from tkinter import ttk

win= Tk()
def display_text():
   global entry
   string= entry.get()
   print(string)
   return string



label=Label(win,text= 'ville')
label.pack()

entry= Entry(win)
entry.focus_set()
entry.pack()

ttk.Button(win, text= "Okay",width= 20, command= display_text).pack(pady=20)

win.mainloop()