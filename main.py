from tkinter import *

class GUI:
    def __init__(self, window):
        self.window = window

        self.attackLabel = Label(window, text='Attack: ').grid(row=0, column=0,padx=5, pady=5)
        self.attackEntry = Entry(window).grid(row=0, column=1, padx=5, pady=5)

        self.strengthLabel = Label(window, text='Strength: ').grid(row=1, column=0, padx=5, pady=5)
        self.strengthEntry = Entry(window).grid(row=1, column=1, padx=5, pady=5)

        self.strengthLabel = Label(window, text='Strength: ').grid(row=1, column=0, padx=5, pady=5)
        self.strengthEntry = Entry(window).grid(row=1, column=1, padx=5, pady=5)

        self.defenseLabel = Label(window, text='Defense: ').grid(row=2, column=0, padx=5, pady=5)
        self.defenseEntry = Entry(window).grid(row=2, column=1, padx=5, pady=5)

        self.hitpointsLabel = Label(window, text='Hitpoints: ').grid(row=3, column=0, padx=5, pady=5)
        self.hitpointsEntry = Entry(window).grid(row=3, column=1, padx=5, pady=5)

        self.rangeLabel = Label(window, text='Ranged: ').grid(row=0, column=2, padx=5, pady=5)
        self.rangeEntry = Entry(window).grid(row=0, column=3, padx=5, pady=5)

        self.magicLabel = Label(window, text='Magic: ').grid(row=1, column=2, padx=5, pady=5)
        self.magicEntry = Entry(window).grid(row=1, column=3, padx=5, pady=5)

        self.prayerLabel = Label(window, text='Prayer: ').grid(row=2, column=2, padx=5, pady=5)
        self.prayerEntry = Entry(window).grid(row=2, column=3, padx=5, pady=5)

        self.calculateButton = Button(window, text='Calculate').grid(row=3, column=2, columnspan=2)


def main():
    window = Tk()
    window.title('OSRS Combat Calculator')
    window.geometry('480x320')
    window.resizable(False, False)

    GUI(window)
    window.mainloop()

if __name__ == "__main__":
    main()