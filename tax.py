ai = float(input("Enter the annual income of the employee : "))
hr = float(input("Enter the house rent : "))
ins = float(input("Enter the amount paid for insurence : "))
tf = float(input("Enter the tution fee : "))
tx = ai - hr + ins + tf
if (tx < 300000):
    print("there is no tax to be paid")
elif (300000<tx<600000):
    print("the tax to be paid is : ",tx*0.1)
elif (600000<tx<1000000):
    print("the tax to be paid is : ",tx*0.15)
else:
    print("the tax to be paid is : ",tx*0.20)
    

