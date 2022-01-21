call-it-official documentation of "Bullshit Query Language" (short: BSQL)

# part of the project "color-poll" developed by GAP
# tool to specifically analyze the results of that poll
# author: Emil Schläger
# name is definitely not a knock-off of SQL
-----
english:

In here, you will find a documentation of how to use the console dialogue. There will also be a graphical user interface, however that will take longer and should be self-explanatory.

Before going into greater detail on the syntax, it might be of value to get a quick overview on the entire process. In bsql, quiries always
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
you won't know all of them, there is a list of every attribute name at the END OF THIS FILE. (There will also be an image or a pdf file relating
all of them to their respective question of the original poll sheet).

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


But that's not it for all the filtering tools that are at your disposal. You can also chain individual filters together, for example:

    > file overall.csv
    5 entries selected
    > filter age = 10 and sex = weiblich
    2 entries selected

Notice the `and` key word in this quiry. This is called a 'logical operator', and you might have run across these in math or NWT classes.
In BSQL, there are three of them:
            and
            or
            not

Whilst probably quite self-explanatory, I'll shortly go over each of them:

    1. and
    `and` is really straight forward - To evaluate to True (or "meeting your filter requirements"), the filter on each side of the operator
    has to apply to a form.

    2. or


----
(Bei Betrachten der Nutzer scheint mir eine deutsche Version angebracht) deutsch:

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

        !! DOES NOT SUPPORT <= OR >= OPERATORS !!
> filter clear

> view 

> save `new_file`