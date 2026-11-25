# Mission 05 — Number Systems and Data Representation

## 1. Task / Objective

The objective of this mission was to understand different number systems, practise number conversions, create a simple Python number converter, and learn about ASCII encoding.

## 2. Work Completed

- Learned Decimal, Binary and Hexadecimal number systems.
- Practised converting numbers manually.
- Used Python functions to perform number conversions.
- Created a simple Python number converter program.
- Tested the program with three positive numbers.
- Learned about ASCII values and character representation.

## 3. Number Systems

### Decimal Number System (Base 10)

The Decimal system uses ten digits from 0 to 9. It is the number system commonly used in everyday life.

### Binary Number System (Base 2)

The Binary system uses only two digits: 0 and 1. Computers use binary representations to process digital data.

### Hexadecimal Number System (Base 16)

The Hexadecimal system uses sixteen symbols: 0 to 9 and A to F.

In hexadecimal:
- A = 10
- B = 11
- C = 12
- D = 13
- E = 14
- F = 15

## 4. Manual Number Conversions

I practised the following conversions:

| Conversion | Answer |
|---|---|
| Decimal 13 to Binary | 1101 |
| Decimal 26 to Hexadecimal | 1A |
| Binary 10110 to Decimal | 22 |
| Hexadecimal 3A to Decimal | 58 |
| Decimal 19 to Binary | 10011 |
| Decimal 45 to Hexadecimal | 2D |

## 5. Python Conversion Functions

I used the following built-in Python functions:

| Function | Purpose |
|---|---|
| `bin()` | Converts an integer into a binary representation |
| `hex()` | Converts an integer into a hexadecimal representation |
| `int(value, 2)` | Converts a binary string into an integer |
| `int(value, 16)` | Converts a hexadecimal string into an integer |

Examples:

```python
bin(19)
hex(45)
int("10011", 2)
int("2D", 16)
```

Python adds prefixes automatically:
- `0b` represents Binary.
- `0x` represents Hexadecimal.

## 6. Number Converter Program

File: `number_converter.py`

I created a simple Python program that takes a positive decimal number from the user and displays its Binary and Hexadecimal representations.

### Program Code

```python
# Take a number from the user
number = int(input("Enter a positive decimal number: "))

# Check whether the number is positive
if number > 0:

    # Convert the number into Binary
    binary = bin(number)

    # Convert the number into Hexadecimal
    hexadecimal = hex(number)

    # Display the results
    print("Decimal:", number)
    print("Binary:", binary)
    print("Hexadecimal:", hexadecimal)

else:
    print("Please enter a positive number.")
```

### Command Used to Run the Program

```bash
python3 mission-05-numbers-data/number_converter.py
```

### Test Cases

| Decimal Input | Binary Output | Hexadecimal Output |
|---:|---|---|
| 13 | `0b1101` | `0xd` |
| 45 | `0b101101` | `0x2d` |
| 255 | `0b11111111` | `0xff` |

I also tested zero as input. The program displayed a message asking for a positive number.

**Note:** The program accepts whole-number input. Non-numeric text is not handled by this beginner-level version.

## 7. ASCII Encoding

ASCII stands for American Standard Code for Information Interchange.

It assigns numerical codes to characters so computers can represent and process text.

Examples:

| Character | ASCII Decimal Value |
|---|---:|
| A | 65 |
| a | 97 |
| B | 66 |
| b | 98 |

I practised the following Python functions:

| Python Command | Output |
|---|---|
| `ord('A')` | 65 |
| `ord('a')` | 97 |
| `chr(65)` | 'A' |
| `chr(97)` | 'a' |
| `chr(48)` | '0' |

The `ord()` function returns the numerical code of a character, and the `chr()` function converts a numerical code into a character.

Python uses Unicode. For standard ASCII characters, the Unicode code points match their ASCII values.

## 8. My Understanding

I learned how Decimal, Binary and Hexadecimal number systems work. I also learned how to convert numbers manually and use Python functions for conversions.

I understood that computers represent characters using numerical codes and that ASCII is one standard for representing basic characters.

## 9. Difficulties Faced

Understanding the difference between character values and their numerical codes required some practice.

## 10. How I Resolved Them

I practised using Python's `ord()` and `chr()` functions and observed their outputs to understand the difference.

## 11. Evidence / Files

- `number_converter.py` — Python program for Decimal to Binary and Hexadecimal conversion.
- `README.md` — Documentation of number systems, conversions, Python functions and ASCII encoding.

## 12. Commit Details

To be updated after committing and pushing this mission.