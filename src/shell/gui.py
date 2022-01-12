import tkinter as tk
from tkinter import StringVar, ttk
from core import form_manager
import os
import traceback

#setup root
root = tk.Tk()
root.geometry("930x790")
root.title("Auswertungsbogen")
root.resizable(0, 0)


#variable setup
entry_age = tk.StringVar(root)
checkbutton_sex = 0 # 0->None, 1->Male, 2->Female, 3->Other
entry_culture = tk.StringVar(root)
luck_color = None
entry_luck_reason = tk.StringVar(root)
closet_color = None
noble_color_1 = None
noble_color_2 = None
quality_1 = None
quality_2 = None
car = None
red_entry = tk.StringVar(root)
room_color = None
checkbutton_room_color_deliberatly_chosen = 4 # 4->None, 5->Yes, 6->No
entry_room_color_reason = tk.StringVar(root)
entry_room_atmosphere = tk.StringVar(root)
learning_color = None
relaxing_color = None
checkbutton_red = 7 # 7->None, 8->Love, 9->War
checkbutton_flag = 10 # 10->None, 11->Yes, 12->No
entry_flag = tk.StringVar(root)
sweet_ingredients = None
schlager_color = None
pop_color = None
classic_color = None
rap_color = None
electro_color = None
favorite_color = None
checkbutton_favorite_color = 13 # 13->None, 14->Matches, 15->Does not match, 16 -> matches partially

def log(message):
    with open(os.path.abspath(form_manager.WORKING_DIR + "/../../.data/log.txt"), "a") as log:
        log.write("gui.py: " + message + "\n")

