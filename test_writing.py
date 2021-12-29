from core.form import Form
from core import form_manager
import core.file

def create_temp_form(form : Form):
    tf.age = int(input("age "))
    tf.sex = input("sex ")
    tf.culture = input("culture ")
    tf.luck["color"] = input("luck color ")
    tf.luck["reason"] = input("reason ")
    tf.color["clauset"] = input("color clauset ")
    tf.color["noble"] = input("color noble ")
    tf.color["high-quality"] = input("color high-quality ")
    tf.color["car"] = input("color car ")
    tf.color["learning"] = input("color learning ")
    tf.color["relaxing"] = input("color relaxing ")
    tf.association_red = input("association red ")
    tf.room["color"] = input("room color ")
    tf.room["conscious decision"] = input("conscious decision ")
    tf.room["reason"] = input("reason ")
    tf.room["ambience"] = input("room ambience ")
    tf.meaning_red = input("meaning red ")
    tf.flag_meaning = input("flag meaning ")
    tf.check_ingredients = int(input("check ingredients "))
    tf.music_genre["schlager"] = input("schlager ")
    tf.music_genre["pop"] = input("pop ")
    tf.music_genre["classic"] = input("classic ")
    tf.music_genre["rap"] = input("rap ")
    tf.music_genre["electro"] = input("electro ")
    tf.favourite_color = input("favourite color ")
    tf.fits_personality = eval(input("fits personality "))

if __name__ == "__main__":
    tf = Form()
    create_temp_form(tf)
    #print(form_manager.WORKING_DIR)
    form_manager.on_form_submit(tf)
