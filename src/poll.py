from shell import gui
from core import form_manager
import os
import traceback

try:
    gui.run()
except Exception as e:
    f = open(os.path.abspath(form_manager.WORKING_DIR + "/../../.data/log.txt"), "a")
    f.write("poll.py: uncaught exception:\n" + str(traceback.print_exception(type(e),e, e.__traceback__)) + "\n")
    f.close()
