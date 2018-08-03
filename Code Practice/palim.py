s1='vishi'
flag=True
# j=len(s1)-1
# for i in range(0,len(s1)/2):
#     if s1[i] == s1[j]:
#         j -=1
#         continue
#     else:
#         flag=False
#         break


for i in range(0,len(s1)/2):
    if s1[i] == s1[-(i+1)]:
        continue
    else:
        flag=False
        break

if flag:
    print 'Palimdrom'
else:
    print 'Not Palindrom'