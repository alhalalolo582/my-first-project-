def binary_to_decimal(binary_str):

    if not all(char in "01" for char in binary_str):
        print("Invalid input. Please enter a binary number (only containing 0s and 1s).")
        return None

    digits = [int(char) for char in binary_str[::-1]]

    decimal_value = 0
    for i, digit in enumerate(digits):
        decimal_value += digit * (2**i)

    return decimal_value

while True:
  binary_str = input("Enter a binary number: ")
  decimal_value = binary_to_decimal(binary_str)
  if decimal_value is not None:
    break

print(f"The decimal equivalent of {binary_str} is {decimal_value}")