def setup():
    global entry_age
    global checkbutton_sex
    global entry_culture
    global luck_color
    global entry_luck_reason
    global closet_color
    global noble_color_1
    global noble_color_2
    global quality_1
    global quality_2
    global car
    global red_entry
    global room_color
    global checkbutton_room_color_deliberatly_chosen
    global entry_room_color_reason
    global entry_room_atmosphere
    global learning_color
    global relaxing_color
    global checkbutton_red
    global checkbutton_flag
    global entry_flag
    global sweet_ingredients
    global schlager_color
    global pop_color
    global classic_color
    global rap_color
    global electro_color
    global favorite_color
    global checkbutton_favorite_color
    #SERIOUSLY PYTHON WHAT IN THE GODDAMN STUPID FUCKING WORLD

    #age
    age_label = ttk.Label(root, text="Alter:")
    age_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

    age_entry = ttk.Entry(root, textvariable=entry_age)
    age_entry.grid(row=0, column=1, padx=5, pady=5)

    #sex
    sex_label = ttk.Label(root, text="Geschlecht:")
    sex_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

    checkbutton_sex = tk.IntVar()
    sex_checkbutton_male = ttk.Checkbutton(root, onvalue=1, variable=checkbutton_sex, text="Männlich")
    sex_checkbutton_male.grid(row=1, column=1, padx=5, pady=5)

    sex_checkbutton_female = ttk.Checkbutton(root, onvalue=2, variable=checkbutton_sex, text="Weiblich")
    sex_checkbutton_female.grid(row=1, column=3, padx=5, pady=5)

    sex_checkbutton_other = ttk.Checkbutton(root, onvalue=3, variable=checkbutton_sex, text="Anderes Geschlecht")
    sex_checkbutton_other.grid(row=1, column=5, padx=5, pady=5)

    #culture
    culture_label = ttk.Label(root, text="Kulturzugehörigkeit: ")
    culture_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)

    entry_culture = tk.StringVar()
    culture_checkbutton_german = ttk.Checkbutton(root, offvalue="", onvalue="Deutsch", variable=entry_culture, text="Deutsch")
    culture_checkbutton_german.grid(row=2, column=1, padx=5, pady=5)

    culture_label_other = ttk.Label(root, text="Eingabe:")
    culture_label_other.grid(row=2, column=2, padx=5, pady=5, sticky=tk.E)

    culture_entry_other = ttk.Entry(root, textvariable=entry_culture)
    culture_entry_other.grid(row=2, column=3, padx=5, pady=5)


    #luck color
    luck_label = ttk.Label(root, text="Signalfarbe Glück:")
    luck_label.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)

    luck_color = StringVar(root)
    luck_color.set("Grün")
    luck_optionmenu = ttk.OptionMenu(root, luck_color, "Grün", "-----", "Weiß", "Gelb", "Orange", "Rot", "Rosa", "Violett", "Hellgrün", "Grün", "Hellblau", "Blau","Braun", "Grau", "Schwarz")
    luck_optionmenu.grid(row=3, column=1, padx=5, pady=5)

    luck_label_other = ttk.Label(root, text="Eingabe:")
    luck_label_other.grid(row=3, column=2, padx=5, pady=5, sticky=tk.E)

    luck_entry_other = ttk.Entry(root, textvariable=luck_color)
    luck_entry_other.grid(row=3, column=3, padx=5, pady=5)

    luck_label_reason = ttk.Label(root, text="Grund:")
    luck_label_reason.grid(row=3, column=4, padx=5, pady=5, sticky=tk.E)

    luck_entry_reason = ttk.Entry(root, textvariable=entry_luck_reason)
    luck_entry_reason.grid(row=3, column=5, padx=5, pady=5)


    #closet color
    closet_label = ttk.Label(root, text="Häufigste Farbe im Kleiderschrank:")
    closet_label.grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)

    closet_color = StringVar(root)
    closet_color.set("-----")
    closet_optionmenu = ttk.OptionMenu(root, closet_color, "-----", "-----", "Weiß", "Gelb", "Orange", "Rot", "Rosa", "Violett", "Hellgrün", "Grün", "Hellblau", "Blau","Braun", "Grau", "Schwarz")
    closet_optionmenu.grid(row=4, column=1, padx=5, pady=5)

    closet_label_other = ttk.Label(root, text="Eingabe:")
    closet_label_other.grid(row=4, column=2, padx=5, pady=5, sticky=tk.E)

    closet_entry_other = ttk.Entry(root, textvariable=closet_color)
    closet_entry_other.grid(row=4, column=3, padx=5, pady=5)


    #noble colors
    noble_label = ttk.Label(root, text="Signalfarben Edel:")
    noble_label.grid(row=5, column=0, padx=5, pady=5, sticky=tk.W)

    noble_color_1 = StringVar(root)
    noble_color_1.set("-----")
    noble_optionmenu_1 = ttk.OptionMenu(root, noble_color_1, "-----", "-----", "Weiß", "Gelb", "Orange", "Rot", "Rosa", "Violett", "Hellgrün", "Grün", "Hellblau", "Blau","Braun", "Grau", "Schwarz")
    noble_optionmenu_1.grid(row=5, column=1, padx=5, pady=5)

    noble_label_other_1 = ttk.Label(root, text="Eingabe:")
    noble_label_other_1.grid(row=5, column=2, padx=5, pady=5, sticky=tk.E)

    noble_entry_other_1 = ttk.Entry(root, textvariable=noble_color_1)
    noble_entry_other_1.grid(row=5, column=3, padx=5, pady=5)

    noble_color_2 = StringVar(root)
    noble_color_2.set("-----")
    noble_optionmenu_2 = ttk.OptionMenu(root, noble_color_2, "-----", "-----", "Weiß", "Gelb", "Orange", "Rot", "Rosa", "Violett", "Hellgrün", "Grün", "Hellblau", "Blau","Braun", "Grau", "Schwarz")
    noble_optionmenu_2.grid(row=5, column=5, padx=5, pady=5)

    noble_label_other_2 = ttk.Label(root, text="Eingabe:")
    noble_label_other_2.grid(row=5, column=6, padx=5, pady=5, sticky=tk.E)

    noble_entry_other_2 = ttk.Entry(root, textvariable=noble_color_2)
    noble_entry_other_2.grid(row=5, column=7, padx=5, pady=5)


    #high-quality colors
    quality_label = ttk.Label(root, text="Signalfarben Hochwertig:")
    quality_label.grid(row=6, column=0, padx=5, pady=5, sticky=tk.W)

    quality_1 = StringVar(root)
    quality_1.set("-----")
    quality_optionmenu_1 = ttk.OptionMenu(root, quality_1, "-----", "-----", "Weiß", "Gelb", "Orange", "Rot", "Rosa", "Violett", "Hellgrün", "Grün", "Hellblau", "Blau","Braun", "Grau", "Schwarz")
    quality_optionmenu_1.grid(row=6, column=1, padx=5, pady=5)

    quality_label_other_1 = ttk.Label(root, text="Eingabe:")
    quality_label_other_1.grid(row=6, column=2, padx=5, pady=5, sticky=tk.E)

    quality_entry_other_1 = ttk.Entry(root, textvariable=quality_1)
    quality_entry_other_1.grid(row=6, column=3, padx=5, pady=5)

    quality_2 = StringVar(root)
    quality_2.set("-----")
    quality_optionmenu_2 = ttk.OptionMenu(root, quality_2, "-----", "-----", "Weiß", "Gelb", "Orange", "Rot", "Rosa", "Violett", "Hellgrün", "Grün", "Hellblau", "Blau","Braun", "Grau", "Schwarz")
    quality_optionmenu_2.grid(row=6, column=5, padx=5, pady=5)

    quality_label_other_2 = ttk.Label(root, text="Eingabe:")
    quality_label_other_2.grid(row=6, column=6, padx=5, pady=5, sticky=tk.E)

    quality_entry_other_2 = ttk.Entry(root, textvariable=quality_2)
    quality_entry_other_2.grid(row=6, column=7, padx=5, pady=5)


    #car color
    car_label = ttk.Label(root, text="Farbe Traumauto:")
    car_label.grid(row=7, column=0, padx=5, pady=5, sticky=tk.W)

    car = StringVar(root)
    car.set("-----")
    car_optionmenu = ttk.OptionMenu(root, car, "-----", "-----", "Weiß", "Gelb", "Orange", "Rot", "Rosa", "Violett", "Hellgrün", "Grün", "Hellblau", "Blau","Braun", "Grau", "Schwarz")
    car_optionmenu.grid(row=7, column=1, padx=5, pady=5)

    car_label_other = ttk.Label(root, text="Eingabe:")
    car_label_other.grid(row=7, column=2, padx=5, pady=5, sticky=tk.E)

    car_entry_other = ttk.Entry(root, textvariable=car)
    car_entry_other.grid(row=7, column=3, padx=5, pady=5)


    #association red
    red_label = ttk.Label(root, text="Assoziation Rot:")
    red_label.grid(row=8, column=0, padx=5, pady=5, sticky=tk.W)

    red_association_entry = ttk.Entry(root, textvariable=red_entry)
    red_association_entry.grid(row=8, column=1, padx=5, pady=5)


    #room color
    room_label = ttk.Label(root, text="Zimmer Farbe:")
    room_label.grid(row=9, column=0, padx=5, pady=5, sticky=tk.W)

    room_color = StringVar(root)
    room_color.set("Weiß")
    room_optionmenu = ttk.OptionMenu(root, room_color, "Weiß", "-----", "Weiß", "Gelb", "Orange", "Rot", "Rosa", "Violett", "Hellgrün", "Grün", "Hellblau", "Blau","Braun", "Grau", "Schwarz")
    room_optionmenu.grid(row=9, column=1, padx=5, pady=5)

    room_label_other = ttk.Label(root, text="Eingabe:")
    room_label_other.grid(row=9, column=2, padx=5, pady=5, sticky=tk.E)

    room_entry_other = ttk.Entry(root, textvariable=room_color)
    room_entry_other.grid(row=9, column=3, padx=5, pady=5)

    #room color deliberatly chosen
    room_color_deliberatly_chosen_label = ttk.Label(root, text="Zimmer Farbe bewusst gewählt:")
    room_color_deliberatly_chosen_label.grid(row=10, column=0, padx=5, pady=5, sticky=tk.W)

    checkbutton_room_color_deliberatly_chosen = tk.IntVar()
    room_color_deliberatly_chosen_checkbutton_yes = ttk.Checkbutton(root, onvalue=5, variable=checkbutton_room_color_deliberatly_chosen, text="Ja")
    room_color_deliberatly_chosen_checkbutton_yes.grid(row=10, column=1, padx=5, pady=5)

    room_color_deliberatly_chosen_label_reason = ttk.Label(root, text="Grund:")
    room_color_deliberatly_chosen_label_reason.grid(row=10, column=2, padx=5, pady=5, sticky=tk.E)

    room_color_deliberatly_chosen_entry_reason = ttk.Entry(root, textvariable=entry_room_color_reason)
    room_color_deliberatly_chosen_entry_reason.grid(row=10, column=3, padx=5, pady=5)

    room_color_deliberatly_chosen_checkbutton_no = ttk.Checkbutton(root, onvalue=6, variable=checkbutton_room_color_deliberatly_chosen, text="Nein")
    room_color_deliberatly_chosen_checkbutton_no.grid(row=10, column=5, padx=5, pady=5)


    #room atmosphere
    room_atmosphere_label = ttk.Label(root, text="Zimmer Atmosphäre:")
    room_atmosphere_label.grid(row=11, column=0, padx=5, pady=5, sticky=tk.W)

    room_atmosphere_entry = ttk.Entry(root, textvariable=entry_room_atmosphere)
    room_atmosphere_entry.grid(row=11, column=1, padx=5, pady=5)

    #learning color
    learning_color_label = ttk.Label(root, text="Farbe zum Lernen:")
    learning_color_label.grid(row=12, column=0, padx=5, pady=5, sticky=tk.W)

    learning_color = StringVar(root)
    learning_color.set("-----")
    learning_color_optionmenu = ttk.OptionMenu(root, learning_color, "-----", "-----", "Weiß", "Gelb", "Orange", "Rot", "Rosa", "Violett", "Hellgrün", "Grün", "Hellblau", "Blau","Braun", "Grau", "Schwarz")
    learning_color_optionmenu.grid(row=12, column=1, padx=5, pady=5)

    learning_color_label_other = ttk.Label(root, text="Eingabe:")
    learning_color_label_other.grid(row=12, column=2, padx=5, pady=5, sticky=tk.E)

    learning_color_entry_other = ttk.Entry(root, textvariable=learning_color)
    learning_color_entry_other.grid(row=12, column=3, padx=5, pady=5)


    #relaxing color
    relaxing_color_label = ttk.Label(root, text="Farbe zum Entspannen:")
    relaxing_color_label.grid(row=13, column=0, padx=5, pady=5, sticky=tk.W)

    relaxing_color = StringVar(root)
    relaxing_color.set("-----")
    relaxing_color_optionmenu = ttk.OptionMenu(root, relaxing_color, "-----", "-----", "Weiß", "Gelb", "Orange", "Rot", "Rosa", "Violett", "Hellgrün", "Grün", "Hellblau", "Blau","Braun", "Grau", "Schwarz")
    relaxing_color_optionmenu.grid(row=13, column=1, padx=5, pady=5)

    relaxing_color_label_other = ttk.Label(root, text="Eingabe:")
    relaxing_color_label_other.grid(row=13, column=2, padx=5, pady=5, sticky=tk.E)

    relaxing_color_entry_other = ttk.Entry(root, textvariable=relaxing_color)
    relaxing_color_entry_other.grid(row=13, column=3, padx=5, pady=5)


    #word association red
    red_word_assoziation_label = ttk.Label(root, text="Wort-Assoziation Rot:" )
    red_word_assoziation_label.grid(row=14, column=0, padx=5, pady=5, sticky=tk.W)

    checkbutton_red = tk.IntVar()
    red_word_assoziation_checkbutton_love = ttk.Checkbutton(root, onvalue=8, variable=checkbutton_red, text="Liebe")
    red_word_assoziation_checkbutton_love.grid(row=14, column=1, padx=5, pady=5)

    red_word_assoziation_checkbutton_war = ttk.Checkbutton(root, onvalue=9, variable=checkbutton_red, text="Krieg/Brutalität")
    red_word_assoziation_checkbutton_war.grid(row=14, column=3, padx=5, pady=5)


    #flag association
    flag_assoziation_label = ttk.Label(root, text="Assoziation Flagge:")
    flag_assoziation_label.grid(row=15, column=0, padx=5, pady=5, sticky=tk.W)

    checkbutton_flag = tk.IntVar()
    flag_assoziation_checkbutton_yes = ttk.Checkbutton(root, onvalue=11, variable=checkbutton_flag, text="Ja")
    flag_assoziation_checkbutton_yes.grid(row=15, column=1, padx=5, pady=5)

    flag_assoziation_label_reason = ttk.Label(root, text="Bedeutung:")
    flag_assoziation_label_reason.grid(row=15, column=2, padx=5, pady=5, sticky=tk.E)

    flag_assoziation_entry_reason = ttk.Entry(root, textvariable=entry_flag)
    flag_assoziation_entry_reason.grid(row=15, column=3, padx=5, pady=5)

    flag_assoziation_checkbutton_no = ttk.Checkbutton(root, onvalue=12, variable=checkbutton_flag, text="Nein")
    flag_assoziation_checkbutton_no.grid(row=15, column=5, padx=5, pady=5)


    #sweet ingredients
    sweet_ingredients_label = ttk.Label(root, text="Interesse Süßigkeiten-Zutaten:")
    sweet_ingredients_label.grid(row=16, column=0, padx=5, pady=5, sticky=tk.W)

    sweet_ingredients = StringVar(root)
    sweet_ingredients.set("-----")
    sweet_ingredients_optionmenu = ttk.OptionMenu(root, sweet_ingredients, "-----", "-----", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
    sweet_ingredients_optionmenu.grid(row=16, column=1, padx=5, pady=5)


    #"Schlager" color
    schlager_color_label = ttk.Label(root, text="Farb-Assoziation Schlager:")
    schlager_color_label.grid(row=17, column=0, padx=5, pady=5, sticky=tk.W)

    schlager_color = StringVar(root)
    schlager_color.set("-----")
    schlager_color_optionmenu = ttk.OptionMenu(root, schlager_color, "-----", "-----", "Weiß", "Gelb", "Orange", "Rot", "Rosa", "Violett", "Hellgrün", "Grün", "Hellblau", "Blau","Braun", "Grau", "Schwarz")
    schlager_color_optionmenu.grid(row=17, column=1, padx=5, pady=5)

    schlager_color_label_other = ttk.Label(root, text="Eingabe:")
    schlager_color_label_other.grid(row=17, column=2, padx=5, pady=5, sticky=tk.E)

    schlager_color_entry_other = ttk.Entry(root, textvariable=schlager_color)
    schlager_color_entry_other.grid(row=17, column=3, padx=5, pady=5)


    #pop color
    pop_color_label = ttk.Label(root, text="Farb-Assoziation Pop:")
    pop_color_label.grid(row=18, column=0, padx=5, pady=5, sticky=tk.W)

    pop_color = StringVar(root)
    pop_color.set("-----")
    pop_color_optionmenu = ttk.OptionMenu(root, pop_color, "-----", "-----", "Weiß", "Gelb", "Orange", "Rot", "Rosa", "Violett", "Hellgrün", "Grün", "Hellblau", "Blau","Braun", "Grau", "Schwarz")
    pop_color_optionmenu.grid(row=18, column=1, padx=5, pady=5)

    pop_color_label_other = ttk.Label(root, text="Eingabe:")
    pop_color_label_other.grid(row=18, column=2, padx=5, pady=5, sticky=tk.E)

    pop_color_entry_other = ttk.Entry(root, textvariable=pop_color)
    pop_color_entry_other.grid(row=18, column=3, padx=5, pady=5)


    #classic color
    classic_color_label = ttk.Label(root, text="Farb-Assoziation Klassik:")
    classic_color_label.grid(row=19, column=0, padx=5, pady=5, sticky=tk.W)

    classic_color = StringVar(root)
    classic_color.set("-----")
    classic_color_optionmenu = ttk.OptionMenu(root, classic_color, "-----", "-----", "Weiß", "Gelb", "Orange", "Rot", "Rosa", "Violett", "Hellgrün", "Grün", "Hellblau", "Blau","Braun", "Grau", "Schwarz")
    classic_color_optionmenu.grid(row=19, column=1, padx=5, pady=5)

    classic_color_label_other = ttk.Label(root, text="Eingabe:")
    classic_color_label_other.grid(row=19, column=2, padx=5, pady=5, sticky=tk.E)

    classic_color_entry_other = ttk.Entry(root, textvariable=classic_color)
    classic_color_entry_other.grid(row=19, column=3, padx=5, pady=5)


    #rap color
    rap_color_label = ttk.Label(root, text="Farb-Assoziation Rap:")
    rap_color_label.grid(row=20, column=0, padx=5, pady=5, sticky=tk.W)

    rap_color = StringVar(root)
    rap_color.set("-----")
    rap_color_optionmenu = ttk.OptionMenu(root, rap_color, "-----", "-----", "Weiß", "Gelb", "Orange", "Rot", "Rosa", "Violett", "Hellgrün", "Grün", "Hellblau", "Blau","Braun", "Grau", "Schwarz")
    rap_color_optionmenu.grid(row=20, column=1, padx=5, pady=5)

    rap_color_label_other = ttk.Label(root, text="Eingabe:")
    rap_color_label_other.grid(row=20, column=2, padx=5, pady=5, sticky=tk.E)

    rap_color_entry_other = ttk.Entry(root, textvariable=rap_color)
    rap_color_entry_other.grid(row=20, column=3, padx=5, pady=5)


    #electro color
    electro_color_label = ttk.Label(root, text="Farb-Assoziation Elektro:")
    electro_color_label.grid(row=21, column=0, padx=5, pady=5, sticky=tk.W)

    electro_color = StringVar(root)
    electro_color.set("-----")
    electro_color_optionmenu = ttk.OptionMenu(root, electro_color, "-----", "-----", "Weiß", "Gelb", "Orange", "Rot", "Rosa", "Violett", "Hellgrün", "Grün", "Hellblau", "Blau","Braun", "Grau", "Schwarz")
    electro_color_optionmenu.grid(row=21, column=1, padx=5, pady=5)

    electro_color_label_other = ttk.Label(root, text="Eingabe:")
    electro_color_label_other.grid(row=21, column=2, padx=5, pady=5, sticky=tk.E)

    electro_color_entry_other = ttk.Entry(root, textvariable=electro_color)
    electro_color_entry_other.grid(row=21, column=3, padx=5, pady=5)


    #favorite color
    favourite_color_label = ttk.Label(root, text="Lieblingsfarbe:")
    favourite_color_label.grid(row=22, column=0, padx=5, pady=5, sticky=tk.W)

    favorite_color = StringVar(root)
    favorite_color.set("-----")
    favorite_color_optionmenu = ttk.OptionMenu(root, favorite_color, "-----", "-----", "Rot", "Orange", "Gelb", "Grün", "Blau", "Hellblau", "Violett", "Weiß", "Rosa", "Grau","Schwarz", "Braun")
    favorite_color_optionmenu.grid(row=22, column=1, padx=5, pady=5)

    checkbutton_favorite_color = tk.IntVar()
    favorite_color_personality_Checkbutton_yes = ttk.Checkbutton(root, onvalue=14, variable=checkbutton_favorite_color, text="Passt")
    favorite_color_personality_Checkbutton_yes.grid(row=22, column=2, padx=5, pady=5)

    favorite_color_personality_Checkbutton_no = ttk.Checkbutton(root, onvalue=15, variable=checkbutton_favorite_color, text="Passt nicht")
    favorite_color_personality_Checkbutton_no.grid(row=22, column=3, padx=5, pady=5)

    favorite_color_personality_Checkbutton_inbetween = ttk.Checkbutton(root, onvalue=16, variable=checkbutton_favorite_color, text="Passt halbwegs")
    favorite_color_personality_Checkbutton_inbetween.grid(row=22, column=5, padx=5, pady=5)

    #submit
    submit_button = ttk.Button(root, text="Abschicken",  command=submit_form)
    submit_button.grid(row=23, column=7, padx=5, pady=5, sticky=tk.E)


def save_values_in(form):
    global entry_age
    form_manager.to_form(form,
                        entry_age.get(),
                        checkbutton_sex.get(),
                        entry_culture.get(),
                        luck_color.get(),
                        entry_luck_reason.get(),
                        closet_color.get(),
                        noble_color_1.get(),
                        noble_color_2.get(),
                        quality_1.get(),
                        quality_2.get(),
                        car.get(),
                        learning_color.get(),
                        relaxing_color.get(),
                        red_entry.get(),
                        room_color.get(),
                        checkbutton_room_color_deliberatly_chosen.get(),
                        entry_room_color_reason.get(),
                        entry_room_atmosphere.get(),
                        checkbutton_red.get(),
                        checkbutton_flag.get(),
                        entry_flag.get(),
                        sweet_ingredients.get(),
                        schlager_color.get(),
                        pop_color.get(),
                        classic_color.get(),
                        rap_color.get(),
                        electro_color.get(),
                        favorite_color.get(),
                        checkbutton_favorite_color.get())
    log("saved values")


def reset():
    global root

    global entry_age
    global entry_luck_reason
    global red_entry
    global entry_room_color_reason
    global entry_room_atmosphere
    global entry_flag
    
    #clears entire window, so that it can be newly written on
    for widget in root.winfo_children():
        widget.destroy()

    #resetting text of entry boxes
    entry_age.set('')
    entry_luck_reason.set('')
    red_entry.set('')
    entry_room_color_reason.set('')
    entry_room_atmosphere.set('')
    entry_flag.set('')

    log("reset window\n")
    #there probably is a way more elegant way to do this rather than simply redrawing the entire thing, but it works so stfu
    setup()


#get variables to form.py
def submit_form():
    try:
        log("submit button pressed")
        save_values_in(form_manager.form)
        form_manager.on_form_submit(form_manager.form)
        reset()
    except Exception as e:
        log("uncaught exception durin submit operation:\n" + str(traceback.print_exception(type(e), e, e.__traceback__)) + "\n")
    
#------------------------------------------------------------------------------------------------------
#all stuff essential for program execution

def run():
    setup()
    root.mainloop()
