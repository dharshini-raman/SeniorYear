s = 221
d = 2
r = 4
a = str(s)
b = str(d)
n=r
x=0
def getSum(n):  
     
    sum = 0
    for digit in str(n):   
      sum += int(digit)
      print(sum, 'hi')
    return sum

# Calculating octal value using function 
sum1 = oct(int(a, 8))

#oct(int(a, 8) + int(b, 8))
#print(a, "Hi")

for i in range(0, n):
        for j in range(0, i+1):
            print(sum1[2:], end=" ")
            if i==r-1:
                x = getSum(sum1[2:])+x
                print(x)
            sum1 = oct(int(sum1[2:], 8) + int(b, 8))
            
        print("\r") 

n = 5

    
print(x)        
