#gcd of two numbers
num1=int(input("enter the number 1 "))
num2=int(input("enter the number 2 "))
#gcd of two numbers
min=0
if(num1>num2):
    min=num2
else:
    min=num1
while(min>0):
    if(num1%min==0 and num2%min==0):
        print(min)
        break
    min=min-1