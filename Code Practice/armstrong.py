n=153
sumNum=0

a=list(map(int,str(n)))
print a

for i in range(0,len(a)):
    sumNum = sumNum + a[i]**3

if sumNum==n :
    print 'Armstrong'
else:
    print "Not Armstrong"
