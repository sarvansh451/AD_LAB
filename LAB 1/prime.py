size = int(input("Enter the size of the array: "))

arr = []

for i in range(size):

    element = int(input(f"Enter the element {i}: "))

    arr.append(element)



for j in range(size):

    num = arr[j]

    flag = 0

    if num > 1:  # Prime numbers are greater than 1

        for k in range(2, num):

            if num % k == 0:

                flag = 1

                break

        if flag == 0:

            print(num)