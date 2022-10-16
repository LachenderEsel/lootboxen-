import random
import gui

loot = ['Magisches Schwert', 'Axt', 'Kissen', 'Zauberstab', 'Feuchter Furz']

"""
Printet Sachen aus einem Array aus 
wenn die Random Nummer innerhalb des Arrays liegt
"""
def lootprint(i):
    if i < (len(loot)-1):
        return print(loot[i])
    else:
        return print("out of range")


"""
Diese Methode zeigt dir wie du eine zufällige 
Zahl zwischen 0 und 50 erzeugen kannst. 
"""
def randomnumber(minimal, maximal):
    return random.randrange(minimal,maximal)

"""
Simples Hello World für den Start
"""
def main():
    for i in range(5):
        print("Das Program von dem Tosh")
    gui.window()
    

main()