from functools import *

# use of partial
def f(a,b,c,d):
    print 1000*a + 100*b + 10*c + d

g=partial(f,4,3,2)
g(1)

#packing unpacking
def unpack(*args):
    print args

def pack(a,b,c):
    print a,b,c

unpack([1,2,3,4])
args1=[1,2,3]
pack(*args1)

#character to interger
s='0'
print ord(s)


#sorted() doesn't sort the container. its just used to print in the sorted order means it doesn't effect the container
l1=[5,4,2,6,4,8,6,5]
for i in sorted(l1):
    print("After using sorted", i)

for i in set(l1):
    print ("After usig set",i)