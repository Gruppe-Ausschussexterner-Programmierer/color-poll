from lib import file as csv

DATA_SELECTED = None
DATA_FILTERED = None

def file(f_dir):
    global DATA_SELECTED

    DATA_SELECTED = csv.read_csv(f_dir)
    print(str(len(DATA_SELECTED)) + " entries selected")

    #room for potential further operations to perform on a file

#TODO: add 2 ways of comparing strings: '=' for checking for word being in string; '==' for absolute comparison
#TODO: add exclude function (> filter exclude age = 13)

#allows for more detailed filtering of selected data set
#@param cm: input tokenized command 
def filter(cm):
    global DATA_SELECTED

    #DATA_FILTERED = DATA_SELECTED  # from here on out, only work on DATA_FILTERED

    command = cm.copy()
    command.remove(command[0]) #gets rid of unnecessary 'filter' key word

    filters = []
    for i in range(len(command)):
        if is_logical_operator(command[i]):
            filters.append(command[i])
        if is_comparison_operator(command[i]):
            filters.append([command[i - 1], command[i], command[i + 1]])

    #TODO add bigger_than
    #TODO handle boolean values
    #TODO try catches
    for row in DATA_SELECTED:
        filter_applied = []
        for filter in filters:
            if type(filter) == list:
                operator = filter[1]
                name = filter[0]
                value = filter[2]
                if operator == '==':
                    filter_applied.append(double_equals(get_value(row, name), value))
                elif operator == '=':
                    filter_applied.append(single_equals(get_value(row, name), value))
                elif operator == '<':
                    filter_applied.append(smaller_than(get_value(row, name), value))
            else:
                filter_applied.append(filter)
    print("done filtering")
    pass


def save(nf):
    print("save command")

#allows to view every entry in selected data formatted
def view():
    pass

#TODO check for a and b bein integers, otherwise it won't work
def smaller_than(a, b):
    pass

def single_equals(a, b):
    try:
        return int(a) == int(b)
    except ValueError: #either a or b cannot be converted to int type
        return str(b) in str(a)


def double_equals(a, b):
    return a == b


def is_logical_operator(token):
    if token == "and": return True  #TODO handle operator
    if token == "or": return True #TODO handle operator
    if token == "not": return True #TODO handle operator
    return False


def is_comparison_operator(token):
    if token == '=': return True 
    if token == '==': return True
    if token == '>': return True #TODO handle operator
    if token == '<': return True #TODO handle operator
    return False


def get_value(row, col : str):
    index = get_column(col)
    if type(index) == tuple:
        val1 = row[index[0]]
        val2 = row[index[1]]
        value = str(val1) + str(val2)
    else:
        value = row[index]

    try:
        return int(value)
    except ValueError:
        pass
    try: 
        return eval(value)
    except Exception:
        pass

    return value


#could be done way more elegantly by simply saving everything inside of a dictionary but who cares
#code: perfectly clean, readable and structured -> bsql.get_column() go brrrrrrrrrrrrrrrrrrrrr
def get_column(col : str):
    if col == "age":
        return 0
    elif col == "sex":
        return 1
    elif col == "culture":
        return 2
    elif col == "luck-color":
        return 3
    elif col == "luck-reason":
        return 4
    elif col == "color-clauset":
        return 5
    elif col == "color-noble":
        return (6, 7)
    elif col == "color-highquality":
        return (8, 9)
    elif col == "color-car":
        return 10
    elif col == "association-red":
        return 11
    elif col == "room-color":
        return 12
    elif col == "room-color-chosen":
        return 13
    elif col == "room-color-reason":
        return 14
    elif col == "room-ambience":
        return 15
    elif col == "color-learning":
        return 16
    elif col == "color-relaxing":
        return 17
    elif col == "meaning-red":
        return 18
    elif col == "knows-flag":
        return 19
    elif col == "flag-meaning":
        return 20
    elif col == "check-ingredients":
        return 21
    elif col == "genre-schlager":
        return 22
    elif col == "genre-pop":
        return 23
    elif col == "genre-classic":
        return 24
    elif col == "genre-rap":
        return 25
    elif col == "genre-electro":
        return 26
    elif col == "favourite-color":
        return 27
    elif col == "fits-personality":
        return 28
    return None
