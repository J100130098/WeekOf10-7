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