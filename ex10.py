tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

#while True:
#	for i in ["/", "-", "|", "\\", "|"]:
#		print "%s\r" % i,

#-------------------------
# Study Drill

# 2. The only reason you might need """ instead of ''' (or vice versa) 
# is if the string itself contains a triple quote.
# s1 = '''This string contains """ so use triple-single-quotes.'''
# s2 = """This string contains ''' so use triple-double-quotes."""
# If a string contains both triple-single-quotes and triple-double-quotes 
# then you will have to escape one of them, but this is an extremely rare situation.
print '''This uses
triple single quote
'''

# 3. 
print """\"She said, \"My favorite quote is:
\'You is smart, you is kind, you is important\'.\" 
But she cannot remember what movie it's from.\""""

# 4.
print "The first day of the \'%s\' is %r." % ('week', 'Mon')