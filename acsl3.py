rows_cols="3 4"
def minimum(a, b, c): 
   list = [a, b, c]
   return min(list)
def minimum6(a, b, c, d, e, f): 
   list = [a, b, c, d, e, f]
   return min(list)
def maximum(a, b, c): 
   list = [a, b, c] 
   return max(list)
def maximum6(a, b, c, d, e, f): 
   list = [a, b, c, d, e, f] 
   return max(list)
split_string = rows_cols.partition(' ')
r = int(split_string[0])
c = int(split_string[2])
#print (c)
array1= "171111111111"
arr1=[]
for i in range(len(array1)):
    if i % c == 0:
        portion = array1[i:i+c]
        a = []
        for j in portion:
            a.append((j))
        arr1.append(a)
print(arr1)
array2= "111111111111"
arr2=[]
for i in range(len(array2)):
    if i % c == 0:
        portion = array2[i:i+c]
        a2 = []
        for j in portion:
            a2.append((j))
        arr2.append(a2)
print(arr2)
array3= "111111111111"
arr3=[]
for i in range(len(array3)):
    if i % c == 0:
        portion = array3[i:i+c]
        a3 = []
        for j in portion:
            a3.append((j))
        arr3.append(a3)
print(arr3)
i=0
j=0
x1 = arr1[0][0]
x2 = arr2[0][0]
x3 = arr3[0][0]
#print(x1)
#print(x2)
#print(x3)
small_sum=minimum(x1,x2,x3)
#firstmove = maximum(x1,x2,x3)
print(small_sum)
#print("hi")   
while i+1 < r and j+1 < c:
    r1 = arr1[i][j+1]
    r2 = arr2[i][j+1]
    r3 = arr3[i][j+1]
    d1 = arr1[i+1][j]
    d2 = arr2[i+1][j]
    d3 = arr3[i+1][j]
    print("values:")
    print(r1)
    print(r2)
    print(r3)
    print(d1)
    print(d2)
    print(d3)
    peak = maximum6(r1, r2, r3, d1, d2, d3)
    print("peak")
    print(peak)
    if (peak == r1 )and (peak != r2 and peak != r3 and peak != d1 and peak != d2 and peak !=d3):
       small_sum=int(minimum(r1, r2, r3))+int(small_sum)
       j=j+1
       print("p1")
    elif (peak == r2 )and (peak != r1 and peak != r3 and peak != d1 and peak != d2 and peak !=d3):
        small_sum=int(minimum(r1, r2, r3))+int(small_sum)
        j=j+1
        print("p2")
    elif (peak == r3 )and (peak != r1 and peak != r2 and peak != d1 and peak != d2 and peak !=d3):
       print("p3")
       small_sum=int(minimum(r1, r2, r3))+int(small_sum)
       j=j+1
    elif (peak == d1 )and (peak != r1 and peak != r2 and peak != r3 and peak != d2 and peak !=d3):
        i =i+1
        print("p4")
        small_sum=int(minimum(d1, d2, d3))+int(small_sum)
    elif (peak == d2 )and (peak != r1 and peak != r2 and peak != r3 and peak != d1 and peak !=d3):
        i =i+1
        print("p5")
        small_sum=int(minimum(d1, d2, d3))+int(small_sum)
    elif (peak == d3 )and (peak != r1 and peak != r2 and peak != r3 and peak != d2 and peak !=d1):
        i =i+1
        print("p6")
        small_sum=int(minimum(d1, d2, d3))+int(small_sum)
    else:
        print("hi")
        j=j+1
        i = i+1
        small_sum=int(minimum(arr1[i][j], arr2[i][j], arr3[i][j]))+int(small_sum)
    print("smallsum")
    print(small_sum)
print(small_sum)
