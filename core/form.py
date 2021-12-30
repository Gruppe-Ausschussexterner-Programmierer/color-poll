#REPRESENT THE INPUT IN PYTHON DATA TYPES BEFORE WRITING TO FILES
# @FINN TODO: convert input from GUI to an instance of this class

from shell.gui import *

class Form:
    def __init__(self):
        self.age : int = entry_age # @SCHLÄGER TODO: convert to int (is str rn)
        self.sex : int = checkbutton_sex # 0->None, 1->Male, 2->Female, 3->Other
        self.culture : str = entry_culture
        self.luck = {
            "color": luck_color,
            "reason": entry_luck_reason
        }
        self.color = {
            "clauset": closet_color,
            "noble": noble_color_1, # @SCHLÄGER TODO: add a second noble color
            "high-quality": quality_2, # @SCHLÄGER TODO: add a second high-quality color
            "car": car,
            "learning": learning_color,
            "relaxing": relaxing_color,
        }
        self.association_red : str = red_entry
        self.room = {
            "color": room_color,
            "conscious decision": checkbutton_room_color_deliberatly_chosen, # 0->None, 1->Yes, 2->No
            "reason": entry_room_color_reason,
            "ambience": entry_room_atmosphere,
        }
        self.meaning_red : int = checkbutton_red # 0->None, 1->Love, 2->War
        self.flag_meaning : int = checkbutton_flag # 0->None, 1->Yes, 2->No
        self.check_ingredients : int = sweet_ingredients # @SCHLÄGER TODO: convert to int (is str rn)
        self.music_genre = {
            "schlager": schlager_color,
            "pop": pop_color,
            "classic": classic_color,
            "rap": rap_color,
            "electro": electro_color
        }
        self.favourite_color : str = favorite_color
        self.fits_personality : int = checkbutton_favorite_color # 0->None, 1->Yes, 2->No
