dict={}
dict1={}
s="Vidhi is Vidhi who is Vidhi"

strList=s.split(" ")
# letter occurence
for letter in s.replace(" ",''):
    dict[letter]=s.count(letter)

print  dict
# words occurence
for word in strList:
    dict1[word]=strList.count(word)

print dict1