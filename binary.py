n = int(input())
y = 0
x = 0
while (n>=2):
    r = n%2
    x = r*10**y+x
    n = n//2
    y = y+1
    if (n==1):
        x=1*10**y+x
        print(x)
