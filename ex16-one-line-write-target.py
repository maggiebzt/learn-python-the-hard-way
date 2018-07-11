from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line1: ")
line2 = raw_input("line2: ")
line3 = raw_input("line3: ")

print "I'm going to write these to the file."

# TO-DO: Use strings, formats, and escapes to print out line1, line2, and 
# line3 with just one target.write() command instead of six.
str = line1 + '\n' + line2 + '\n' + line3 + '\n'
target.write(str)

print "And finally, we close it."
target.close()