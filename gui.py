from email.mime import application
from tkinter import *   

"""
Dieses Modul macht etwas
"""
def hallo():
    print("hallo Tosh")

"""
Fenster mit Button
"""
def window():
    root = Tk()  
    root.geometry('100x100')
    btn = Button(root, text = 'Hier', bd = '10', command = root.destroy)
    btn.pack(side = 'bottom')  
    root.mainloop()

