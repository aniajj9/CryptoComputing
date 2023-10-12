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
    ('0-', '0+'): True,
    ('0-', 'A-'): True,
    ('0-', 'A+'): True,
    ('0-', 'B-'): True,
    ('0-', 'B+'): True,
    ('0-', 'AB-'): True,
    ('0-', 'AB+'): True,

    ('0+', '0+'): True,
    ('0+', 'A+'): True,
    ('0+', 'B+'): True,
    ('0+', 'AB+'): True,

    ('A-', 'A-'): True,
    ('A-', 'A+'): True,
    ('A-', 'AB-'): True,
    ('A-', 'AB+'): True,

    ('A+', 'A+'): True,
    ('A+', 'AB+'): True,

    ('B-', 'B-'): True,
    ('B-', 'B+'): True,
    ('B-', 'AB-'): True,
    ('B-', 'AB+'): True,

    ('B+', 'B+'): True,
    ('B+', 'AB+'): True,

    ('AB-', 'AB-'): True,
    ('AB-', 'AB+'): True,

    ('AB+', 'AB+'): True,
}

def check_compatibility(alice_blood, bob_blood):
    return blood_type_table.get((alice_blood, bob_blood), False)