import unittest

from Alice import Alice
from Bob import Bob
from blood_types import blood_types_encoding, logic_compatibility



class TestAliceAndBob(unittest.TestCase):


    def test_bob(self):
        def setUp(alice_val, bob_val):
            self.alice = Alice(alice_val)
            self.bob = Bob(bob_val)

        def protocol(receiver, donor):
            setUp(receiver, donor)
            self.bob.garbling_boolean_compatibility(self.alice)
            self.bob.fake_ot(self.alice)
            self.bob.encoding(self.alice)
            self.alice.evaluate()
            self.alice.send_Z_to_Bob(self.bob)
            result = self.bob.decode()
            return result
        exceptions = []
        correct = []
        for receiver in blood_types_encoding:
            for donor in blood_types_encoding:
                logic_result = logic_compatibility(donor, receiver)
                protocol_result = protocol(donor, receiver)
                if protocol_result != logic_result:
                    exceptions.append(f"different vals for {self.alice.input}, {self.bob.input}: logic {logic_result}, protocol: {protocol_result}")
                else:
                    correct.append(f"same vals for {self.alice.input}, {self.bob.input}: logic {logic_result}, protocol: {protocol_result}")


        print(exceptions)

        print("---------------")
        print(correct)

    '''def test_interaction(self):
        self.bob.garbling_boolean_compatibility()

        run_Yao_OT(self.alice, self.bob)

        self.bob.Z_value = self.alice.evaluate()
        self.bob.decode()'''




if __name__ == '__main__':
    unittest.main()
