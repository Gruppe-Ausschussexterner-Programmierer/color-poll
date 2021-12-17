from tkinter import *

root = Tk()

Label(root, text="Alter").grid(row=0, sticky=W)
Label(root, text="Geschlecht").grid(row=1, sticky=W)
Label(root, text="1. Welche Farbe signalisiert Glück?").grid(row=2, sticky=W)
Label(root, text="2. Erklärung").grid(row=3, sticky=W)
Label(root, text="3.").grid(row=4, sticky=W)
Label(root, text="4.").grid(row=5, sticky=W)
Label(root, text="5.").grid(row=6, sticky=W)
Label(root, text="6.").grid(row=7, sticky=W)
Label(root, text="7.").grid(row=8, sticky=W)
Label(root, text="8.").grid(row=9, sticky=W)
Label(root, text="9.").grid(row=10, sticky=W)
Label(root, text="10.").grid(row=11, sticky=W)
Label(root, text="11.").grid(row=12, sticky=W)
Label(root, text="12.").grid(row=13, sticky=W)
Label(root, text="13.").grid(row=14, sticky=W)
Label(root, text="14.").grid(row=15, sticky=W)
Label(root, text="15.").grid(row=16, sticky=W)
Label(root, text="16.").grid(row=17, sticky=W)
Label(root, text="17.").grid(row=18, sticky=W)
Label(root, text="18.").grid(row=19, sticky=W)


ageInput = Entry(root)
sexButton1 = Button(root, text="Männlich")
sexButton2 = Button(root, text="Weiblich")
sexButton3 = Button(root, text="Anderes Geschlecht")
cultureButton = Button(root, text="Deutsch")
cultureInput = Entry(root)


ageInput.grid(row=0, column=1)
sexButton1.grid(row=1, column=1)
sexButton2.grid(row=1, column=2)
sexButton3.grid(row=1, column=3)
cultureButton.grid(row=2, column=1)
cultureInput.grid(row=2, column=2)

root.mainloop()