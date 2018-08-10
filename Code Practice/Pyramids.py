# *
#
# * *
#
# * * *
#
# * * * *
#
# * * * * *
#


def simplePyramid(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print("*"),
        print "\n"

simplePyramid(5)


#         *
#       * *
#     * * *
#   * * * *
# * * * * *

def func1(n):
    k=2*n-2
    for i in range(0,n):
        for j in range(0,k):
            print(" "),
        k=k-1
        for l in range(0,n+1):
            print("*")
        print "\n"

func1(5)