my_name = 'Jan'
my_age = 76 # a lie
my_height = 175 # cm
my_weight = 180 # kg
my_eyes = 'Black'
my_teeth = 'red'
my_hair = 'black'

print "Let's talk about %s." % my_name
print "He's %d cm tall." % my_height
print "He's %d kg heavy." % my_weight
print "Actually that's a little heavy."
print "He's got %s eys and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the smoke." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)
