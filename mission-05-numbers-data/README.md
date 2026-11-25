# Mission 5 — Numbers and data

## 1. Task / objective
The objective of Mission 5 is to understand positional number systems (decimal, binary, and hexadecimal), perform manual step-by-step conversions, verify mathematical calculations using Python built-in functions, build an interactive number converter program (`number_converter.py`), and analyze how digital systems store and encode human text.

## 2. Work completed
- Calculated all seven required number conversions by hand, showing complete division and positional notation steps.
- Verified manual calculations against Python's built-in `bin()`, `hex()`, and `int()` functions in the interactive shell.
- Authored and tested a working Python CLI application: `mission-05-numbers-data/number_converter.py`.
- Tested the converter with three positive integers (42, 255, and 1024) and documented the outputs.
- Researched ASCII decimal values for uppercase and lowercase letters and explained the role of character encoding standards (ASCII and UTF-8).

---

### Task 5.1 — Convert numbers by hand

| Question | Your working and answer |
| :--- | :--- |
| **Convert decimal 13 to binary** | Repeated division by 2:<br>• $13 \div 2 = 6$ with remainder **1**<br>• $6 \div 2 = 3$ with remainder **0**<br>• $3 \div 2 = 1$ with remainder **1**<br>• $1 \div 2 = 0$ with remainder **1**<br>Reading remainders from bottom to top: **`1101₂`** |
| **Convert decimal 25 to binary** | Repeated division by 2:<br>• $25 \div 2 = 12$ with remainder **1**<br>• $12 \div 2 = 6$ with remainder **0**<br>• $6 \div 2 = 3$ with remainder **0**<br>• $3 \div 2 = 1$ with remainder **1**<br>• $1 \div 2 = 0$ with remainder **1**<br>Reading remainders from bottom to top: **`11001₂`** |
| **Convert binary 1010 to decimal** | Positional expansion in base 2:<br>$(1 \times 2^3) + (0 \times 2^2) + (1 \times 2^1) + (0 \times 2^0)$<br>$= (1 \times 8) + (0 \times 4) + (1 \times 2) + (0 \times 1)$<br>$= 8 + 0 + 2 + 0 = \mathbf{10_{10}}$ |
| **Convert binary 1101 to decimal** | Positional expansion in base 2:<br>$(1 \times 2^3) + (1 \times 2^2) + (0 \times 2^1) + (1 \times 2^0)$<br>$= (1 \times 8) + (1 \times 4) + (0 \times 2) + (1 \times 1)$<br>$= 8 + 4 + 0 + 1 = \mathbf{13_{10}}$ |
| **Convert hexadecimal A to decimal** | Hexadecimal symbol $A$ equals 10 in base 10:<br>$(10 \times 16^0) = 10 \times 1 = \mathbf{10_{10}}$ |
| **Convert hexadecimal 1F to decimal** | Positional expansion in base 16 ($F = 15$):<br>$(1 \times 16^1) + (15 \times 16^0)$<br>$= (1 \times 16) + (15 \times 1)$<br>$= 16 + 15 = \mathbf{31_{10}}$ |
| **Convert binary 1111 to hexadecimal** | Evaluate 4-bit nibble into decimal:<br>$(1 \times 8) + (1 \times 4) + (1 \times 2) + (1 \times 1) = 8 + 4 + 2 + 1 = 15$<br>In hexadecimal, the decimal value 15 is represented by the single symbol **`F₁₆`**. |

---

### Task 5.2 — Verify using Python

Tested in Python interactive shell:

| Target Conversion | Python Expression Tested | Python Output | Matches Manual Calculation? |
| :--- | :--- | :--- | :---: |
| **13 (dec to bin)** | `bin(13)` | `'0b1101'` | Yes (`1101`) |
| **25 (dec to bin)** | `bin(25)` | `'0b11001'` | Yes (`11001`) |
| **1010 (bin to dec)** | `int('1010', 2)` | `10` | Yes (`10`) |
| **1101 (bin to dec)** | `int('1101', 2)` | `13` | Yes (`13`) |
| **A (hex to dec)** | `int('A', 16)` | `10` | Yes (`10`) |
| **1F (hex to dec)** | `int('1F', 16)` | `31` | Yes (`31`) |
| **1111 (bin to hex)** | `hex(0b1111)` | `'0xf'` | Yes (`F`) |

