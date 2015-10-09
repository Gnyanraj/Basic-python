__author__ = 'rudragouda'

# prints true or false accordingly
x = 2
print x == 2
print x == 3
print x < 3
print "-----print name and age-----"
name = "rudra"
age = 26
if name == "rudra" and age == 26:
    print "Your name is %s, and you are also %d years old." % (name, age)
print "---------or keyword---------"
if name == "rudra" or name == "ardur":
    print "Your name is either rudra or ardur."

print "---------in keyword---------"
if name in ["rudra", "ardur"]:
    print "Your name is either rudra or ardur."
print "------------------------"
# if and else if statements
x = 2
if x == 2:
    print "x equals two!"
else:
    print "x does not equal to two."
# the is operator
x = [1, 2, 3]
y = [1, 2, 3]
print x == y
print x is y
print "------------------------"
# the not operator

print "....Exercise work here...."
x = 0
if x > 0:
    print "x is positive!"

elif x < 0:
    print "x is negative"

else:
    print "x is zero"
print "------------------------"
