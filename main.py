import tkinter
from tkinter import *


class GUI:
    def __init__(self, window):
        """
        Creates the GUI
        :param window:
        """

        self.window = window
        attack = tkinter.IntVar()
        self.attackLabel = Label(window, text='Attack: ')
        self.attackLabel.grid(row=0, column=0, padx=5, pady=5)
        self.attackEntry = Entry(window, textvariable=attack)
        self.attackEntry.grid(row=0, column=1, padx=5, pady=5)

        self.strengthLabel = Label(window, text='Strength: ')
        self.strengthLabel.grid(row=1, column=0, padx=5, pady=5)
        self.strengthEntry = Entry(window)
        self.strengthEntry.grid(row=1, column=1, padx=5, pady=5)

        self.defenseLabel = Label(window, text='Defense: ')
        self.defenseLabel.grid(row=2, column=0, padx=5, pady=5)
        self.defenseEntry = Entry(window)
        self.defenseEntry.grid(row=2, column=1, padx=5, pady=5)

        self.hitpointsLabel = Label(window, text='Hitpoints: ')
        self.hitpointsLabel.grid(row=3, column=0, padx=5, pady=5)
        self.hitpointsEntry = Entry(window)
        self.hitpointsEntry.grid(row=3, column=1, padx=5, pady=5)

        self.rangeLabel = Label(window, text='Ranged: ')
        self.rangeLabel.grid(row=0, column=2, padx=5, pady=5)
        self.rangeEntry = Entry(window)
        self.rangeEntry.grid(row=0, column=3, padx=5, pady=5)

        self.magicLabel = Label(window, text='Magic: ')
        self.magicLabel.grid(row=1, column=2, padx=5, pady=5)
        self.magicEntry = Entry(window)
        self.magicEntry.grid(row=1, column=3, padx=5, pady=5)

        self.prayerLabel = Label(window, text='Prayer: ')
        self.prayerLabel.grid(row=2, column=2, padx=5, pady=5)
        self.prayerEntry = Entry(window)
        self.prayerEntry.grid(row=2, column=3, padx=5, pady=5)

        self.combat_level = Label(window, text="")
        self.combat_level.grid(row=4, column=0)
        self.error_label = Label(window, text="")
        self.error_label.grid(row=5, column=0)

        self.calculateButton = Button(window, text='Calculate', command=self.clicked).grid(row=3, column=2, columnspan=2)

    def clicked(self):
        """
        shows combat level in gui
        :return:
        """
        self.error_label.config(text=self.attackEntry.get())





def main():
    """
    Main Function
    :return:
    """
    window = Tk()
    window.title('OSRS Combat Calculator')
    window.geometry('480x320')
    window.resizable(False, False)

    GUI(window)
    window.mainloop()


if __name__ == "__main__":
    main()
