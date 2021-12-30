#containing all functions necessary to perform actions on an instance of the form class
#from form import Form
from core.form import Form
from core import file
import os.path

WORKING_DIR = os.path.abspath(os.path.dirname(__file__))
RESULTS_DIR = os.path.abspath(WORKING_DIR + "/../.data/results") 

#TODO: test this
def on_form_submit(form : Form):
    form_data = to_row(form)
    dir = get_file_dir(form.age)
    file.append_csv(dir, form_data)
    

def get_file_dir(age):
    file = "age" + str(age)
    if age == 9:
        file += "_minus"
    elif age == 18:
        file += "_plus"
    file += ".csv"

    return os.path.abspath(RESULTS_DIR + "/" + file)

def to_form(form : Form, a, s, c, lc, lr, cclauset, cnoble, cnoble2, chq, chq2, ccar, clearn, crelax, ar, rc, cd, 
            cdr, ra, mr, kf, fm, ci, mgs, mgp, mgc, mgr, mge, fc, fp):
    form.age = int(a)
    form.sex = s
    form.culture = c
    form.luck["color"] = lc
    form.luck["reason"] = lr
    form.color["clauset"] = cclauset
    form.color["noble"] = cnoble
    form.color["noble 2"] = cnoble2
    form.color["high-quality"] = chq
    form.color["high-quality 2"] = chq2
    form.color["car"] = ccar
    form.color["learning"] = clearn
    form.color["relaxing"] = crelax
    form.association_red = ar
    form.room["color"] = rc
    form.room["conscious decision"] = cd
    form.room["reason"] = cdr
    form.room["ambience"] = ra
    form.meaning_red = mr
    form.knows_flag = kf
    form.flag_meaning = fm
    form.check_ingredients = int(ci)
    form.music_genre["schlager"] = mgs
    form.music_genre["pop"] = mgp
    form.music_genre["classic"] =mgc 
    form.music_genre["rap"] = mgr
    form.music_genre["electro"] = mge 
    form.favourite_color = fc
    form.fits_personality = fp


def to_row(form : Form):
    csv_entries = []
    csv_entries.append(form.age)
    csv_entries.append(form.sex)
    csv_entries.append(form.culture)
    csv_entries.append(form.luck["color"])
    csv_entries.append(form.luck["reason"])
    csv_entries.append(form.color["clauset"])
    csv_entries.append(form.color["noble"])
    csv_entries.append(form.color["high-quality"])
    csv_entries.append(form.color["car"])
    csv_entries.append(form.color["learning"])
    csv_entries.append(form.color["relaxing"])
    csv_entries.append(form.association_red)
    csv_entries.append(form.room["color"])
    csv_entries.append(form.room["conscious decision"])
    csv_entries.append(form.room["reason"])
    csv_entries.append(form.room["ambience"])
    csv_entries.append(form.meaning_red)
    csv_entries.append(form.flag_meaning)
    csv_entries.append(form.check_ingredients)
    csv_entries.append(form.music_genre["schlager"])
    csv_entries.append(form.music_genre["pop"])
    csv_entries.append(form.music_genre["classic"])
    csv_entries.append(form.music_genre["rap"])
    csv_entries.append(form.music_genre["electro"])
    csv_entries.append(form.favourite_color)
    csv_entries.append(form.fits_personality)

    return csv_entries
