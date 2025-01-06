print("sarvansh")
print("2205238")

def is_palindrome(num):
    num_str = str(num)
    return num_str == num_str[::-1]


def is_perfect(num):
    divisors_sum = 0
    for i in range(1, num):
        if num % i == 0:
            divisors_sum += i
    return divisors_sum == num


def is_armstrong(num):
    num_str = str(num)
    total = 0
    for digit in num_str:
        total += int(digit) ** len(num_str)
    return total == num


def check_number():
    num = int(input("Enter a number: "))

    if is_palindrome(num):
        print(f"{num} is a Palindrome")
    else:
        print(f"{num} is not a Palindrome")

    if is_perfect(num):
        print(f"{num} is a Perfect number")
    else:
        print(f"{num} is not a Perfect number")

    if is_armstrong(num):
        print(f"{num} is an Armstrong number")
    else:
        print(f"{num} is not an Armstrong number")


check_number()
