# The Four lines of readable below are defining what x, y, binary, and doNot mean and what they will display when they are printed.
x = "there are %d types of people." % 10
binary = "binary"
doNot = "don't"
# The line below uses %s to determine what will be printed when it is. The first %s will display text associated with binary, while the second %s will display text associated with doNot.
y = "Those  who %s and those who %s" % (binary, doNot)

# The two lines below will print the text associated with x and y.
print(x)
print(y)

# The two lines below add text before both x and y.
print("I said: %r" % x)
print("I also said: '%s'." % y)

# The line below is defining the term hilarious, which is false.
hilarious = False
# the line below is defining what the term joke_evaluation will print when it is printed.
joke_evaluation = "Isn't that joke so funny!? %r"
# the line below prints the defined terms from above, stating that the joke was not funny.
print(joke_evaluation % hilarious)

# the two lines below define what w and e will be printed as when given the command print.
w = "This is the left side of..."
e = "A string with a right side."

# the line below is printing the text associated with w and e together, making one complete sentence.
print(w + e)

# 10-8 more stuff

# the 4 lines below print the text in parentheses when run
print("Mary had a little lamb.")
print("it's fleece was white as %s." % 'snow')
print("And everywhere that Mary went.")
print("." * 10)
# the line above is multiplying the text 10 times to make ".........."

# the 12 lines below give the "ends" a meaning
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# the line below prints the "ends" all together, spelling out CheeseBurger
print(end1 + end2 + end3 + end4 + end5 + end6 + end7 + end8 + end9 + end10 + end11 + end12)

# More Formatting
# the 5 lines below first give the term "formatter" a value, then print the whatever values you want to be associated with formatter.
formatter = "%r %r %r %r"
print(formatter % (1, 2, 3, 4))
print(formatter % ("one", "two", "three", "four"))
print(formatter % (True, False, False, True))
print(formatter % (formatter, formatter, formatter, formatter))

# why use %r instead of %s?
# while %r and %s appear to be identical, %r allows you to change the value that it is associated with immediately after it is given a definition, while %s will not change what it represents.

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug\nSep\nOct\nNov\nDec"

print("Here are the days: ", days)
print("Here are the months: ", months)

print("""
There's something going on here.
with the three double quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""")

# what if I didn't like Jan being listed on the line with the rest of the
# text and away from the other months? How can I fix that?

# more escaping

tabbyCat = "\tI'm tabbed in."
persianCat = "I'm split\non a line."
backslashCat = "I'm \\ a \\ Cat"
taskCat = """
I'll make a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
print(tabbyCat)
print(persianCat)
print(backslashCat)
print(taskCat)

# escape Seq                What does it do
# \\
# \\ adds a single \ to a line of printed code
print("I \\ am \\ a slash")
# \*
# \* adds a * to where ever it is printed
print("\* this does this")
# \"
# \" adds " to where it is typed when printed
print("\"This does something incredible\"")
# \a
# \a adds a Bullet to where it is typed in a print line
print("\a is pretty cool")
# \b
# \b creates a backspace whenever it is printed
print("\b is not\bas cool as \a")
# \f
# \f seems to do the same thing as \a
print("I never\f want to use \f")
# \n
# \n forces all that is printed to be printed on the next line
print("never gonna \n give you up!")
# \N{name}
# \N{name} allows you to print unicode characters from python's unicode database.
print (u"\N{SOLIDUS} \N{BLACK SPADE SUIT}")
# \r
# \r creates a carriage return in your print.
print("Apples\rOranges")
# \t
# \t creates a tab in your print
print("\t Why does \t exist? ")
# \uxxxx
# \uxxxx
print(" u'\\🐍\\u032f\\u0361\\u0e4f' will do this cool thing")
# \Uxxxxxxx
# \v
# \ooo
# \xhh

# what's the following Code do?
#   while True:
#       for i in ["\","-","|","\\","|"]:
#           print("%s\r" % i, end='')

# Can you replace """ with '''?

age = input("How old are you? ")
height = input("How tall are you? ")

print("You are %r tall and %r old" % (height, age))
