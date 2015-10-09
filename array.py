__author__ = 'rudragouda'

arr = []
a = int(raw_input("How many numbers you want to enter: "))
print "Array size is ... %d" % a
print "Enter the input"
for i in range(a):
    x = int(raw_input(":"))
    arr.append(x)

print "the original array is..."
print arr

arr.sort()
print "the sorted array is..."
print arr

arr.reverse()
print "the reverse of the sorted array is..."
print arr
