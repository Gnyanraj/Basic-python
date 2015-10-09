__author__ = 'rudragouda'

# operations will be on this string
astring = "Hi there, This is a program on basic string operations!"

# prints the length of the string
print "The string length is: %d" % len(astring)

# prints the index value of a character
print "The index value of the character 'o' is: %d" % astring.index("o")

print "The character 'o' is repeated %d times in the string " % astring.count("o")
print astring[14:29]

print "------------------------"
print "------------------------"
print "....Exercise work here...."
# prints string in upper case and lower case
print astring.upper()
print astring.lower()
print "------------------------"
# prints true or false accordingly
print astring.startswith("Hi")
print astring.endswith("asdfasdfasdf")
print "------------------------"
split = astring.split("o")
print split


