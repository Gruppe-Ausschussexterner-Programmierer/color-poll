import tkinter as tk


class ActiveButton():
    def pressed(self):
        self.button1.config(relief=SUNKEN)
        self.button2.config(relief=RAISED)

    def raised(self):
        
        self.button.config(relief=RAISED)