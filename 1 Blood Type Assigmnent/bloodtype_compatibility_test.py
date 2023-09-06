# Create a compatibility table
blood_type_table = {
    # 0- compatibility
    (0b000, 0b000): True,  # 0- can receive from 0-
    (0b000, 0b001): True,  # 0- can receive from 0+
    (0b000, 0b100): True,  # 0- can receive from A-
    (0b000, 0b101): True,  # 0- can receive from A+
    (0b000, 0b010): True,  # 0- can receive from B-
    (0b000, 0b011): True,  # 0- can receive from B+
    (0b000, 0b110): True,  # 0- can receive from AB-
    (0b000, 0b111): True,  # 0- can receive from AB+

    # 0+ compatibility
    (0b001, 0b001): True,  # 0+ can receive from 0+
    (0b001, 0b101): True,  # 0+ can receive from A+
    (0b001, 0b011): True,  # 0+ can receive from B+
    (0b001, 0b111): True,  # 0+ can receive from AB+

    # A- compatibility
    (0b100, 0b100): True,  # A- can receive from A-
    (0b100, 0b101): True,  # A- can receive from A+
    (0b100, 0b110): True,  # A- can receive from AB-
    (0b100, 0b111): True,  # A- can receive from AB+

    # A+ compatibility
    (0b101, 0b101): True,  # A+ can receive from A+
    (0b101, 0b111): True,  # A+ can receive from AB+

    # B- compatibility
    (0b010, 0b010): True,  # B- can receive from B-
    (0b010, 0b011): True,  # B- can receive from B+
    (0b010, 0b110): True,  # B- can receive from AB-
    (0b010, 0b111): True,  # B- can receive from AB+

    # B+ compatibility
    (0b011, 0b011): True,  # B+ can receive from B+
    (0b011, 0b111): True,  # B+ can receive from AB+

    # AB- compatibility
    (0b110, 0b110): True,  # AB- can receive from AB-
    (0b110, 0b111): True,  # AB- can receive from AB+

    # AB+ compatibility
    (0b111, 0b111): True,  # AB+ can receive from AB+
}


def encode_blood_type(blood_type_string):
    # Define blood type encodings
    blood_types = {
        '0-': 0b000,
        '0+': 0b001,
        'A-': 0b100,
        'A+': 0b101,
        'B-': 0b010,
        'B+': 0b011,
        'AB-': 0b110,
        'AB+': 0b111
    }
    return blood_types.get(blood_type_string)


# Function for truth table based compatibility
def truth_table_compatibility(blood_type_receiver, blood_type_donor) -> bool:
    blood_type_receiver_encoded = encode_blood_type(blood_type_receiver)
    blood_type_donor_encoded = encode_blood_type(blood_type_donor)
    return blood_type_table.get((blood_type_receiver_encoded, blood_type_donor_encoded), False)


# Function for logic based compatibility
def logic_compatibility(blood_type_receiver, blood_type_donor) -> bool:
    blood_type_receiver_encoded = encode_blood_type(blood_type_receiver)
    blood_type_donor_encoded = encode_blood_type(blood_type_donor)

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
        are_bits_compatible(blood_type_receiver_encoded, blood_type_donor_encoded, bit_position) for bit_position in
        range(3))


blood_types = ["A-", "A+", "B-", "B+", "AB-", "AB+", "0-", "0+"]


# Check if both functions return the same result for a pair
def are_functions_equivalent():
    for blood_receiver in blood_types:
        for blood_donor in blood_types:
            truth_table = truth_table_compatibility(blood_receiver, blood_donor)
            logic = logic_compatibility(blood_receiver, blood_donor)
            if truth_table != logic:
                print(
                    f"Error for receiver: {blood_receiver} and donor: {blood_donor}. Logic: {logic}, truth table: {truth_table}")
                return False
    return True


# Print blood compatibility for all blood types
def print_blood_compatibility():
    if are_functions_equivalent():
        # If both functions return the same, display the results
        for blood_receiver in blood_types:
            for blood_donor in blood_types:
                print(
                    f"{blood_receiver} can receive blood from {blood_donor}: {truth_table_compatibility(blood_receiver, blood_donor)}")


print_blood_compatibility()
