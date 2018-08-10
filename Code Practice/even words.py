import re

str1="This is Debo and Vidhi. They both are good."
l1=str1.split()
print l1

str2="This is Debo and Vidhi. They, both are good."

l2=re.split("[., \-!?:]+",str2)
print l2

l3=[]
for i in l2:
    if len(i)%2==0:
        l3.append(i)

print l3