call-it-official documentation of "Bullshit Query Language" (short: BSQL)

# part of the project "color-poll" developed by GAP
# tool to specifically analyze the results of that poll
# author: Emil Schläger
# name is definitely not a knock-off of SQL
-----
english:

In here, you will find a documentation of how to use the console dialogue. There will also be a graphical user interface, however that will take longer and should be self-explanatory.

----
(Bei Betrachten der Nutzer ist eine deutsche Version vermutlich angebracht) deutsch:

---
list of commands:
> file `filename`
> file *

> filter not `filter` and `filter` or `filter` ...
    (`filter`:
        a = b
        a == b
        a > b
        a < b )

        DOES NOT SUPPORT <= OR >= OPERATORS
> filter exclude `filter` (-> does 'not' serve exact same purpose?)

> view 

> save `new_file`
