n = int(input())
sd = input()
count = 1
y = 0
if(sd=='sunday'):
    y=0
elif(sd=='monday'):
    y=1
elif(sd=='tuesday'):
    y=2
elif(sd=='wednesday'):
    y=3
elif(sd=='thursday'):
    y=4
elif(sd=='friday'):
    y=5
else:
    y=6
for i in range (0,y):
    count+=1
    print(' ',end=' ')
for j in range (1,n+1):
    if(count%7!=0):
        count+=1
        print(j,end=' ')
    else:
        count+=1
        print(j)
