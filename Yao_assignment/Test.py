import unittest

from Alice import Alice
from Bob import Bob
from Yao_OT import run_Yao_OT


class TestAliceAndBob(unittest.TestCase):
    def setUp(self):
        self.alice = Alice()
        self.bob = Bob()

    def test_interaction(self):
        self.bob.garbling_boolean_compatibility()

        run_Yao_OT(self.alice, self.bob)

        self.bob.Z_value = self.alice.evaluate()
        self.bob.decode()


if __name__ == '__main__':
    unittest.main()
