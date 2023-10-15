import unittest
from utils import check_compatibility
from HomomorphicEncryption import run_homomorphic_encryption
from KeyGenerator import KeyGenerator
from utils import encode_blood_type
from Alice import Alice
from Bob import Bob

class TestHomomorphicEncryption(unittest.TestCase):
    def setUp(self):
        self.blood_types = ['0-', '0+', 'A-', 'A+', 'B-', 'B+', 'AB-', 'AB+']
    
    def test_encryption_decryption(self):
        for alice_blood in self.blood_types:
            encoded_alice_blood = encode_blood_type(alice_blood)
            # Initialize Alice and generate keys
            alice = Alice(encoded_alice_blood)

            # Encrypt blood type and print ciphertexts
            alice_ciphertext = alice.compute_ciphertexts()
            print("Alice ciphertext: ", alice_ciphertext)

            # Decrypt ciphertexts and print results
            decrypted_data = [alice.decrypt(i) for i in alice_ciphertext]
            print("Alice decrypt: ", decrypted_data)

            assert encoded_alice_blood == decrypted_data

    def test_interaction(self):
        key_gen = KeyGenerator()

        for alice_blood in self.blood_types:
            for bob_blood in self.blood_types:
                is_compatible = check_compatibility(bob_blood, alice_blood)
                result = run_homomorphic_encryption(alice_blood, bob_blood, key_gen)
                print(f"truth table: {is_compatible}")
                self.assertEqual(is_compatible, result)    
    
if __name__ == '__main__':
    unittest.main()
