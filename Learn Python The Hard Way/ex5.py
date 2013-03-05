name = 'Richard Littauer'
age = 24 #Not a lie
height = 12*6 #inches
weight = 180 #lbs
eyes = 'grey-green-blue'
teeth = 'slightly yellow'
hair = 'Brown'

print "Let's talk about %r." % name
print "He's %r inches tall." % height
print "He's %r pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %r eyes and %r hair." % (eyes, hair)
print "His teeth are usually %r depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %r, %r, and %r I get %r." % (age, height, weight,
        age + height + weight)
