from lib import file as csv
import os
from bsql import bsql as bs

WORKING_DIR = os.path.abspath(os.path.dirname(__file__))
RESULTS_DIR = os.path.abspath(WORKING_DIR + "/../.data/results/")

#TODO functionality: add a default way to deal with filter requests without destroying data set and having to reload it

#TODO command: receive total amounts of entries for selected data set
#TODO command: on save: select a way to sort entries
#TODO command: view every stat of current data set

#TODO command file: add way to view all existing files and their name

def run_console_dialogue():
    command = input("> ")
    tokens = tokenize(command)

    if tokens[0] == "file":
        bs.file(get_file_dir(tokens[1]))
    elif tokens[0] == "filter":
        bs.filter(tokens)
    elif tokens[0] == "save":
        bs.save(tokens[1])
    pass

#TODO add way to deal with filter being given without spaces around '=' sign
def tokenize(inp):
    return inp.split(" ")

def get_file_dir(f):
    return RESULTS_DIR + '/' + f

if __name__ == "__main__":
    while True:
        run_console_dialogue()
