# ex15: Reading Files

# The file requires 1 additional argument when ran in terminal
# To run in terminal:
#	- download this file (ex15c.py) and ex15_sample.txt file
#	- call '$ python ex15c.py ex15_sample.txt'

from sys import argv

# Argv variables
script, filename = argv

# Open file
txt = open(filename)

# Print file's current position
print "Tell starting position: %s \n" % txt.tell() # 0

# -- next() --
# Print first line using next method and strip the 'new-line' character
print "file.next():"
print txt.next().strip('\n')
# Print file's current position after calling next method
print "Tell position after next(): %s \n" % txt.tell() # 97

# -- seek() --
# Set file's current position to 0
txt.seek(0)

# -- readline() --
# Print first line using readline method
print "file.readline():"
print txt.readline().strip('\n')
# Print file's current position after calling readline method
print "Tell position after readline(): %s \n" % txt.tell() # 35

# -- read() --
# Read the rest of the file:
print "file.read():"
print "NOTE: Since current position is 35, read() print out the rest of the file"
print txt.read(), '\n'

# Reset current position in the file
txt.seek(0)
print "NOTE: Current position is reset to 0, read() print out the whole file"
print txt.read(), '\n'
print "Tell current position:", txt.tell()

# Close the file
txt.close()