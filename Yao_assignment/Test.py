import unittest

from Yao_Alice import Yao_Alice
from Yao_Bob import Yao_Bob
from OT import run_Yao_OT
from OT_Alice import OT_Alice
from OT_Bob import OT_Bob
from utils import is_prime, is_safe_prime, extended_euclidian_algorithm, generate_safe_prime, generate_generator, modular_exponentiation, generate_random_group_elements
from utils import is_tuple_of_bytes, tuple_of_bytes_to_ints


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

    def test_is_tuple_of_bytes(self):
        self.assertTrue(is_tuple_of_bytes((b'hello', b'world')))
        self.assertFalse(is_tuple_of_bytes(('hello', 'world')))
        self.assertFalse(is_tuple_of_bytes([b'hello', b'world']))
        self.assertFalse(is_tuple_of_bytes(None))
        self.assertFalse(is_tuple_of_bytes(b'hello'))

    def test_tuple_of_bytes_to_ints(self):
        self.assertEqual(tuple_of_bytes_to_ints((b'\x01', b'\x02')), (1, 2))
        with self.assertRaises(Exception) as context:
            tuple_of_bytes_to_ints(('hello', 'world'))
        self.assertEqual(str(context.exception),
                         "Input is not a tuple of bytes")


class TestAliceAndBobOT(unittest.TestCase):
    def setUp(self):
        self.r = 3  # Some random value
        self.sk = 5  # Some secret key
        self.alice = OT_Alice()
        self.bob = OT_Bob()

    def test_encryption_decryption(self):
        m = 7  # Some message
        self.alice.secret_keys.append(5)
        self.alice.perform_normal_key_generation()
        c0, c1 = self.bob.encryption(m, self.r, self.alice.public_keys[0])
        decrypted_m = self.alice.decrypt_ciphertext(
            self.alice.secret_keys.pop(), c0, c1)
        self.assertEqual(decrypted_m, m)

    def test_oblivious_key_generation(self):
        self.alice.secret_keys.append(5)
        self.alice.perform_normal_key_generation()
        self.alice.perform_oblivious_key_generation(self.r)
        self.assertEqual(self.alice.public_keys[0], 9)


class TestAliceAndBobYao(unittest.TestCase):
    def setUp(self):
        self.alice = Yao_Alice()
        self.bob = Yao_Bob()

    def test_interaction(self):
        self.alice.F_values = self.bob.garbling_boolean_compatibility()

        run_Yao_OT(self.alice, self.bob)

        self.alice.garbled_y = self.bob.encoding()
        self.bob.Z_value = self.alice.evaluate()
        self.bob.decode()


if __name__ == '__main__':
    unittest.main()
