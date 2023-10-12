import unittest
from utils import check_compatibility
from HomomorphicEncryption import run_homomorphic_encryption
from KeyGenerator import KeyGenerator

class TestAliceAndBobDHE(unittest.TestCase):
    def setUp(self):
        self.blood_types = ['0-', '0+', 'A-', 'A+', 'B-', 'B+', 'AB-', 'AB+']


    def test_interaction(self):
        print("key generation takes place... ")
        key_gen = KeyGenerator()
        print("log 0")

        for alice_blood in self.blood_types:
            for bob_blood in self.blood_types:
                is_compatible = check_compatibility((alice_blood, bob_blood), False)
                result = run_homomorphic_encryption(alice_blood, bob_blood, key_gen)
                print(f"truth table: {is_compatible}")
                #self.assertEqual(is_compatible, result)        
    
if __name__ == '__main__':
    unittest.main()
