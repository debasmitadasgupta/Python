# l1=[5,2,1,6,9]
#
# for i in range(0,len(l1)):
#     for j in range(i,len(l1)):
#         if l1[j]> l1[j+1]:
#             t=l1[j]
#             l1[j]=l1[j+1]
#             l1[j+1]=t
#
# print l1

l1=[5,2,1,6,9]

for i in range(0,len(l1)):
    for j in range(i+1, len(l1)):
        if l1[i]> l1[j]:
            t=l1[i]
            l1[i]=l1[j]
            l1[j]=t

print l1