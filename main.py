import tkinter
from tkinter import *
from PIL import ImageTk, Image
from math import floor

class GUI:
    def __init__(self, window):
        """
        Creates the GUI
        :param window:
        """

        self.window = window

        attack_var = tkinter.StringVar(value=1)
        self.attackLabel = Label(window, text='Attack: ')
        self.attackLabel.grid(row=0, column=0, padx=5, pady=5)
        self.attackEntry = Entry(window, textvariable=attack_var)
        self.attackEntry.grid(row=0, column=1, padx=5, pady=5)

        strength_var = tkinter.StringVar(value=1)
        self.strengthLabel = Label(window, text='Strength: ')
        self.strengthLabel.grid(row=1, column=0, padx=5, pady=5)
        self.strengthEntry = Entry(window, textvariable=strength_var)
        self.strengthEntry.grid(row=1, column=1, padx=5, pady=5)

        defense_var = tkinter.StringVar(value=1)
        self.defenseLabel = Label(window, text='Defense: ')
        self.defenseLabel.grid(row=2, column=0, padx=5, pady=5)
        self.defenseEntry = Entry(window, textvariable=defense_var)
        self.defenseEntry.grid(row=2, column=1, padx=5, pady=5)

        hitpoints_var = tkinter.StringVar(value=10)
        self.hitpointsLabel = Label(window, text='Hitpoints: ')
        self.hitpointsLabel.grid(row=3, column=0, padx=5, pady=5)
        self.hitpointsEntry = Entry(window, textvariable=hitpoints_var)
        self.hitpointsEntry.grid(row=3, column=1, padx=5, pady=5)

        range_var = tkinter.StringVar(value=1)
        self.rangeLabel = Label(window, text='Ranged: ')
        self.rangeLabel.grid(row=0, column=2, padx=5, pady=5)
        self.rangeEntry = Entry(window, textvariable=range_var)
        self.rangeEntry.grid(row=0, column=3, padx=5, pady=5)

        magic_var = tkinter.StringVar(value=1)
        self.magicLabel = Label(window, text='Magic: ')
        self.magicLabel.grid(row=1, column=2, padx=5, pady=5)
        self.magicEntry = Entry(window, textvariable=magic_var)
        self.magicEntry.grid(row=1, column=3, padx=5, pady=5)

        prayer_var = tkinter.StringVar(value=1)
        self.prayerLabel = Label(window, text='Prayer: ')
        self.prayerLabel.grid(row=2, column=2, padx=5, pady=5)
        self.prayerEntry = Entry(window, textvariable=prayer_var)
        self.prayerEntry.grid(row=2, column=3, padx=5, pady=5)

        self.combat_level = Label(window, text="")
        self.combat_level.grid(row=4, column=1)
        self.error_label = Label(window, text="")
        self.error_label.grid(row=5, column=1)

        self.blank_img = ImageTk.PhotoImage(Image.open('blank.png'))
        self.img_label = Label(image=self.blank_img)
        self.img_label.image = self.blank_img
        self.img_label.grid(row=10, column=1)

        self.rat_img = ImageTk.PhotoImage(Image.open('osrs-rat.png'))
        self.giant_rat_img = ImageTk.PhotoImage(Image.open('osrs-giant-rat.png'))
        self.hell_rat_img = ImageTk.PhotoImage(Image.open('osrs-hell-rat.png'))

        self.calculateButton = Button(window, text='Calculate', command=self.clicked).grid(row=3, column=2, columnspan=2)

    def clicked(self):
        """
        shows combat level in gui
        :return:
        """

        self.error_label.config(text="")
        self.combat_level.config(text="")

        try:
            attack = int(self.attackEntry.get())
            strength = int(self.strengthEntry.get())
            defense = int(self.defenseEntry.get())
            HP = int(self.hitpointsEntry.get())
            ranged = int(self.rangeEntry.get())
            magic = int(self.magicEntry.get())
            prayer = int(self.prayerEntry.get())

            base = .25 * (defense + HP + floor(.5 * prayer))
            mele = .325 * (attack + strength)
            ranging = .325 * float(floor(ranged * 1.5))
            mage = .325 * float(floor(magic * 1.5))

            final = base + max(mele, ranging, mage)
            if attack < 1 or strength < 1 or defense < 1 or HP < 1 or ranged < 1 or magic < 1 or prayer <1:
                self.error_label.config(text='Please enter only Integers Greater than 0')
            else:
                self.combat_level.config(text='Combat Level: {:.2f}'.format(final))

            if 0 < final < 56:
                self.img_label.config(image=self.rat_img)
                self.img_label.image = self.rat_img
            if 55 < final < 89:
                self.img_label.config(image=self.giant_rat_img)
                self.img_label.image = self.giant_rat_img
            if 88 < final:
                self.img_label.config(image=self.hell_rat_img)
                self.img_label.image = self.hell_rat_img

        except ValueError:
            self.error_label.config(text='Please enter only Integers Greater than 0')
        except TypeError:
            self.error_label.config(text='Please enter only Integers Greater than 0')






def main():
    """
    Main Function
    :return:
    """
    window = Tk()
    window.title('OSRS Combat Calculator')
    window.geometry('480x320')
    window.resizable(True, True)

    GUI(window)
    window.mainloop()


if __name__ == "__main__":
    main()
