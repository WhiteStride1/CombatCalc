from tkinter import *

window = Tk()

attackNameLabel = Label(window, text='Attack: ').grid(row=0,column=0)
attackLevelEntry = Entry(window).grid(row=0,column=1)

strengthLabel = Label(window, text='Strength: ').grid(row=1,column=0)
strengthLevelEntry = Entry(window).grid(row=1,column=1)

defenceLabel = Label(window, text='Defence: ').grid(row=2, column=0)
defenseLevelEntry = Entry(window).grid(row=2, column=1)

hitpointsLabel = Label(window, text='Hitpoints: ').grid(row=3, column=0)
hitpointsLevelEntry = Entry(window).grid(row=3, column=1)

rangeLabel = Label(window, text='Range: ').grid(row=0, column=3)
rangeLevelEntry = Entry(window).grid(row=0, column=4)

magicLabel = Label(window, text='Magic: ').grid(row=1, column=3)
magicLevelEntry = Entry(window).grid(row=1, column=4)

prayerLabel = Label(window, text='Prayer: ').grid(row=2, column=3)
prayerLevelEntry = Entry(window).grid(row=2, column=4)

calculateButton = Button(window,text='Calculate').grid(row=4,column=0,columnspan=2)
window.mainloop()