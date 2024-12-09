#to find sum of the array
size = int(input("Enter the size of the array: "))
arr = []
for i in range(size):
    element = int(input(f"Enter the element {i}: "))
    arr.append(element)

sum=0
for j in range(size):
    sum=sum+arr[j]
print(sum)