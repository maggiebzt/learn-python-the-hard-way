# A very simplified Zork and Adventure game

from sys import argv

# Variables
script, name = argv
prompt = 'Answer: '

print "Welcome to %r, %r!" % (script, name)
print "We start from west of house"
print "You're standing at the west side of the house. Do you want to go inside?"
ans = raw_input(prompt)
print "Glad you said %r" % ans