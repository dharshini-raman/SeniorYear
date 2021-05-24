edges ="98 91"
count = (edges.count(' '))
edge1=[]   
edge=edges.split(' ')
edge1=list(map(int, edge))
edge1.sort()
#print(edge1)
edge=[str(i) for i in edge1]
print(edge)
x=0
sum = 0
part=0
string=""
E = [int(i[x]) for i in edge]
E.sort()
print(E)
while (E[x] < count+1):
    #print("Edge")
    #print(edge[x][1])
    result = [part for part in edge if part.startswith(edge[x][1])]    
    print(result)
    for i in result:
        #print("hi")
        #print(x)
        #print(result)
        print(str(E[x])+string.join(i))
        num = int((str(E[x])+string.join(i)))
        snum=str(num)
        if(snum[0]==snum[2]):
           print("Hi"+snum[0]+snum[2])
        else:
            sum = sum + int((str(E[x])+string.join(i)))
    string=""
    x=x+1
    if x == count+1:
        break
print(sum)
