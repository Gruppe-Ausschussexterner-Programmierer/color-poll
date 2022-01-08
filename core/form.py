#REPRESENT THE INPUT IN PYTHON DATA TYPES BEFORE WRITING TO FILES
# @FINN TODO: convert input from GUI to an instance of this class

from shell.gui import *

class Form:
    def __init__(self):
        self.age: int = None 
        self.sex: int = None
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
            "conscious decision": None,
            "reason": None,
            "ambience": None,
        }
        self.meaning_red: int = None
        self.knows_flag : int = None
        self.flag_meaning : str = None
        self.check_ingredients : str = None
        self.music_genre = {
            "schlager": None,
            "pop": None,
            "classic": None,
            "rap": None,
            "electro": None
        }
        self.favourite_color : str = None
        self.fits_personality: int = None

    def reset(self):
        self.age = None
        self.sex = None
        self.culture = None
        self.luck["color"] = None
        self.luck["reason"] = None
        self.color["clauset"] = None
        self.color["noble"] = None
        self.color["noble 2"] = None
        self.color["high-quality"] = None
        self.color["high-quality 2"] = None
        self.color["car"] = None
        self.color["learning"] = None
        self.color["relaxing"] = None
        self.association_red = None
        self.room["color"] = None
        self.room["conscious decision"] = None
        self.room["reason"] = None
        self.room["ambience"] = None
        self.meaning_red = None
        self.knows_flag = None
        self.flag_meaning = None
        self.check_ingredients = None
        self.music_genre["schlager"] = None
        self.music_genre["pop"] = None
        self.music_genre["classic"] = None
        self.music_genre["rap"] = None
        self.music_genre["electro"] = None
        self.favourite_color = None
        self.fits_personality = None
