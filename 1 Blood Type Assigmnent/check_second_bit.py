def compare_bits(number1, number2, bit_position):
    bit1 = (number1 >> bit_position) & 1
    bit2 = (number2 >> bit_position) & 1
    return bit1 == bit2

# Example usage:
number1 = 0b010
number2 = 0b100

print(compare_bits(number1, number2, 0))
print(compare_bits(number1, number2, 1))
print(compare_bits(number1, number2, 2))