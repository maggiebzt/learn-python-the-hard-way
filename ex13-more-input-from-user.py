# 3. Combine raw_input with argv to get more input from user

from sys import argv

# Variables
script, time_of_day = argv

print "This is ma script:", script
# Print out greetings according to the argument provided by user
print "Good", time_of_day

# Prompt user to provide input
condition = raw_input("How are you today? ")
print "That's fantastic! Glad to hear that you're", condition

# Calculate user's year of birth from user's age
age = int(raw_input("How old are you? "))
print "You were born on", (2018 - age)
print "You are %s years old" % age