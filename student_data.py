l=[]
for i in range(0,2):
    l.append(input('enter roll no:'))
    l.append(input('enter name:'))
    l.append(input('enter ssc marks:'))
    l.append(input('enter inter marks:'))
    l.append(input('enter cgpa upto 3-2 semester:'))
    l.append(input('enter preferred programming language:'))
    l.append(input('enter career option:'))


x=1
for i in range(0,14):
    print('student',x)
    match i%7:
        case 0:print('rollno:',l[i])
        case 1:print('name:',l[i])
        case 2:print('sscmarks',l[i])
        case 3:print('inter marks',l[i])
        case 4:print('cgpa upto 3-2',l[i])
        case 5:print('proglang:',l[i])
        case 6:print('careeropt',l[i])
    if((i+1)%7==0):
        print()
        x+=1
