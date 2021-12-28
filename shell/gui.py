import tkinter as tk
from tkinter import StringVar, ttk

'''#input to variable
from core import form'''

#setup root
root = tk.Tk()
root.geometry("750x700")
root.title("Auswertungsbogen")
root.resizable(0, 0)

#age
age_label = ttk.Label(root, text="Alter:")
age_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

age_entry = ttk.Entry(root)
age_entry.grid(row=0, column=1, padx=5, pady=5)

#sex
sex_label = ttk.Label(root, text="Geschlecht:")
sex_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

sex_button_male = ttk.Button(root, text="Männlich")
sex_button_male.grid(row=1, column=1, padx=5, pady=5)

sex_button_female = ttk.Button(root, text="Weiblich")
sex_button_female.grid(row=1, column=2, padx=5, pady=5)

sex_button_male = ttk.Button(root, text="Anderes Geschlecht")
sex_button_male.grid(row=1, column=3, padx=5, pady=5)

#culture
culture_label = ttk.Label(root, text="Kulturzugehörigkeit: ")
culture_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)

culture_button_german = ttk.Button(root, text="Deutsch")
culture_button_german.grid(row=2, column=1, padx=5, pady=5)

culture_label_other = ttk.Label(root, text="Andere:")
culture_label_other.grid(row=2, column=2, padx=5, pady=5, sticky=tk.E)

culture_entry = ttk.Entry(root)
culture_entry.grid(row=2, column=3, padx=5, pady=5)

#luck color
luck_label = ttk.Label(root, text="Signalfarbe Glück:")
luck_label.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)

luck_color = StringVar(root)
luck_color.set("Grün")
luck_drop_down = ttk.OptionMenu(root, luck_color, "Grün", "Weiß", "Gelb", "Orange", "Rot", "Rosa", "Violett", "Hellgrün", "Grün", "Hellblau", "Blau","Braun", "Grau", "Schwarz")
luck_drop_down.grid(row=3, column=1, padx=5, pady=5)

luck_label_reason = ttk.Label(root, text="Grund:")
luck_label_reason.grid(row=3, column=2, padx=5, pady=5, sticky=tk.E)

luck_entry_reason = ttk.Entry(root)
luck_entry_reason.grid(row=3, column=3, padx=5, pady=5)

#closet color
closet_label = ttk.Label(root, text="Häufigste Farbe im Kleiderschrank:")
closet_label.grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)

#noble colors
closet_label = ttk.Label(root, text="Signalfarbe Edel:")
closet_label.grid(row=5, column=0, padx=5, pady=5, sticky=tk.W)

#high-quality colors
closet_label = ttk.Label(root, text="Signalfarbe Hochwertig:")
closet_label.grid(row=6, column=0, padx=5, pady=5, sticky=tk.W)

#car color
closet_label = ttk.Label(root, text="Farbe Traumauto:")
closet_label.grid(row=7, column=0, padx=5, pady=5, sticky=tk.W)

#association red
closet_label = ttk.Label(root, text="Assoziation Rot:")
closet_label.grid(row=8, column=0, padx=5, pady=5, sticky=tk.W)

#room color
closet_label = ttk.Label(root, text="Zimmer Farbe")
closet_label.grid(row=9, column=0, padx=5, pady=5, sticky=tk.W)

#room atmosphere
closet_label = ttk.Label(root, text="Zimmer Atmosphäre:")
closet_label.grid(row=10, column=0, padx=5, pady=5, sticky=tk.W)

#learning color
closet_label = ttk.Label(root, text="Farbe zum Lernen:")
closet_label.grid(row=11, column=0, padx=5, pady=5, sticky=tk.W)

#relaxing color
closet_label = ttk.Label(root, text="Farbe zum Entspannen:")
closet_label.grid(row=12, column=0, padx=5, pady=5, sticky=tk.W)

#word association red
closet_label = ttk.Label(root, text="Word-Assoziation Rot:" )
closet_label.grid(row=13, column=0, padx=5, pady=5, sticky=tk.W)

#flag association
closet_label = ttk.Label(root, text="Assoziation Flagge:")
closet_label.grid(row=14, column=0, padx=5, pady=5, sticky=tk.W)

#sweets ingredients
closet_label = ttk.Label(root, text="Zutaten in Süßkram:")
closet_label.grid(row=15, column=0, padx=5, pady=5, sticky=tk.W)

#"Schlager" color
closet_label = ttk.Label(root, text="Schlager Farbe:")
closet_label.grid(row=16, column=0, padx=5, pady=5, sticky=tk.W)

#pop color
closet_label = ttk.Label(root, text="Pop Farbe:")
closet_label.grid(row=17, column=0, padx=5, pady=5, sticky=tk.W)

#classic color
closet_label = ttk.Label(root, text="Klassik Farbe:")
closet_label.grid(row=18, column=0, padx=5, pady=5, sticky=tk.W)

#rap color
closet_label = ttk.Label(root, text="Rap Farbe:")
closet_label.grid(row=19, column=0, padx=5, pady=5, sticky=tk.W)

#electro color
closet_label = ttk.Label(root, text="Elekto Farbe:")
closet_label.grid(row=20, column=0, padx=5, pady=5, sticky=tk.W)

#favorite color
closet_label = ttk.Label(root, text="Lieblingsfarbe:")
closet_label.grid(row=21, column=0, padx=5, pady=5, sticky=tk.W)

#submit
submit_button = ttk.Button(root, text="Abschicken")
submit_button.grid(row=22, column=5, padx=5, pady=5, sticky=tk.E)


def run():
    root.mainloop()
