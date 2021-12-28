#REPRESENT THE INPUT IN PYTHON DATA TYPES BEFORE WRITING TO FILES
# @FINN TODO: convert input from GUI to an instance of this class


class Form:
    def __init__(self):
        self.age = None
        self.sex = None
        self.culture = None
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
        self.association_red = None
        self.room = {
            "color": None,
            "conscious decision": None,
            "reason": None,
            "ambience": None,
        }
        self.meaning_red = None  # war ? brutality
        self.flag = [[True, None], False] #flag[0][1] represents meaning of flag given by participant
        self.check_ingredients: int = None
        self.music_genre = {
            "schlager": None,
            "pop": None,
            "classic": None,
            "rap": None,
            "electro": None
        }
        self.favourite_color = None
        self.fits_personality: bool = None
