# number of cars
cars = 100

# number of space in a car
space_in_a_car = 4.0

# number of drivers
drivers = 30

# number of passengers
passengers = 90

# number of cars not driven
cars_not_driven = cars - drivers

# number of cars driven
cars_driven = drivers

# number of carpool capacity
carpool_capacity = cars_driven * space_in_a_car

# number of average passengers per car
average_passengers_per_car = passengers / cars_driven

# print out numbers and explanations
print "There are", cars, "cars available"
print "There are only", drivers, "drivers available"
print "There will be", cars_not_driven, "empty cars today"
print "We can transport", carpool_capacity, "people today"
print "We have", passengers, "to carpool today"
print "We need to put about", average_passengers_per_car, "in each car"

print "------------------"
print "Study Drill"

# 1. It's not necessary -- we're counting number of people, therefore expecting
# round numbers. 

# 2. More accurate, no round downs, has decimal points. 
# Floats may also be in scientific notation, with E or e indicating the 
# power of 10 (2.5e2 = 2.5 x 102 = 250).

# 4. '=' (equals) assigns a value to a variable

# 5. '_' (underscore)

# 6. Python calculator using variables
i = 123
x = 456
j = 789

print "If i + x =", i + x
print "and i + j =", i + j
print "and x + j =", x + j

print "What is the value of i, x, and j?"