from functools import reduce
l1=[1,2,3]
l2=[]
multiply_result= reduce((lambda x,y : x*y),l1)
for i in l1:
    l2.append(multiply_result/i)

#print l2