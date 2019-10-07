# The Four lines of readable below are defining what x, y, binary, and doNot mean and what they will display when they are printed.
x = "there are %d types of people." % 10
binary = "binary"
doNot = "don't"
# The line below uses %s to determine what will be printed when it is. The first %s will display text associated with binary, while the second %s will display text associated with doNot.
y = "Those  who %s and those who %s" % (binary, doNot)

# The two lines below will print the text associated with x and y
print(x)
print(y)

# The two lines below add text before both x and y
print("I said: %r" % x)
print("I also said: '%s'." % y)


hilarious = False
joke_evaluation = "Isn't that joke so funny!? %r"
print(joke_evaluation % hilarious)

w = "This is the left side of..."
e = "A string with a right side."

print(w + e)

