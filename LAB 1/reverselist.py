# to print the number of list in reverse order
size=int(input("enter the size of the list "))
list=[]
for i in range(size):
    element=int((input(f"enter the element {i} ")))
    list.append(element)
list.reverse()
print(list)