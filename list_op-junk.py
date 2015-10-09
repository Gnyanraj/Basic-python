# __author__ = 'rudragouda'
#
# oldlist = ['fegsf','fggf','grfh']
# newlist = ['fegsf','fggf','grfh']
# print "The complete list is..", list
# print "No of elements in the list are..", len(list)
# print "The name at the index list[0] is: ", list[0]
# print "The name at the index list[1:5] are: ", list[1:5]
# print max(list)
# print min(list)
#
# print list;
# del list[3];
# print "After deleting value at index 2 : "
# print list;
# list.pop()
# print "after pop operation:", list
#
# print "Value available at index 2 is: ", list[2]
# list[2] = 'NEWDEL'
# print "New value available at index 2 is: ", list[2]
#
# cmpres = cmp(oldlist,newlist)
# if (cmpres == 0):
#     print "Both the list are matching"
# else:
#     print "List are not matching"


#
# from collections import deque
# queue = deque(["Eric", "John", "Michael"])
# queue.append("Terry")
# queue.append("Graham")
# print queue
# print queue.popleft()
#
# def f(x): return x % 5 == 0
# print map(f, range(2, 25))

def cube(x):
    return x*x
seq1 = range(1, 11)
seq2 = range(21, 31)
print map(cube, seq1)
# seq1 = range(1,6)
# seq2 = range(11,16)
# def add(x, y): return x+y
# print map(add, seq1, seq2)


def add(x, y):
    return x+y
print reduce(add, range(1, 5))

# seq1 = range(1,6)
# seq2 = range(11,16)
# def add(x, y): return x+y
# print map(add, seq1, seq2)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print [[row[i] for row in matrix] for i in range(3)]
transposed = []
for i in range(3):
    transposed.append([row[i] for row in matrix])
print transposed
print zip(*matrix)

t = 12345, 54321, 'hello!'
print t
u = t, (1, 2, 3, 4, 5)
print u
