number = int(input("Enter a positive decimal number: "))
if number > 0:
    binary = bin(number)
    hexadecimal = hex(number)
    print("Decimal:", number)
    print("Binary:", binary)
    print("Hexadecimal:", hexadecimal)
else:
    print("Please enter a positive number.")

