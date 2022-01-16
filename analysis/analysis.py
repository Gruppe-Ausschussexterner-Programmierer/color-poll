#TODO: add 2 ways of comparing strings: '=' for checking for word being in string; '==' for absolute comparison

from core import file as csv
import os
from core.form_manager import RESULTS_DIR

WORKING_DIR = os.path.abspath(os.path.dirname(__file__))
RESULTS_DIR = os.path.abspath(WORKING_DIR + "/../../../.data/results/")


data = None
filtered = None

def run():
    pass

def tokenize(inp):
    return inp.split(" ")

def e(f):
    return RESULTS_DIR + f
