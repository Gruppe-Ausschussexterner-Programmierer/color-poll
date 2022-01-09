#EXECUTE THIS, OTHERWISE BACKEND WON'T FIND CSV FILES
from shell import gui
try:
    gui.run()
except Exception as e:
    f = open("/.data/log.txt", "a")
    f.writeline("poll.py: " + e.with_traceback() + "\n")
    f.close()