import unittest

from Alice import Alice
from Bob import Bob


class TestAliceAndBob(unittest.TestCase):
    def setUp(self):
        self.alice = Alice()
        self.bob = Bob()

    def test_bob(self):
        self.bob.garbling_boolean_compatibility(self.alice)
        self.bob.fake_ot(self.alice)
        self.bob.encoding(self.alice)
        self.alice.evaluate()
        self.alice.send_Z_to_Bob(self.bob)
        result = self.bob.decode()
        print(result)

    '''def test_interaction(self):
        self.bob.garbling_boolean_compatibility()

        run_Yao_OT(self.alice, self.bob)

        self.bob.Z_value = self.alice.evaluate()
        self.bob.decode()'''




if __name__ == '__main__':
    unittest.main()
