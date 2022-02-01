#TODO: FOR BSQLGUI, HAVE EVERY FUNCTION RETURN SOMETHING INSTEAD OF PRINTING IT
# ==> HAVING VALUES RETURNED ALLOWS FOR EASY ANALYSIS

from lib import file as csv
import operator

FILE_DATA = None #never modified, always kept to revert filters
data_selected = None
data_filtered = None

entries = ["age", "sex", "culture", "luck-color", "luck-reason", "color-clauset", "color-noble", "color-noble", "color-highquality",
           "color-highquality","color-car", "association-red", "room-color", "room-color-chosen", "room-color-reason", 
           "room-ambience", "color-learning","color-relaxing", "meaning-red", "knows-flag", "flag-meaning", "check-ingredients", 
           "genre-schlager", "genre-pop", "genre-classic", "genre-rap", "genre-electro", "favourite-color", "fits-personality"]

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

    try:
        view_nones = command[1] + " " + command [2] == "--view all" #comparing deals with command[1] and [2] being sth else
    except IndexError:
        view_nones = False

    values: dict = {}
    if command[0] == '*':
        num = 1 #ui sugar
        for row in data_selected:
            print(str(num) + ".: {", end='')
            print(format_row(row, view_nones))
            print("}")
            print(20 * "-")
            num += 1

    #this code has to be here for this if statement is also true when the following is -> better comments will be found there
    elif command[0][:2] == "--":
        color = command[0][2:].lower()  # removes '--' from string
        for row in data_selected:
            for entry in enumerate(row):
                split_values = entry[1].replace(';', ',').split(',')  # deals with commas
                for value in split_values:
                    if value.replace(' ', '') == color: #replace function deals with spaces on edge of value
                        try:
                            values[get_column_name(entry[0])] += 1
                        except KeyError:
                            values[get_column_name(entry[0])] = 1

    elif command[0][0] == '-':
        attribute = command[0][1:] #cuts off first character
        index = get_column(attribute)

        for row in data_selected:
            if type(index) == tuple: #due to stupid design, some attributes have multiple values, thus returning tuples
                val1 = row[index[0]]
                val2 = row[index[1]]
                value = str(val1) + "," + str(val2) #just joining the attributes together to treat them as any other attribute
            else:
                value = str(row[index]).lower()
            #splitting value in case it is a list seperated with commas
            split_values = value.replace(';', ',').split(',') #replace() handles semicolons as delimeter as well
            for val in split_values:
                if len(val) >= 1: #prevents empty attributes from crashing application
                    val = val.replace(' ', '')
                else:
                    val = "no answer"
                
                try:
                    values[val] += 1
                except KeyError: #creates entry if not yet existant
                    values[val] = 1
    
    #returns values in `values` sorted from highest to lowest as a list of tuples
    values_sorted = sorted(values.items(), key=operator.itemgetter(1), reverse=True)
    if len(values_sorted) == 0:
        print("no entries match the parameter")
    for value_pair in values_sorted:
        print("\t{0[0]}: {0[1]}".format(value_pair))
            
    
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
            filters_combined = eval_logical_operators(filters_combined, filter_applied[i], filter_applied[i + 1])

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
        elif operator == "is" and value == "null":
            return is_null(get_value(row, name))
    else:
        return filter


def format_row(row : list, view_all : bool):
    out = "\t"
    entry_index = 0
    for entry in row:
        if view_all or entry != '':
            out += "{0}: {1}\n\t".format(get_column_name(entry_index), entry)
        entry_index += 1
    
    out = out[:-2]
    return out

#--------------------------------------------------------------------------------------------------------------------------------
#@REGION operator handlers
#all of these are put into their own function for cleanlyness purposes

def double_equals(a, b):
    try:
        return str(a).lower() == str(b).lower()
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

def is_null(a):
    return a == '' or a == None
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
    if token == 'is': return True
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

def get_column_name(index):
    try:
        return entries[index]
    except:
        return None

def get_column(col : str):
    if col == "color-noble":
        return (6, 7)
    elif col == "color-highquality":
        return (8, 9)
    else:
        try:
            return entries.index(col)
        except :
            return None
