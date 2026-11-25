# Mission 05 — Number Systems and Data Representation

## 1. Task / Objective

The objective of this mission was to understand decimal, binary and hexadecimal number systems, practise number conversions, create a Python number converter, and learn about ASCII encoding.

## 2. Work Completed

- Learned decimal, binary and hexadecimal number systems.
- Practised manual conversions between different number systems.
- Used Python built-in functions to verify conversions.
- Created a number converter program.
- Tested the program with three positive decimal numbers.
- Learned ASCII encoding and character representation.

## 3. Number Systems

### Decimal (Base 10)
Uses ten digits: 0 to 9.

### Binary (Base 2)
Uses two digits: 0 and 1. Computers use binary representations for digital data.

### Hexadecimal (Base 16)
Uses sixteen symbols: 0 to 9 and A to F.

## 4. Manual Conversions

Practised the following conversions:

- Decimal 13 = Binary 1101
- Decimal 26 = Hexadecimal 1A
- Binary 10110 = Decimal 22
- Hexadecimal 3A = Decimal 58
- Decimal 19 = Binary 10011
- Decimal 45 = Hexadecimal 2D

## 5. Python Conversion Functions

Used Python's built-in functions:

| Function | Purpose |
|---|---|
| `bin()` | Converts an integer to a binary string |
| `hex()` | Converts an integer to a hexadecimal string |
| `int(value, 2)` | Converts a binary string to an integer |
| `int(value, 16)` | Converts a hexadecimal string to an integer |

## 6. Number Converter Program

File: `number_converter.py`

The program accepts a positive decimal integer and displays its binary and hexadecimal representations.

Commands used for execution:

```bash
python3 mission-05-numbers-data/number_converter.py
```

### Test Cases

| Decimal Input | Binary Output | Hexadecimal Output |
|---:|---:|---:|
| 13 | 1101 | D |
| 45 | 101101 | 2D |
| 255 | 11111111 | FF |

Also tested zero and invalid text input to check input validation.

## 7. ASCII Encoding

ASCII stands for American Standard Code for Information Interchange.

ASCII assigns numerical codes to characters.

| Character | Decimal ASCII Value |
|---|---:|
| A | 65 |
| a | 97 |

Python commands practised:

- `ord('A')` returns 65.
- `ord('a')` returns 97.
- `chr(65)` returns 'A'.
- `chr(97)` returns 'a'.

Python's `ord()` returns a Unicode code point. For ASCII characters, this value matches the ASCII code.

## 8. My Understanding

I learned how numbers are represented in different number systems and how Python can convert between them. I also understood how characters are represented using numerical codes.

## 9. Difficulties Faced

Understanding the difference between character values and their numerical codes required practice.

## 10. How I Resolved Them

I practised using Python's `ord()` and `chr()` functions and checked their outputs.

## 11. Evidence / Files

- `number_converter.py` — Python conversion program.
- This README — Documentation of number systems, conversions and ASCII encoding.

## 12. Commit Details

To be updated after committing and pushing this mission.