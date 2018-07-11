from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename)

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line1: ")
line2 = raw_input("line2: ")
line3 = raw_input("line3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')

print "And finally, we close it."
target.close()

#--------------------
# Study Drills

# 4. Passing a 'w' makes allows python to truncate the file if it existed and write on a
#    new file. Without explicitly saying 'w', the default value is 'r' which is read.
#    In this mode, we won't be able to truncate/write on the file. Try it yourself!

# 5. No. Passing the 'w' makes python truncate the file if it already exists.