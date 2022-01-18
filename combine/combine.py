import csv
import io
import os
import glob
import time

RESULTS_FINAL = "c:/Coding Stuff/GAP/color-poll/combine/results_final/"

def read_csv(file):
    file_content = []
    with io.open(file, "r", encoding='utf-8') as rf:
        reader = csv.reader(rf, quotechar='"', delimiter=';',
                            quoting=csv.QUOTE_MINIMAL, skipinitialspace=True)
        for row in reader:
            if(row):
                file_content.append(row)
        rf.close()
    return file_content


def append_csv(file, new_content):
    with open(file, "a", newline='', encoding="utf-8")as wf:
        writer = csv.writer(wf, delimiter=';', quotechar='"',
                            quoting=csv.QUOTE_MINIMAL)
        writer.writerow(new_content)
        wf.close()

def get_master_file(age_str):
    try:
        age = int(age_str)
        file = "master_age" + age_str
    except:
        age = None
        file ="master_ageNone"
    
    if age:
        if age <= 9:
            file = "master_age9_minus"
        if age == 18:
            file = "master_age18_plus"
    file += ".csv"

    return file

if __name__ == "__main__":
    for dir in glob.glob(os.path.dirname(__file__) + "\\results_import/*"):
        print("\ndirectory: " + dir)
        time.sleep(1)
        for file in glob.glob(dir + "/*"):
            if not "overall.csv" in file:
                file_content = read_csv(file)

                file_location = file.replace(dir + "\\", '')
                print(file_location)
                for row in file_content:
                    master_file = get_master_file(row[0])
                    append_csv(RESULTS_FINAL + master_file, row)
                    append_csv(RESULTS_FINAL + "overall.csv", row)
                
                    try:
                        if int(row[0]) > 18: #only > instead of >= since 18 year olds are already stored in that file
                            append_csv(RESULTS_FINAL + "master_age18_plus.csv", row)
                    except:
                        pass
                time.sleep(.25)