---

### Task 5.3 — Build a small number converter

Program written: `mission-05-numbers-data/number_converter.py`

#### Test Execution Table:
| Test number (Decimal) | Binary output | Hexadecimal output |
| :---: | :--- | :--- |
| **42** | `101010` (Prefix: `0b101010`) | `2A` (Prefix: `0x2A`) |
| **255** | `11111111` (Prefix: `0b11111111`) | `FF` (Prefix: `0xFF`) |
| **1024** | `10000000000` (Prefix: `0b10000000000`) | `400` (Prefix: `0x400`) |

#### Explanation of conversion functions:
- **`bin(x)`**: Takes an integer as input and returns its binary representation formatted as a string prefixed with `'0b'`. It calculates how the value is composed of powers of 2.
- **`hex(x)`**: Takes an integer as input and returns its hexadecimal representation formatted as a string prefixed with `'0x'`. It groups the binary bits into 4-bit nibbles and converts each nibble to a base-16 digit (`0-9`, `a-f`).

---

### Task 5.4 — How is text stored?

1. **ASCII Decimal Codes**:
   - Uppercase **'A'**: **65** (Binary: `01000001`)
   - Lowercase **'a'**: **97** (Binary: `01100001`)
   *(Notice that the difference between uppercase and lowercase in ASCII is exactly 32, which corresponds to toggling bit 5: `00100000`)*.

2. **Why computers need an encoding standard**:
   Physical computer hardware (transistors, memory capacitors, and buses) can only store and manipulate binary voltage states ($0$ and $1$). An encoding standard is essential because it establishes a universal, deterministic mapping table that associates specific numerical binary values with human-readable textual symbols, ensuring that text written on one machine is displayed identically on any other machine in the world.

3. **Example of a character outside basic ASCII**:
   - The **Indian Rupee symbol (`₹`)**: Unicode code point **`U+20B9`** (stored in UTF-8 as a 3-byte sequence: `0xE0 0xA4 0xB9`). Basic 7-bit ASCII only supports codes 0 to 127 (English alphabet, numbers, and basic punctuation), so symbols like `₹` require modern multi-byte UTF-8 encoding.

---

## 3. Commands / tools used
| Command / Function | Purpose |
| :--- | :--- |
| `python3 mission-05-numbers-data/number_converter.py` | Runs the interactive number conversion tool. |
| `bin()` | Python built-in function to convert integer to binary string. |
| `hex()` | Python built-in function to convert integer to hexadecimal string. |
| `int(str, base)` | Python built-in function to parse a string representation in a specific base to base 10. |

## 4. My understanding
- All computer data—whether integers, floating-point numbers, text, images, or instructions—is physically represented as binary bits.
- Binary (base 2) aligns directly with transistor logic gates. Hexadecimal (base 16) serves as human-friendly shorthand for binary, where each hexadecimal digit represents exactly 4 binary bits (one nibble).
- UTF-8 is backward-compatible with 7-bit ASCII while expanding dynamically up to 4 bytes to represent over 149,000 global characters, symbols, and emojis.

## 5. Difficulties faced
- No major difficulties. Stripping the default `'0b'` and `'0x'` prefixes from Python's return values allowed clean formatted output for the user.

## 6. How I resolved them
- Used string slicing (`[2:]`) and `.upper()` to format the binary and hexadecimal values cleanly.

## 7. Evidence / files
- `mission-05-numbers-data/number_converter.py` (working converter script)
- `mission-05-numbers-data/README.md` (this report)

## 8. Commit details
- **Commit message**: `Build number converter and practise data representation`
- **Branch**: `main`
- **Push target**: `origin main`
