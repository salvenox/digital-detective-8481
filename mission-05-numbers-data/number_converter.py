
try:
    number = int(input("Enter a positive decimal number: "))

    if number <= 0:
        print("Please enter a positive number.")

    else:
        binary = bin(number)[2:]
        hexadecimal = hex(number)[2:].upper()

        print("Decimal:", number)
        print("Binary:", binary)
        print("Hexadecimal:", hexadecimal)

except ValueError:
    print("Invalid input! Please enter a whole number.")
