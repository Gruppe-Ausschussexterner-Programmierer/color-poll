#REPRESENT THE INPUT IN PYTHON DATA TYPES BEFORE WRITING TO FILES
# @FINN TODO: convert input from GUI to an instance of this class

class Form:
    def __init__(self):
        self.age : int = None
        self.sex : str = None
        self.culture : str = None
        self.luck = {
            "color": None,
            "reason": None
        }
        self.color = {
            "clauset": None,
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
