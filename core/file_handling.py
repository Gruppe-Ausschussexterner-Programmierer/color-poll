import csv

def read_csv(file):
    file_content = []
    with io.open(file, "r", encoding='utf-8') as rf:
        reader = csv.reader(rf, quotechar='"', delimiter=';', quoting=csv.QUOTE_MINIMAL, skipinitialspace=True)
        for row in reader:
            if(row):
                file_content.append(row)
        rf.close()
    return file_content

def append_csv(file, new_content):
    with open(file, "a", newline='', encoding="utf-8")as wf:
        writer = csv.writer(wf, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(new_content)
        wf.close()

