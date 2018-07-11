my_name = "Margaret K. Baramuli"
my_age = 123
my_height = 123.456 #cm
my_weight = 123.12345 #lbs
my_eyes = "Brown"
my_teeth = "White"
my_hair = "Black"
my_race = "Asian"

print "Let's talk about %s." % my_name
print "She's %d centimeres tall." % my_height
print "She's %i pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

print "I'm %d and %s" % (my_age, my_race)

print "What's this for %i?" % my_weight

print "------------------"
print "Study Drill"

# 1.
name = "Margaret K. Baramuli"
age = 123.8
height = 123.99 #cm
weight = 123 #lbs
eyes = "Brown"
teeth = "White"
hair = "Black"
race = "Asian"

# '%s' = string, good for user view
print "Let's talk about %s." % name

# '%d' = decimal, doesn't display decimal and rounds down
print "She's %d years old." % age

# '%i' = integer, doesn't display decimal and rounds down
print "She's %i centimeres tall." % height

# '%e' = floating point, displays 6 decimal places and
# uses scientific notation E or e
print "She's %e pounds heavy." % weight # 1.230000e+02 = 123

# '%r' = raw string, good for debugging but not good for user view
print "She's got %s eyes and %r hair." % (eyes, hair)
print "Her teeth are usually %s depending on the coffee." % teeth

gender = "f"
# '%c' = single character string
print "Her gender is %c" % gender

# 4.
print "----------"
print "Conversion"
print "She's %e inches tall." % (height * 0.393701)
print "She's %e kgs heavy." % (weight * 0.453592)
