from typing import Optional

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


def truth_table_compatibility(blood_type_receiver, blood_type_donor) -> bool:
    blood_type_receiver_encoded = encode_blood_type(blood_type_receiver)
    blood_type_donor_encoded = encode_blood_type(blood_type_donor)
    return blood_type_table.get((blood_type_receiver_encoded, blood_type_donor_encoded), False)


def logic_compatibility(blood_type_receiver, blood_type_donor) -> bool:
    blood_type_receiver_encoded = encode_blood_type(blood_type_receiver)
    blood_type_donor_encoded = encode_blood_type(blood_type_donor)

    def are_bits_the_same(number1, number2, bit_position) -> bool:
        bit1 = (number1 >> bit_position) & 1
        bit2 = (number2 >> bit_position) & 1
        return bit1 == bit2

    # Types 0 and B
    if (blood_type_receiver_encoded >> 2) & 1 == 0:
        # Type 0
        if (blood_type_receiver_encoded >> 1) & 1 == 0:
            # Type 0-
            if (blood_type_receiver_encoded >> 0) & 1 == 0:
                return True
            # Type 0+
            elif are_bits_the_same(blood_type_receiver_encoded, blood_type_donor_encoded, 0):
                return True
        # Type B
        elif are_bits_the_same(blood_type_receiver_encoded, blood_type_donor_encoded, 1):
            # Type B-
            if (blood_type_receiver_encoded >> 0) & 1 == 0:
                return True
            # Type B+
            elif are_bits_the_same(blood_type_receiver_encoded, blood_type_donor_encoded, 0):
                return True
    # Types A and AB
    elif (blood_type_receiver_encoded >> 2) & 1 == 1:
        # Type A
        if (blood_type_receiver_encoded >> 1) & 1 == 0 and are_bits_the_same(blood_type_receiver_encoded, blood_type_donor_encoded, 2):
            # Type A-
            if (blood_type_receiver_encoded >> 0) & 1 == 0:
                return True
            # Type A+
            elif are_bits_the_same(blood_type_receiver_encoded, blood_type_donor_encoded, 0):
                return True
        # Type AB
        if (blood_type_receiver_encoded >> 1) & 1 == 1:
            #print("receiver " ,  blood_type_receiver_encoded)
            if are_bits_the_same(blood_type_receiver_encoded, blood_type_donor_encoded, 2) and are_bits_the_same(blood_type_receiver_encoded, blood_type_donor_encoded, 1):
                # Type AB-
                if (blood_type_receiver_encoded >> 0) & 1 == 0:
                    return True
                # Type AB+
                #print("recv " , blood_type_receiver_encoded)
                if are_bits_the_same(blood_type_receiver_encoded, blood_type_donor_encoded, 0):
                    return True

    return False


blood_types = ["A-", "A+", "B-", "B+", "AB-", "AB+", "0-", "0+"]

for blood_receiver in blood_types:
    for blood_donor in blood_types:
        truth_table = truth_table_compatibility(blood_receiver, blood_donor)
        logic = logic_compatibility(blood_receiver, blood_donor)
        if truth_table != logic:
            print(f"error for receiver: {blood_receiver} and donor: {blood_donor}. Logic: {logic}, truth table: {truth_table}")

