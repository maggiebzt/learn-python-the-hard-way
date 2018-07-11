days = "M T W Th F S Su"

# \n = new line
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print "Here are the days: ", days

# This would replace \n with new line
print "Here are the months: ", months

print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""

# This would literally print out the value of months
# instead of replacing \n with new line
print "months with r: %r" % months