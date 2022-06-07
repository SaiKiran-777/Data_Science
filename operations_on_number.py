n = int(input("Enter the number"))
c = 0
for i in range (1,n):
    if(n%i==0):
        c+=1
if(c==1):
    print("it is a prime number")
else:
    print("it is not a prime number")
if (n%2==0):
    print("it is a even number")
else:
    print ("it is a odd number")
print("The sum of the number",(n*(n+1))/2)
