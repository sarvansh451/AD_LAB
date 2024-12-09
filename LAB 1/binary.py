#to print binary equivalent
num = int(input("Enter the element: "))
list = []

while num > 0:
    list.append(num % 2)
    num = num // 2

list.reverse()
print(list)