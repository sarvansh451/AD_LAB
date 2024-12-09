#to check of a number is prime
number=int(input("enter the number"))
flag=0
for k in range(2,number-1):
    if(number%k==0):
      flag=1

if(flag==1):
    print("not a prime number")
else:
    print("prime number")