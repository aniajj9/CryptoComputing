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

    def test_find_modulo_inverse(self):
        self.assertEqual(find_modulo_inverse(3, 11), 4)  # 3 * 4 ≡ 1 (mod 11)
        self.assertEqual(find_modulo_inverse(10, 17),
                         12)  # 10 * 12 ≡ 1 (mod 17)

    def test_generate_safe_prime(self):
        sp = generate_safe_prime(10, 50)
        self.assertTrue(is_safe_prime(sp))

    def test_generate_generator(self):
        q = 11
        g = generate_generator(q)
        self.assertIsInstance(g, int)

    def test_modular_exponentiation(self):
        self.assertEqual(modular_exponentiation(
            2, 5, 13), 6)  # 2^5 ≡ 6 (mod 13)

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
        self.alice.set_sk_gen(5)
        self.alice.key_generation()
        print(self.alice.pk_gen)
        c0, c1 = self.bob.encryption(m, self.r, self.alice.pk_gen)
        print(c0, c1)
        decrypted_m = self.alice.decryption(self.alice.sk_gen, c0, c1)
        self.assertEqual(decrypted_m, m)


if __name__ == '__main__':
    unittest.main()
