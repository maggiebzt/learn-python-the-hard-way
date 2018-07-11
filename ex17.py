from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line too, how?
in_file = open(from_file)
indata = in_file.read()

# this is how you do it in one line
# indata = open(from_file).read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alrght, all done"

out_file.close()
in_file.close()

#-------------------------
# Study Drill

# 6. Good explanation here: https://stackoverflow.com/questions/25070854/why-should-i-close-files-in-python