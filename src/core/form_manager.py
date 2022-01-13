#containing all functions necessary to perform actions on an instance of the form class
from core.form import Form
from core import file
import os.path
import traceback

form = Form()
WORKING_DIR = os.path.abspath(os.path.dirname(__file__))
RESULTS_DIR = os.path.abspath(WORKING_DIR + "/../../.data/results") 


def log(message):
    with open(os.path.abspath(WORKING_DIR + "/../../.data/log.txt"), "a") as log:
        log.write("form_manager.py: " + message + "\n")

def on_form_submit(form : Form):
    log("received data")
    form_data = to_row(form)
    log("transformed data to row")
    dir = get_file_dir(form.age)
    log("got file directory: " + dir)
    try:
        file.append_csv(dir, form_data)
        log("appended to csv file")
    except FileNotFoundError as fne:
        log("File Not Found exception:\n" + str(traceback.print_exception(type(fne), fne, fne.__traceback__)) + "\n")
    form.reset()
    

def get_file_dir(age):
    log("received age: " + str(age))
    file = "age" + str(age)
    if age <= 9:
        file += "_minus"
    elif age == 18: #TODO when combining everything together, add all values belonging in here to here
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
    if fc == 16:
        return "teilweise"
    return None


#bEaUtIfUl ClEaN cOdE
def to_form(form : Form, a, s, c, lc, lr, cclauset, cnoble, cnoble2, chq, chq2, ccar, clearn, crelax, ar, rc, cd, 
            cdr, ra, mr, kf, fm, ci, mgs, mgp, mgc, mgr, mge, fc, fp):
    if a:
        form.age = int(a)
    if eval_sex(s): #yeah fuck data redundancy and unnessecary compution
        form.sex = eval_sex(s).lower()
    form.culture = c.lower()
    if lc != "-----":
        form.luck["color"] = lc.lower()
    form.luck["reason"] = lr.lower()
    if cclauset != "-----":
        form.color["clauset"] = cclauset.lower()
    if cnoble != "-----":
        form.color["noble"] = cnoble.lower()
    if cnoble2 != "-----":
        form.color["noble 2"] = cnoble2.lower()
    if chq != "-----":
        form.color["high-quality"] = chq.lower()
    if chq2 != "-----":
        form.color["high-quality 2"] = chq2.lower()
    if ccar != "-----":
        form.color["car"] = ccar.lower()
    if clearn != "-----":
        form.color["learning"] = clearn.lower()
    if crelax != "-----":
        form.color["relaxing"] = crelax.lower()
    form.association_red = ar.lower()
    if rc != "-----":
        form.room["color"] = rc.lower()
    form.room["conscious decision"] = eval_decision(cd)
    form.room["reason"] = cdr.lower()
    form.room["ambience"] = ra.lower()
    if eval_red(mr):
        form.meaning_red = eval_red(mr).lower()
    form.knows_flag = eval_flag(kf)
    form.flag_meaning = fm.lower()
    if ci and ci != "-----":
        form.check_ingredients = int(ci)
    if mgs != "-----":
        form.music_genre["schlager"] = mgs.lower()
    if mgp != "-----":
        form.music_genre["pop"] = mgp.lower()
    if mgc != "-----":
        form.music_genre["classic"] = mgc .lower()
    if mgr != "-----":
        form.music_genre["rap"] = mgr.lower()
    if mge != "-----":
        form.music_genre["electro"] = mge .lower()
    if fc != "-----":
        form.favourite_color = fc.lower()
    form.fits_personality = eval_fav_color(fp)


#for real tho all these functions are terrible
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
