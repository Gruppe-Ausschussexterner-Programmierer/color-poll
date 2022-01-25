call-it-official documentation of "Bullshit Query Language" (short: BSQL)

# part of the project "color-poll" developed by GAP
# tool to specifically analyze the results of that poll
# author: Emil Schläger
# name is definitely not a knock-off of SQL
# please excuse the awkward line wrapping, but text files are a little impractical in that regard

-----
english:

To start the console dialogue, navigate into the `analysis` folder and execute `analysis.exe`. It basically is the same procedure as last time.

------------------------------------------------------------------------------

In here, you will find a documentation of how to use the console dialogue.
AT THE VERY END OF THIS FILE, THERE WILL BE A QUICK OVERVIEW ON ALL COMMANDS AND ALL FORM ATTRIBUTE NAMES AS WELL AS THEIR CORRESPONDING QUESTIONS.

Before going into greater detail on the syntax, it might be of value to get a quick overview on the entire process. In BSQL, queries always
follow the same structure:
            1. reading the content of a file
            2. filtering the selected content
            3. saving the filtered data for later use

There of course are a couple more functions which differ from this structure slightly, but this is generally how you will analyze data with this tool.
So without further ado, let's get into how you actually do this:

------------------------------------------------------------------------------

1. OPENING A FILE

Before working on a data set, you have to select it. To do so, use the `file` key word and specify the file you want to 
work on immediately after. Here, `overall.csv` is used as an example:

    > file overall.csv

After processing the command, the program will tell you how many forms the file you selected stores. This will look something like this:

    > file overall.csv
    5 entries selected

Now it might very well be, that you don't know the names of the files existing. In that case, don't worry, just type 

    > file *

This will return you a list of every existing file's name and should look something like this:

    > file *
    age10.csv
    age11.csv
    ...

Note that using `file *` won't actualy open any file, you still have to do that manually afterwards.

------------------------------------------------------------------------------

2. FILTERING DATA

