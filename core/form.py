#REPRESENT THE INPUT IN PYTHON DATA TYPES BEFORE WRITING TO FILES
# @FINN TODO: convert input from GUI to an instance of this class

from shell.gui import entry_age, checkbutton_sex, entry_culture, luck_color, entry_luck_reason, closet_color

class Form:
    def __init__(self):
        self.age : int = entry_age #TODO: convert to int (is str rn)
        self.sex : int = checkbutton_sex # 0->None, 1->Male, 2->Female, 3->Other
        self.culture : str = entry_culture
        self.luck = {
            "color": luck_color,
            "reason": entry_luck_reason
        }
        self.color = {
            "clauset": closet_color,
            "noble": None,
            "high-quality": None,
            "car": None,
            "learning": None,
            "relaxing": None,
        }
        self.association_red : str = None
        self.room = {
            "color": None,
            "conscious decision": None,
            "reason": None,
            "ambience": None,
        }
        self.meaning_red : str = None  # war ? brutality
        self.flag_meaning : str = None #leave None when participant didn't know
        self.check_ingredients : int = None
        self.music_genre = {
            "schlager": None,
            "pop": None,
            "classic": None,
            "rap": None,
            "electro": None
        }
        self.favourite_color : str = None
        self.fits_personality : bool = None
