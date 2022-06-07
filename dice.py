user = int(input("enter a number"))
import random
pc = [1,2,3,4,5,6]
c = random.choice(pc)
if (user > c):
    print("user have won the game")
elif (user < c):
    print("computer have won the game")
else:
    print("computer and user draw the game")
if (user == c):
     print("play the game again")
    
    