Oh boy... this was definitely the most work to implement, and is also probably the most difficult to get your head around, syntactically speaking.
Easy things first: You always initiate a filtering operation with the key word `filter`, after which you can apply conditions, by which your data is 
filtered. Here's an example to start:

    > file overall.csv (don't forget to select a file first :)
    5 entries selected
    > filter age = 10
    3 entries selected (notice that again, you will get feedback on how many entries fit your conditions)

In this example, we filterd the data by the attribute `age`, more specifically we selected every entry, where the `age` attibute is equal to 10. So far,
so good. But it gets more complicated: First of all, `age` is only one of 27 attributes a form has. Since each one has its own name and chances are, 
you won't know all of them, there is a list of every attribute name at the END OF THIS FILE linking them to their corresponding questions on the 
analog poll sheet.

Futhermore, there's more comparison operators than `=`. All of the following, to be exact:
            =
            ==
            > (only works when comparing number attributes, like `age`)
            < (only works when comparing number attributes, like `age`)

------
Lets start with the most straight forward ones, `<` and `>`:
They represent `smaller than` and `larger than`, and only work on attributes containging numbers. Frankly, there are only to of them:
            `age`
            `check-ingredients`
Notice, that if you try to use those operators on a non-integer attribute, you will receive the following error message:
    
    > filter culture > 4
    '>' operator expects input of type <int>, <int>

Since it expects integers, notice that passing it a decimal point number will result in the same exception:

    > filter check-ingredients < 5.5
    '<' operator expects input of type <int>, <int>

-----
Now on to `=` and `==`:
To none-JavaScript-programmers, the difference of these two might seem confusing, but it's (in this case) actually pretty trivial:
            `=` compares two values to being SIMILAR to each other
            `==` compares two values to being EXACTLY EQUAL to each other

To maybe give this more sense, let me clarify that I primarily implemented `=` for occasions where there are 2 seperate answers given to a 
single question in a form. Let me demonstrate this with an example:

    Let's say, there is a form where the attribute `culture` has been entered as "deutsch, französich" Clearly two different cultural aspects - 
    So when you filter for culture, you want to have both of them valued individually. Say you do the following:

        > filter culture = deutsch

    In this case, our above form will be seen as fitting the filter, since "deutsch, französich" is similar to "deutsch" (similar, in this case,
    means that "deutsch" appears fully in "deutsch, französich").
    
    Contrary, if you did the following...: 

        > filter culture == deutsch

    ...the above form will not be seen as fitting the filter, since "deutsch, französich" is not EXACTLY equal to "deutsch".

Now, you might wonder, is there any use case for `==` then? I'd argue, there is. Taking our above example agein: Maybe you want to filter for 
people, who only identify as french. In this case, using `==` will eliminate all people identifying as something else as well from the filter.

Note that when comparing numbers, both of these work exactly the same.

Now you might wonder, how you check for attributes being empty. Turns out, that's not actually possible with the operators above. However, there is 
a neat little command you can use for that:

    > filter culture is null
    1 entries selected          (yes, you'll always get the plural of `entry`)

The `is null` key word will filter the data set for forms in which your specified attribute is empty. Apart from needing its second parameter specified 
as "null" (otherwise it won't find any entries), it acts just like any other comparison operator.

-----
But that's not it for all the filtering tools that are at your disposal. You can also chain individual filters together, for example:

    > file overall.csv
    5 entries selected
    > filter age = 10 and sex = weiblich
    2 entries selected

Notice the `and` key word in this query. This is called a 'logical operator', and you might have run across these in math or NWT classes.
In BSQL, there are three of them:
            and
            or
            not

Whilst probably quite self-explanatory, I'll shortly go over each of them:

    1. and
    `and` is really straight forward - To evaluate to True (or "meeting your filter requirements"), the filter on each side of the operator
    has to apply to a form.

        e.g: 
        > filter age = 11 and sex == männlich

    2. or
    `or` evaluates to true, when AT LEAST one of the expressions around it is True. The mathematical `or` is inclusive, which means it
    differs from the common use of 'or' (exlusive, or colloquial "either or") in that it also evaluates to True when both conditions are True - In
    other words, if you use a filter expression containing `or`, in order to NOT be regarded as matching the filter requirements, a form would have 
    to fulfill NONE of the requirements.

        e.g:
        > filter age = 11 or sex == männlich

    3. not
    `not` simply negates the expression following it. Please note, that note has to be in front of the entire expression ("not a = b"), not the 
    comparison operator (wrong: "a not = b")

        e.g:
        > filter not age = 11 and not sex == männlich


Note that it is absolutely possible to stack filters over multiple lines. In other words, you can apply a filter to a data set, and your next filter
will apply to the already filtered data set:

    > filter age = 10 (filters original data set)
    3 entries selected
    > filter sex = weiblich (filters within the 3 entries selected through prior filter)
    2 entries selected

If you want to clear your filters without saving the filtered data to a new file (if you made a mistake for example), simply use the 

    > filter clear
    cleared all filters
    5 entries selected

command. Note that this will clear all filters (not just the last one) and you will be presented to work with the data set you originally read 
out of the file you specified.


**
To have that noted somewhere: Filtering data won't delete any forms from files, you don't have to worry about losing data when filtering.

------------------------------------------------------------------------------

3. SAVING DATA

When you applied all filters, you might want to save that data set - either for later use, or to open your newly created file to only work on a 
much smaller data set entirely. Do so via the `save` command:

    > file overall.csv
    5 entries selected
    > filter age = 10 and sex == weiblich
    2 entries selected
    > save new_file.csv 
    saved selected data to {path to your results folder}\new_file.csv 
    cleared all selected data
    to perform further operations, select a data set using the `file` command

It hereby is of absolute importance that your file name conforms to the following requirements:
            1. spaces are not supported - use underscores instead
            2. the name MUST end in ".csv" - the entire program is built on this file format

Note the feedback you get: First you will be shown the path to your file. This mostly serves means of confirmation, but in case you wondered, where
your files are stored, there you go. Second it tells you that it cleared all selected data - This means, as the next line correctly informs you,
that you first have to select a new file in order to keep analyzing. And apart from that, there's not a lot more to the `save` command - Just 
know that in case the file you're writing to, already exists, its former data will be overriden. An algorithm to block this is only in place for
the `overall.csv` file, everything else it will just override.

------------------------------------------------------------------------------

4. VIEWING DATA 

Now that you know how to read, filter and save forms, it's very reasonable that you also want to view the content of forms. To do so, use the 
`view` command. This will format your requests to make it prettier to look at, as well as offer you a very basic analysis tool. Let's assume
you first executed the following commands:

    > file overall.csv
    5 entries selected
    > filter age = 10 and sex == weiblich
    2 entries selected

Now you want to view how those two entries look. There's three ways you can personalize the `view` command: 

    > view *

This will format you the attributes for every selected form following the structure: `attibute name`: `attribute value` - 
However, it will only show you the attributes that have a corresponding value. An example could look like this:

    > view *
    1.: {   age: 10
            sex: weiblich
            favourite-color: rot
            fits-personality: teilweise
}

Note that it only outputs 4 values - This means, that all other 24 attributes of the form are empty, on other words, the person who took part in 
the poll did not answer the question. 

Now in the probably not very likely case, that you would like to view EVERY attribute of every file, even those empty attributes, simply add 
`--view all` to the end of the command:

    > view * --view all

I won't put the output in here, for it would be a bunch of uneccesary lines, but those should be looking something like this:

    culture: 
    luck-color:
    (...)

Now having to view every attribute of every file and manually keeping score of how often an attribute has a specific value would be an incredible 
waste of time and is not why this entire project exists in the first place. Let me present to you:

    > view -`attribute name` (the '-' in here is important!)

This will go through every selected form and only keep track of the value it has stored as your specfied attribute. It will then count them together
and output, in descending order, how often which value exists in the selected data set. (Since I've been working on this documentation for quite a 
while now and I feel like my explanations only get worse, ) Here's an example:

    > file overall.csv
    5 entries selected
    > view -favourite-color
        rot: 2
        blau: 1
        no answer: 1
        lilablassblaukariert: 1

As you can see, we told the program to look through a data set (containing 5 forms) and keep track of the `favourite-color` attribute. The 
output is to be interpreted as the following: 
    2 people have 'rot' as their favourite color
    1 person each has 'blau' and 'lilablassblaukariert' as their favourite color
    1 person did not answer the question

And that's it - A console dialogue, which can essentially barely do anything, explained in a little over 260 lines. I tried my best to explain
everything as simple and easy to understand as I could, however, if there still are questions, I'm happy to help you. On the other hand, you
practically can't destroy anything - so when in doubt, just try it out. Maybe I'll even have time to give you a graphical interface at some point.

---
In terms of visualizing your data, there isn't anything in BSQL currently, and I highly doubt there ever will be. And that is that way because of a very simple reason: There's no need for me to program something to do this, when there's a million free tools for you online that offer way more flexibility than I ever could. Let me give you a site i found in a 10 second google search that lets you create all kinds of charts and export them:

https://meta-chart.com

You should be able to find sites like this in no time. And whilst I agree that pasting every data into an online tool might 
seem like a little bit of a grind, just think about the fact that creating a visualization tool myself would have probably taken 
me at least a week - show the developers some love (:

-------------------------------------
list of commands:
> file `filename`
> file *

> filter not `filter` and `filter` or `filter` ...
    (`filter`:
        a = b
        a == b
        a > b
        a < b )

        !! DOES NOT SUPPORT <= OR >= OPERATORS !!
> filter `attribute` is null
> filter clear

> view *
> view * --view all
> view -`attribute`

> save `new_file`

---
list of attributes:
[Formattiert als `Name` (`Datentyp` *) -> korrespondierende Frage auf Umfrageboten]
[* int = Integer (Ganzzahl); boolean (entweder `True`, `False` (oder leer)); any (freier text)]

age                 (int)                                       -> Alter
sex                 (any {"männlich" / "weiblich" / "andere"})  -> Geschlecht
culture             (any)                                       -> Welcher Kultur fühlst du dich zugehörig?
luck-color          (any)                                       -> Welche Farbe signalisiert für dich Glück?
luck-reason         (any)                                       -> Erkläre kurz, warum du diese Farbe [als "Glücksfarbe"] notiert hast.
color-clauset       (any)                                       -> Welche Farbe hängt am häufigsten im Kleiderschrank?
color-noble         (any)                                       -> Welche Farben wirken auf dich edel?
color-highquality   (any)                                       -> Welche Farben würdest du als besonders hochwertig wahrnehmen?
color-car           (any)                                       -> Welche Farbe hätte dein Traumauto?
association-red     (any)                                       -> Was verbindest du mit der Farbe Rot?
room-color          (any)                                       -> Welche Wandfarbe hat dein Zimmer?
room-color-chosen   (boolean) (True = Ja / False = Nein)        -> Hast du diese Farbe bewusst gewählt?
room-color-reason   (any)                                       -> [Grunndangabe im Falle einer Beantwortung der vorherigen Frage mit "Ja"]
room-ambience       (any)                                       -> Wie beschreibst du die Atmosphäre in deinem Zimmer?
color-learning      (any)                                       -> Bei welcher Wandfarbe kannst du am besten lernen?
color-relaxing      (any)                                       -> Bei welcher Wandfarbe kannst du am besten entspannen?
meaning-red         (any {"liebe" / "krieg"})                   -> Welches Wort trifft am ehesten auf die Farbe Rot zu?
knows-flag          (boolean) (True = Ja / False = Nein)        -> Weißt du, wofür diese Flagge steht? 
flag-meaning        (any)                                       -> [Antwort im Falle einer Beantwortung der vorherigen Frage mit "Ja"]
check-ingredients   (int {1 bis 10}                             -> Wie oft schaust du auf Inhalts-/Schadstoffe auf Süßigkeitenpackungen?
genre-schlager      (any)                                       -> Farbe des Musikstils Schlager
genre-pop           (any)                                       -> Farbe des Musikstils Pop
genre-classic       (any)                                       -> Farbe des Musikstils Klassik
genre-rap           (any)                                       -> Farbe des Musikstils Rap
genre-electro       (any)                                       -> Farbe des Musikstils Elektro
favourite-color     (any)                                       -> Lieblingsfarbe
fits-personality    {"True" / "False" / "teilweise"}            -> Stimmt deine Lieblingsfarbe mit deiner Persönlichkeit überein?