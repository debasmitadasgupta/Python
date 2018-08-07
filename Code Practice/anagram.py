str1='mother in law'
str2='Hitler woman'


if len(set(str1.replace(" ",'').lower()) - set(str2.replace(" ",'').lower()) )== 0:
    print 'Anagram'
else:
    print "Not Anagram"