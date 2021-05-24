import re
s='MBAMMDXXMMMGGMMZ'
newlist = [m.group() for m in re.finditer(r'(.)\1*', s)]
newlist.sort()
newlist.sort(key=len, reverse=True)
string1 = ''.join(newlist)
newlist2 = [m.group() for m in re.finditer(r'(.)\1*', string1)]
finalstring=''
for x in newlist2:
    while len(x) > 3:
      x=x[1:]
    #print(x)
    finalstring+=x
print(finalstring)
