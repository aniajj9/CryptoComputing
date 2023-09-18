import unittest
from main import blood_compatibility_bedoza

class TestBloodCompatibility(unittest.TestCase):
    
    def test_compatibility(self):
        blood_type_table = {
    # 0- compatibility
    ('0-', '0-'): True,
    ('0-', '0+'): True,
    ('0-', 'A-'): True,
    ('0-', 'A+'): True,
    ('0-', 'B-'): True,
    ('0-', 'B+'): True,
    ('0-', 'AB-'): True,
    ('0-', 'AB+'): True,

    # 0+ compatibility
    ('0+', '0+'): True,
    ('0+', 'A+'): True,
    ('0+', 'B+'): True,
    ('0+', 'AB+'): True,

    # A- compatibility
    ('A-', 'A-'): True,
    ('A-', 'A+'): True,
    ('A-', 'AB-'): True,
    ('A-', 'AB+'): True,

    # A+ compatibility
    ('A+', 'A+'): True,
    ('A+', 'AB+'): True,

    # B- compatibility
    ('B-', 'B-'): True,
    ('B-', 'B+'): True,
    ('B-', 'AB-'): True,
    ('B-', 'AB+'): True,

    # B+ compatibility
    ('B+', 'B+'): True,
    ('B+', 'AB+'): True,

    # AB- compatibility
    ('AB-', 'AB-'): True,
    ('AB-', 'AB+'): True,

    # AB+ compatibility
    ('AB+', 'AB+'): True,
}


                
        for blood_receiver, blood_donor in blood_type_table.keys():
                print(blood_receiver, blood_donor)
                self.assertEqual(blood_compatibility_bedoza(blood_receiver, blood_donor), blood_type_table[blood_receiver, blood_donor])
    
if __name__ == "__main__":
    unittest.main()
