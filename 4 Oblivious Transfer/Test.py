import unittest
from Alice import Alice
from Bob import Bob
from utils import is_prime, is_safe_prime, extended_euclidian_algorithm, find_modulo_inverse, generate_safe_prime, generate_generator, modular_exponentiation, generate_random_group_elements


class TestMathFunctions(unittest.TestCase):

    def test_is_prime(self):
        self.assertTrue(is_prime(11))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(1))

    def test_is_safe_prime(self):
        self.assertTrue(is_safe_prime(5))
        self.assertFalse(is_safe_prime(19))

    def test_extended_euclidian_algorithm(self):
        x, y = extended_euclidian_algorithm(3, 11)
        self.assertEqual(x * 3 + y * 11, 1)

    def test_generate_safe_prime(self):
        sp = generate_safe_prime(10, 50)
        self.assertTrue(is_safe_prime(sp))

    def test_generate_generator(self):
        q = 11
        g = generate_generator(q)
        self.assertIsInstance(g, int)

    def test_modular_exponentiation(self):
        self.assertEqual(modular_exponentiation(
            2, 5, 13), 6)

    def test_generate_random_group_elements(self):
        q = 11
        element = generate_random_group_elements(q)
        self.assertTrue(1 <= element < 2*q + 1)


class TestAliceAndBob(unittest.TestCase):
    def setUp(self):
        self.r = 3  # Some random value
        self.sk = 5  # Some secret key
        self.alice = Alice(q=11, g=2)
        self.bob = Bob(q=11, g=2)

    def test_encryption_decryption(self):
        m = 7  # Some message
        self.alice.secret_keys.append(5)
        self.alice.perform_normal_key_generation()
        c0, c1 = self.bob.encryption(m, self.r, self.alice.public_keys[0])
        decrypted_m = self.alice.decrypt(self.alice.secret_keys.pop(), c0, c1)
        self.assertEqual(decrypted_m, m)
    
    def test_oblivious_key_generation(self):
        self.alice.secret_keys.append(5)
        self.alice.perform_normal_key_generation()
        self.alice.perform_oblivious_key_generation(self.r)
        self.assertEqual(self.alice.public_keys[0], 9)
    
    def test_interaction(self):
        for i in range(7):
            for j in range(i):
                self.alice.choose_blood_type(i)
                self.bob.choose_blood_type(j)
                self.alice.generate_keys()
                self.alice.send_public_keys(self.bob)
                self.bob.encrypt_blood_types()
                self.bob.send_ciphertexts(self.alice)
                self.alice.decrypt_blood_compatibility()


if __name__ == '__main__':
    unittest.main()
