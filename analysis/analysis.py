from lib import file as csv
import os
import glob
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
        if tokens[1] == '*':
            print_all_filenames()
        else:
            bs.file(get_file_dir(tokens[1]))
    elif tokens[0] == "filter":
        bs.filter(tokens)
    elif tokens[0] == "save":
        bs.save(tokens[1])
    pass

#this was way too much fucking work
def tokenize(inp):
    tokens = inp.split(' ')
    
    #while loop instead of for loop required, because length of tokens list gets modified inside loop
    i = 0
    while i < len(tokens):
        if '==' in tokens[i] and len(tokens[i]) > 2: #checking for length makes sure that '==' items get skipped
            t_token = tokens[i].split("==")
            if '' in t_token:
                if tokens[i][0] == '=': t_token.insert(0, '==')
                else: t_token.insert(1, '==') #if token does not begin with '==', it has to be inserted at index 1
            else: t_token.insert(1, '==')

            #replaces original token with modified parts of t_token
            del tokens[i]
            while '' in t_token: t_token.remove('')
            for j in range(len(t_token)):
                tokens.insert(i + j, t_token[j])

        elif '=' in tokens[i] and len(tokens[i]) > 1 and not '==' in tokens[i]:
            t_token = tokens[i].split("=")
            if '' in t_token:
                if tokens[i][0] == '=': t_token.insert(0, '=')
                else: t_token.insert(1, '=')
            else: t_token.insert(1, '=')

            del tokens[i]
            while '' in t_token: t_token.remove('')
            for j in range(len(t_token)):
                tokens.insert(i + j, t_token[j])


        #TODO still add all of this shit for '>' and '<' signs -> create seperate function
        i += 1

    return tokens

def get_file_dir(f):
    return RESULTS_DIR + '/' + f


def print_all_filenames():
    files = glob.glob(RESULTS_DIR + "/*")
    for filename in files:
        print(filename.replace(RESULTS_DIR + '\\', ''))

if __name__ == "__main__":
    while True:
        run_console_dialogue()
