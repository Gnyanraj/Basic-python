__author__ = 'rudragouda'
numbers = []
numbers.append(1)
numbers.append(2)
numbers.append(3)
strings = ['werty', 'asdf', 'fytgf']
names = ["John", "Eric", "Jessica"]
print(numbers)
print strings
print "The second name in the names list is %s" % names[1]
mylist = ['start_list', 1, 2, 3]
mylist.append(4)
mylist.append(5)
mylist.append(6)
mylist.append('end_list')
print(mylist[0])
print(mylist[1])
print(mylist[2])
print(mylist[3])
print"Loop.."
# prints out 1,2,3
for x in mylist:
    print x
print "------------------------"
print "....Exercise work here...."
numlist = []
numlist.append(1)
numlist.append(2)
numlist.append(3)
print "List has following numbers"
for x in numlist:
    print x
numlist[2] = 5
print "updated numlist"
for x in numlist:
    print x
namelist = []
namelist.append('abc')
namelist.append('pqr')
namelist.append('xyz')
print "List has following names"
for x in namelist:
    print x
namelist[0] = 'abcdef'
print "updated namelist"
for x in namelist:
    print x
