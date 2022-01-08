#containing all functions necessary to perform actions on an instance of the form class
#from form import Form
from core.form import Form
from core import file
import os.path

form = Form()
WORKING_DIR = os.path.abspath(os.path.dirname(__file__))
RESULTS_DIR = os.path.abspath(WORKING_DIR + "/../.data/results") 

def on_form_submit(form : Form):
    form_data = to_row(form)
    dir = get_file_dir(form.age)
    file.append_csv(dir, form_data)
    form.reset()
    

def get_file_dir(age):
    file = "age" + str(age)
    if age == 9:
        file += "_minus"
    elif age == 18:
        file += "_plus"
    file += ".csv"

    return os.path.abspath(RESULTS_DIR + "/" + file)

def eval_sex(s):
    if s == 0:
        return None
    elif s == 1:
        return "männlich"
    elif s == 2:
        return "weiblich"
    return "andere"

def eval_decision(d):
    if d == 5:
        return True
    if d == 6:
        return False
    return None

def eval_red(r):
    if r == 8:
        return "liebe"
    if r == 9:
        return "krieg"
    return None

def eval_flag(f):
    if f == 11:
        return True
    if f == 12:
        return False
    return None

def eval_fav_color(fc):
    if fc == 14:
        return True
    if fc == 15:
        return False
    return None


#bEaUtIfUl ClEaN cOdE
def to_form(form : Form, a, s, c, lc, lr, cclauset, cnoble, cnoble2, chq, chq2, ccar, clearn, crelax, ar, rc, cd, 
            cdr, ra, mr, kf, fm, ci, mgs, mgp, mgc, mgr, mge, fc, fp):
    if a:
        form.age = int(a)
    form.sex = eval_sex(s)
    form.culture = c
    if lc != "-----":
        form.luck["color"] = lc
    form.luck["reason"] = lr
    if cclauset != "-----":
        form.color["clauset"] = cclauset
    if cnoble != "-----":
        form.color["noble"] = cnoble
    if cnoble2 != "-----":
        form.color["noble 2"] = cnoble2
    if chq != "-----":
        form.color["high-quality"] = chq
    if chq2 != "-----":
        form.color["high-quality 2"] = chq2
    if ccar != "-----":
        form.color["car"] = ccar
    if clearn != "-----":
        form.color["learning"] = clearn
    if crelax != "-----":
        form.color["relaxing"] = crelax
    form.association_red = ar
    if rc != "-----":
        form.room["color"] = rc
    form.room["conscious decision"] = eval_decision(cd)
    form.room["reason"] = cdr
    form.room["ambience"] = ra
    form.meaning_red = eval_red(mr)
    form.knows_flag = eval_flag(kf)
    form.flag_meaning = fm
    if ci and ci != "-----":
        form.check_ingredients = int(ci)
    if mgs != "-----":
        form.music_genre["schlager"] = mgs
    if mgp != "-----":
        form.music_genre["pop"] = mgp
    if mgc != "-----":
        form.music_genre["classic"] =mgc 
    if mgr != "-----":
        form.music_genre["rap"] = mgr
    if mge != "-----":
        form.music_genre["electro"] = mge 
    if fc != "-----":
        form.favourite_color = fc
    form.fits_personality = eval_fav_color(fp)


#for real tho all these functions are terrible
#TODO @Schläger: convert all strings to lower on csv writing
def to_row(form : Form):
    csv_entries = []
    csv_entries.append(form.age)
    csv_entries.append(form.sex)
    csv_entries.append(form.culture)
    csv_entries.append(form.luck["color"])
    csv_entries.append(form.luck["reason"])
    csv_entries.append(form.color["clauset"])
    csv_entries.append(form.color["noble"])
    csv_entries.append(form.color["noble 2"])
    csv_entries.append(form.color["high-quality"])
    csv_entries.append(form.color["high-quality 2"])
    csv_entries.append(form.color["car"])
    csv_entries.append(form.association_red)
    csv_entries.append(form.room["color"])
    csv_entries.append(form.room["conscious decision"])
    csv_entries.append(form.room["reason"])
    csv_entries.append(form.room["ambience"])
    csv_entries.append(form.color["learning"])
    csv_entries.append(form.color["relaxing"])
    csv_entries.append(form.meaning_red)
    csv_entries.append(form.knows_flag)
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
