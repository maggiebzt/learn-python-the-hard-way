# Defined a function called cheese_and_crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"
	
# Run function by passing numbers
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

# Run function by passing variables
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Run function by passing mathematical calculation
print "We can even do math inside too:"
cheese_and_crackers(10 + 2-, 5 + 6)

# Run function by passing the combination of variables 
# and mathematical calculation
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
