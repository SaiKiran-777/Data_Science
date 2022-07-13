# Factorial of a number

n = int(input())
c = 1
if (n < 0):
    print('no factorial for this number')
elif (n == 0):
    print(1)
else:
    for i in range(1,n+1):
        c = c*i
        print(c)
