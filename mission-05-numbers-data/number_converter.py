#!/usr/bin/env python3
"""
The Digital Detective - Mission 5
Number Systems Converter (Decimal to Binary & Hexadecimal)
"""

def convert_number(decimal_value: int):
    """Converts a positive decimal integer into binary and hexadecimal."""
    binary_str = bin(decimal_value)[2:]      # Remove '0b' prefix
    hex_str = hex(decimal_value)[2:].upper()  # Remove '0x' prefix and uppercase
    return binary_str, hex_str

def main():
    print("=== The Digital Detective: Number Converter ===")
    try:
        user_input = input("Enter a positive decimal integer: ").strip()
        decimal_val = int(user_input)

        if decimal_val < 0:
            print("Error: Please enter a positive integer (0 or greater).")
            return

        binary_result, hex_result = convert_number(decimal_val)

        print("\n--- Conversion Results ---")
        print(f"Decimal (Base 10):     {decimal_val}")
        print(f"Binary (Base 2):       0b{binary_result} ({binary_result})")
        print(f"Hexadecimal (Base 16): 0x{hex_result} ({hex_result})")

    except ValueError:
        print("Error: Invalid input! Please enter digits only.")

if __name__ == "__main__":
    main()
