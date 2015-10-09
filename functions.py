__author__ = 'rudragouda'


# simple func
def my_function():
    print "Hello From My Function!"


# func with args
def my_function_with_args(username, greeting):
    print "Hello, %s , From My Function!, I wish you %s" % (username, greeting)


# return result
def sum_two_numbers(a, b):
    return a + b
print "------------------------"

my_function()
print "------------------------"
my_function_with_args("rudra", "a great year!")
print "------------------------"
x = sum_two_numbers(1, 2)
print "The value returned is %d" % x
print "------------------------"

print "....Exercise work here...."


info = 'Python'


def build_sentence(info):
    print "Using %s is very benifitial !" % info


def list_benifits():
    print "The following are benifits of using %s" % info
    print "1. More organized code"
    print "2. More readable code"
    print "3. Easier code reus"
    print "4. Allowing programmers to share and connect code together"

build_sentence(info)
list_benifits()
