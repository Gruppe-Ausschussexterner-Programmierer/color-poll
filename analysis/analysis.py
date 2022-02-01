from lib import file as csv
import os
import glob
from bsql import bsql as bs

WORKING_DIR = os.path.abspath(os.path.dirname(__file__))
RESULTS_DIR = os.path.abspath(WORKING_DIR + "/../.data/results/")


#TODO functionality: filter for colour? (or at least view occurances of attributes per colour)
#TODO functionality: add syntactically more helpful error handling
#TODO command: on save: select a way to sort entries
#TODO command: help command showing every possible command and a brief description of it

def bsql(command):
    tokens = tokenize(command)

    if tokens[0] == "file":
        if tokens[1] == '*':
            print_all_filenames()
        else:
            bs.file(get_file_dir(tokens[1]))
    elif tokens[0] == "filter":
        bs.filter(tokens)
    elif tokens[0] == "view":
        bs.view(tokens)
    elif tokens[0] == "save":
        if tokens[1] == "overall.csv":  # protecting overall.csv from being overridden
            print("cannot override overall.csv")
        else:
            bs.save(get_file_dir(tokens[1]))


def run_console_dialogue():
    command = input("> ").lower()
    bsql(command)

#this was way too much fucking work
def tokenize(inp):
    tokens = inp.split(' ')
    
    #while loop instead of for loop required, because length of tokens list gets modified inside loop
    i = 0
    while i < len(tokens):
        if '==' in tokens[i] and len(tokens[i]) > 2: #checking for length makes sure that '==' items get skipped
            split_filter_at("==", tokens, i)
        elif '=' in tokens[i] and not '==' in tokens[i] and len(tokens[i]) > 1:
            split_filter_at('=', tokens, i)
        elif '<' in tokens[i] and len(tokens[i]) > 1:
            split_filter_at('<', tokens, i)
        elif '>' in tokens[i] and len(tokens[i]) > 1:
            split_filter_at('>', tokens, i)
        elif '*' in tokens[i] and len(tokens[i]) > 1:
            split_filter_at('*', tokens, i)
        i += 1

    return tokens


def split_filter_at(operator, tokens, i):
    t_token = tokens[i].split(operator)
    if '' in t_token:
        if tokens[i][0] == operator:
            t_token.insert(0, operator)
        # if token does not begin with `operator`, it has to be inserted at index 1
        else: t_token.insert(1, operator)
    else: t_token.insert(1, operator)

    #replaces original token with modified parts of t_token
    del tokens[i]
    while '' in t_token:
        t_token.remove('')
    for j in range(len(t_token)):
        tokens.insert(i + j, t_token[j])


def get_file_dir(f):
    return RESULTS_DIR + '\\' + f


def print_all_filenames():
    files = glob.glob(RESULTS_DIR + "/*")
    for filename in files:
        print(filename.replace(RESULTS_DIR + '\\', ''))


if __name__ == "__main__":
    print("# BSQL v1.1.1\n# developed by GAP as part of the 'color-poll' project\n"
    "# check README.txt or Dokumentation_Deutsch.txt for use guide\n\n")
    while True:
        try:
            run_console_dialogue()
        except:
            print("invalid syntax")
