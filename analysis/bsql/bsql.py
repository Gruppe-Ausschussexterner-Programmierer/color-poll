from lib import file as csv

FILE_DATA = None #never modified, always kept to revert filters
data_selected = None
data_filtered = None


#--------------------------------------------------------------------------------------------------------------------------------
#@REGION bsql commands

def file(f_dir):
    global data_selected
    global FILE_DATA

    FILE_DATA = csv.read_csv(f_dir)
    data_selected = FILE_DATA.copy()
    print(str(len(data_selected)) + " entries selected")

    #room for potential further operations to perform on a file

#allows for more detailed filtering of selected data set
#@param cm: input tokenized command 
def filter(cm):
    global data_selected
    global data_filtered
    global FILE_DATA

    data_filtered = []

    command = cm.copy()
    command.remove(command[0]) #gets rid of unnecessary 'filter' key word

    if command[0] == "clear":
        data_selected = FILE_DATA.copy()
        print("cleared all filters")
        print(str(len(data_selected)) + " entries selected")
        return


    #splits up command into smaller filters like `a == b` and bigger logical operators
    filters = []
    for i in range(len(command)):
        if is_logical_operator(command[i]):
            filters.append(command[i])
        if is_comparison_operator(command[i]):
            filters.append([command[i - 1], command[i], command[i + 1]])

    #checks for every selected entry wether it matches a filter or not
    for row in data_selected:
        filter_applied = []
        for filter in filters:
            filter_applied.append(evaluate_filters(filter, row))
        row_matches_filters = combine_filters(filter_applied) #will only be true when all filters apply

        if row_matches_filters:
            data_filtered.append(row)
        
    #some ui 'sugar'
    if len(data_filtered) == 0:
        print("no entries found that match filters")
        data_filtered = data_selected.copy() #keeps data_selected from getting overwriten by an empty list (data_filtered)
    print(str(len(data_filtered)) + " entries selected")
    #this allows for a possible next filter command to work on an already filtered data set instead of clearing all filters
    data_selected = data_filtered.copy()


def save(nf):
    global data_filtered
    global data_selected

    
    csv.override_csv(nf, data_filtered)
    print("\nsaved selected data to " + nf)
    data_selected = None
    data_filtered = None
    print("cleared all selected data \n"
          "to perform further operations, select a data set using the `file` command")

    #TODO add `order` clause

#allows to view every entry in selected data formatted
def view(cm):
    global data_selected
    #global data_filtered

    command = cm.copy()
    command.remove(command[0])

    if command[0] == '*':
        for row in data_selected:
            print(format_row(row))

    

#--------------------------------------------------------------------------------------------------------------------------------
#@REGION working on data set

def combine_filters(filter_applied):
    #searches for 'not's in filter_applied - if it finds any, the boolean value after it will get flipped and the not removed
    for i in range(len(filter_applied)):
        if filter_applied[i] == 'not':
            filter_applied[i + 1] = not filter_applied[i + 1]
    #clears filter_aplied from nots - doing so in the first loop would require another while loop
    while 'not' in filter_applied:
        filter_applied.remove('not')

    #applies logical operators to the boolean values determined in the steps leading up to call of combine_filters()
    filters_combined: bool = filter_applied[0]
    for i in range(len(filter_applied)):
        if is_logical_operator(filter_applied[i]):
            filters_combined = eval_logical_operators(
                filters_combined, filter_applied[i], filter_applied[i + 1])

    return filters_combined

#evaluates a filter specification like `a == b` to either True or False
def evaluate_filters(filter, row):
    if type(filter) == list:
        operator = filter[1]
        name = filter[0]
        value = filter[2]
        if operator == '==':
            return double_equals(get_value(row, name), value)
        elif operator == '=':
            return single_equals(get_value(row, name), value)
        elif operator == '<':
            try:
                return smaller_than(get_value(row, name), int(value))
            except:
                print("'<' operator expects input of type <int>, <int>")
                raise Exception
        elif operator == '>':
            try:
                return larger_than(get_value(row, name), int(value))
            except:
                print("'>' operator expects input of type <int>, <int>")
                raise Exception
    else:
        return filter


def format_row(row : list):
    pass

#--------------------------------------------------------------------------------------------------------------------------------
#@REGION operator handlers
#all of these are put into their own function for cleanlyness purposes

def double_equals(a, b):
    try:
        return int(a) == int(b)
    except:
        return a == b


def single_equals(a, b):
    try:
        return int(a) == int(b)
    except ValueError:  # either a or b cannot be converted to int type
        return str(b).lower() in str(a).lower()


def smaller_than(a, b):
    if not (type(a) == int and type(b) == int): #operation only works on two integer values
        raise Exception
    return a < b


def larger_than(a, b):
    if not (type(a) == int and type(b) == int):
        raise Exception
    return a > b

#--------------------------------------------------------------------------------------------------------------------------------
#@REGION logical operators

def eval_logical_operators(a, operator, b):
    if operator == 'and':
        return a and b
    elif operator == 'or':
        return a or b

def is_logical_operator(token):
    if token == "and": return True
    if token == "or": return True
    if token == "not": return True
    return False


def is_comparison_operator(token):
    if token == '=': return True 
    if token == '==': return True
    if token == '>': return True
    if token == '<': return True
    return False

#--------------------------------------------------------------------------------------------------------------------------------
#@REGION entry-data receiving

def get_value(row, col : str):
    index = get_column(col)
    if type(index) == tuple:
        val1 = row[index[0]]
        val2 = row[index[1]]
        value = str(val1) + str(val2)
    else:
        value = row[index].lower()

    try:
        return int(value)
    except ValueError:
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
