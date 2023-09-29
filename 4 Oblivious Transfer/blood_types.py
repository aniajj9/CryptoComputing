
# Function for logic based compatibility


def logic_compatibility(blood_type_receiver, blood_type_donor) -> bool:

    # Sub-function that checks if two binary numbers are compatible at a bit specified by a bit position
    # Returns true if:
    #   - The two bits are the same
    #   or
    #   - The bit in the first number is 0
    def are_bits_compatible(number1, number2, bit_position) -> bool:
        bit1 = (number1 >> bit_position) & 1
        bit2 = (number2 >> bit_position) & 1
        return bit1 == bit2 or not (number1 & (1 << bit_position))

    return all(
        are_bits_compatible(blood_type_receiver, blood_type_donor, bit_position) for bit_position in
        range(3))


blood_types_encoding = [0b000, 0b001, 0b100, 0b101, 0b010, 0b011, 0b110, 0b111]
