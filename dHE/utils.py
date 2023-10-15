def encode_blood_type(blood_type_string):
    # Define blood type encodings
    blood_types = {
        '0-': [0, 0, 0],
        '0+': [0, 0, 1],
        'A-': [1, 0, 0],
        'A+': [1, 0, 1],
        'B-': [0, 1, 0],
        'B+': [0, 1, 1],
        'AB-': [1, 1, 0],
        'AB+': [1, 1, 1]
    }
    return blood_types.get(blood_type_string)

# Create a compatibility table
blood_type_table = {
    ('0-', '0-'): True,

    ('0+', '0-'): True,
    ('0+', '0+'): True,

    ('A-', '0-'): True,
    ('A-', 'A-'): True,

    ('A+', '0-'): True,
    ('A+', '0+'): True,
    ('A+', 'A-'): True,
    ('A+', 'A+'): True,

    ('B-', '0-'): True,
    ('B-', 'B-'): True,

    ('B+', '0-'): True,
    ('B+', '0+'): True,
    ('B+', 'B-'): True,
    ('B+', 'B+'): True,

    ('AB-', '0-'): True,
    ('AB-', 'A-'): True,
    ('AB-', 'B-'): True,
    ('AB-', 'AB-'): True,

    ('AB+', '0-'): True,
    ('AB+', '0+'): True,
    ('AB+', 'A-'): True,
    ('AB+', 'A+'): True,
    ('AB+', 'B-'): True,
    ('AB+', 'B+'): True,
    ('AB+', 'AB-'): True,
    ('AB+', 'AB+'): True,
}


def check_compatibility(alice_blood, bob_blood):
    return blood_type_table.get((alice_blood, bob_blood), False)