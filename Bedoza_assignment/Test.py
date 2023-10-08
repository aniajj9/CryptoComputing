import unittest
from main import blood_compatibility_bedoza

class TestBloodCompatibility(unittest.TestCase):
    
    def test_compatibility(self):
        blood_type_table = {
    # 0- compatibility
    ('0-', '0-'): True,

    # 0+ compatibility
    ('0+', '0+'): True,
    ('0+', '0-'): True,

    # A- compatibility
    ('A-', 'A-'): True,
    ('A-', '0-'): True,

    # A+ compatibility
    ('A+', 'A+'): True,
    ('A+', 'A-'): True,
    ('A+', '0+'): True,
    ('A+', '0-'): True,

    # B- compatibility
    ('B-', 'B-'): True,
    ('B-', '0-'): True,

    # B+ compatibility
    ('B+', 'B+'): True,
    ('B+', 'B-'): True,
    ('B+', '0+'): True,
    ('B+', '0-'): True,


    # AB- compatibility
    ('AB-', '0-'): True,
    ('AB-', 'A-'): True,
    ('AB-', 'B-'): True,
    ('AB-', 'AB-'): True,

    # AB+ compatibility
    ('AB+', 'AB+'): True,
    ('AB+', 'AB-'): True,
    ('AB+', 'A+'): True,
    ('AB+', 'A-'): True,
    ('AB+', 'B+'): True,
    ('AB+', 'B-'): True,
    ('AB+', '0+'): True,
    ('AB+', '0-'): True,
}


                
        for blood_receiver, blood_donor in blood_type_table.keys():
                print(blood_receiver, blood_donor)
                self.assertEqual(blood_compatibility_bedoza(blood_receiver, blood_donor), blood_type_table[blood_receiver, blood_donor])
    
if __name__ == "__main__":
    unittest.main()
