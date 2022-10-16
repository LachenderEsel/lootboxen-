import random
import gui

#Dies ist ein Array, eventuell könnte das nochmal praktisch sein
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
Zahl zwischen minimal und maximal erzeugen kannst. 
"""
def randomnumber(minimal, maximal):
    return random.randrange(minimal,maximal)

"""
Simples Hello World für den Start
"""
def main():
    #Eine Schleife die 5 mal etwas printet 
    for i in range(5):
        print("Das Program von dem Tosh")
    
    #Hier rufen wir eine Methode von gui.py auf 
    #Schreibe mal gui und schau, was passiert, wenn du jetzt einen . machst
    #gui.hallo()
    

main()