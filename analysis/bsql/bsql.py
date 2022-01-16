from lib import file as csv

DATA_SELECTED = None
DATA_FILTERED = None

def file(f_dir):
    global DATA_SELECTED

    DATA_SELECTED = csv.read_csv(f_dir)
    print(str(len(DATA_SELECTED)) + " entries selected")

    #room for potential further operations to perform on a file

def save(nf):
    print("save command")

#allows for more detailed filtering of selected data set7
#TODO: add 2 ways of comparing strings: '=' for checking for word being in string; '==' for absolute comparison
#TODO: add exclude function (> filter exclude age = 13)
#TODO: select as many filters as wished, seperate with either commas or semicolons
def filter(f):
    print("filter command")

#allows to view every entry in selected data formatted
def view():
    pass
