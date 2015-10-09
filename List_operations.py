__author__ = 'rudragouda'

list = ['BLR', 'CHN', 'DEL', 'HYD', 'KOL', 'MUM']

print list

list.append('Ahmbd')
list.insert(5, 'pouyg')
L = ['kcmk', 'dcffd', 'cvdcdc', 'sdvvcdv']
# list[len(list):] = L
list.extend(L)

print "The complete list is..", list
print "max element of the list is: ", max(list)
print "min element of the list is: ", min(list)
# print list.remove('BLR')

list.sort()
print list
list.reverse()
print list
list.pop()
print "after pop operation:", list
