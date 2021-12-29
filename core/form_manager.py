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
