#REPRESENT THE INPUT IN PYTHON DATA TYPES BEFORE WRITING TO FILES
# @FINN TODO: convert input from GUI to an instance of this class

from shell.gui import *

class Form:
    def __init__(self):
        self.age: int = None  # @SCHLÄGER TODO: convert to int (is str rn)
        self.sex: str = None  # 0->None, 1->Male, 2->Female, 3->Other
        self.culture: str = None
        self.luck = {
            "color": None,
            "reason": None
        }
        self.color = {
            "clauset": None,
            "noble": None,
            "noble 2" : None,
            "high-quality": None,
            "high-quality 2": None,
            "car": None,
            "learning": None,
            "relaxing": None,
        }
        self.association_red: str = None
        self.room = {
            "color": None,
            "conscious decision": None,  # 0->None, 1->Yes, 2->No
            "reason": None,
            "ambience": None,
        }
        self.meaning_red: int = None  # 0->None, 1->Love, 2->War
        self.knows_flag : bool = None # 0->None, 1->Yes, 2->No
        self.flag_meaning : str = None
        self.check_ingredients : int = None # @SCHLÄGER TODO: convert to int (is str rn)
        self.music_genre = {
            "schlager": None,
            "pop": None,
            "classic": None,
            "rap": None,
            "electro": None
        }
        self.favourite_color : str = None
        self.fits_personality: bool = None  # 0->None, 1->Yes, 2->No
