__author__ = 'rudragouda'
primes = [1, 2, 3, 4, 5]
for prime in primes:
    print prime
print "------------------------"
# Prints out the numbers 0,1,2,3,4
for x in xrange(5):
    print x
print "------------------------"
# Prints out 3,4,5
for x in xrange(3, 6):
    print x
print "------------------------"
# Prints out 3,5,7
for x in xrange(3, 8, 2):
    print x
print "------------------------"
# while statement
# Prints out 0,1,2,3,4
count = 0
while count < 5:
    print count
    count += 1
print "------------------------"
# break and continue statements
# Prints out 0,1,2,3,4
count = 0
while True:
    print count
    count += 1
    if count >= 5:
        break
print "------------------------"
# Prints out only odd numbers - 1,3,5,7,9
for x in xrange(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print x
print "....Exercise work here...."
a = input(raw_input("How many numbers you want to enter: "))
print "start entering the numbers one by one..."