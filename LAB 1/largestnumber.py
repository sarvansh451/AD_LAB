#to find largest in the array
size = int(input("Enter the size of the array: "))
arr = []
for i in range(size):
    element = int(input(f"Enter the element {i}: "))
    arr.append(element)

largest=arr[0]
for j in range(size):
    if(arr[j]>largest):
        largest=arr[j]
print(largest)