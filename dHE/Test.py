import unittest
from Alice import Alice
from Bob import Bob

class TestAliceAndBobDHE(unittest.TestCase):
    def setUp(self):
        self.alice = Alice([1,0,0])
        self.bob = Bob([0,1,0])

    def test_interaction(self):
        self.alice.generate_keys()
        self.alice.send_public_keys(self.bob)
        self.alice.compute_ciphertexts()
        self.alice.send_own_ciphertexts(self.bob)

        self.bob.compute_function()
        self.bob.send_result_ciphertext()

        result = self.alice.decrypt_output()
        

    
if __name__ == '__main__':
    unittest.main()
