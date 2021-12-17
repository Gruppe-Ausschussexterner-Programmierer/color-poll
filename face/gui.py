import tkinter as tk
from tkinter import ttk

#setup root
root = tk.Tk()
root.geometry("760x540")
root.title("Auswertungsbogen")
root.resizable(0, 0)

"""#grid config
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)
root.columnconfigure(2, weight=3)
root.columnconfigure(3, weight=3)"""

#age
age_label = ttk.Label(root, text="Alter:")
age_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

age_entry = tk.Entry(root)
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

luck_button_green = ttk.Button(root, text="Grün")
luck_button_green.grid(row=3, column=1, padx=5, pady=5)

luck_label_other = ttk.Label(root, text="Andere:")
luck_label_other.grid(row=3, column=2, padx=5, pady=5, sticky=tk.E)

luck_entry_other = ttk.Entry(root)
luck_entry_other.grid(row=3, column=3, padx=5, pady=5)

luck_label_reason = ttk.Label(root, text="Grund:")
luck_label_reason.grid(row=3, column=4, padx=5, pady=5, sticky=tk.E)

luck_entry_reason = ttk.Entry(root)
luck_entry_reason.grid(row=3, column=5, padx=5, pady=5)

#closet color
#noble colors
#high-quality colors
#car color
#association red
#room color
#room atmosphere
#learning color
#relaxing color
#word association red
#flag association
#sweets ingredients
#"Schlager" color
#pop color
#classic color
#rap color
#electro color
#favorite color





root.mainloop()














"""Label(root, text="Alter").grid(row=0, sticky=W)
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

sex_button_male = Button(root, text="Männlich")
sex_button_female = Button(root, text="Weiblich")
sex_button_queer = Button(root, text="Anderes Geschlecht")
culture_button = Button(root, text="Deutsch")
culture_input = Entry(root)
favorite_color_red = Button(root, text="     ",bg="red", fg="white")


age_input.grid(row=0, column=1)
sex_button_male.grid(row=1, column=1)
sex_button_female.grid(row=1, column=2)
sex_button_queer.grid(row=1, column=3)
culture_button.grid(row=2, column=1)
culture_input.grid(row=2, column=2)
favorite_color_red.grid(row=3, column=1)"""