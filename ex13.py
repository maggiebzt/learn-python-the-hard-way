from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

# -----------------------------------------------------------------------------
# Study Drills
# 1. ValueError: need more than 1/2/3 values to unpack
# There are 4 arguments, the first argument is always the script name.
# We must provide exactly n-1 values when running the code to avoid this error.
# If we provide more than n-1, ValueError: too many values to unpack

# 4. Modules give you features!

