# Variables
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s" % (binary, do_not) # Two strings

# Print out strings
print "I said %r" % x # One string
print "I also said: '%s'." % y # One string

# More variables
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# Print out joke_evaluation and replaced '%r' with hilarious
print joke_evaluation % hilarious

# More variables
w = "This is the left side of ..."
e = "a string with a right side"

# Print out the variable 'w' concatenated with variable 'e' 
# Can only use '+' to concatenate variables of the same type
print w + e

print "------------------"
print "Study Drill"

# 3. There's 3 places. But line 5 puts 2 strings in a string.
#    'hilarious' is not a string, it's a boolean variable.

# 4. '+' concatenates the two strings into one.