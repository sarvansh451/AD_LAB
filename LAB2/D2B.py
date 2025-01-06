print("sarvansh")
print("2205238")

def decimal_to_binary(decimal):
    binary = ""
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal = decimal // 2
    return binary if binary else "0"

def binary_to_decimal(binary):
    decimal = 0
    for i in range(len(binary)):
        decimal += int(binary[i]) * (2 ** (len(binary) - 1 - i))
    return decimal

def convert():
    choice = input("Choose conversion (1: Decimal to Binary, 2: Binary to Decimal): ")

    if choice == '1':
        decimal = int(input("Enter a decimal number: "))
        print(f"Binary: {decimal_to_binary(decimal)}")
    elif choice == '2':
        binary = input("Enter a binary number: ")
        print(f"Decimal: {binary_to_decimal(binary)}")
    else:
        print("Invalid choice!")

convert()
