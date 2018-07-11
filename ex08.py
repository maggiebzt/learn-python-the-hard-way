formatter = "%r %r %r %r"

# Print out: 1 2 3 4
print formatter % (1, 2, 3, 4)

# Print out: 'one' 'two' 3 4
print formatter % ("one", "two", 3, 4)

# Print out: '%r %r %r %r' '%r %r %r %r' 3 4
print formatter % (formatter, formatter, 3, 4)

# Print out: 'a' 'b' 'c' 'd'
print formatter % (
	"a",
	"b",
	"c",
	"d"
)

# Print out: 'I had this thing.' 'That you could type up right.' 
# "But it didn't sing." 'So I said goodnight.'
print formatter % (
	"I had this thing.",
	"That you could type up right.", 
	"But it didn't sing.",
	"So I said goodnight."
)

#-------------------------
# Study Drill

# 2. Because there is the single-quote character in the word 
# "didn't" in line 25.