from Alice import Alice
from Bob import Bob
from blood_types import blood_types_encoding, logic_compatibility

blood_types_encoding_arrays = [[0, 0, 0], [0, 0, 1], [1, 0, 0], [1, 0, 1], [0, 1, 0], [0, 1, 1], [1, 1, 0], [1, 1, 1]]

exceptions = []
correct = []

for i in range(len(blood_types_encoding)):
    for j in range(len(blood_types_encoding)):
        logic_result = logic_compatibility(blood_types_encoding[i], blood_types_encoding[j])

        # Move the instantiation of Alice and Bob here
        alice = Alice(blood_types_encoding_arrays[i])
        bob = Bob(blood_types_encoding_arrays[j])

        bob.garbling_boolean_compatibility(alice)
        bob.fake_ot(alice)
        bob.encoding(alice)
        alice.evaluate()
        alice.send_Z_to_Bob(bob)
        result = bob.decode()

        if result != logic_result:
            exceptions.append(
                f"different vals for {blood_types_encoding_arrays[i]}, {blood_types_encoding_arrays[j]}: logic {logic_result}, protocol: {result}")
        else:
            correct.append(
                f"same vals for {blood_types_encoding_arrays[i]}, {blood_types_encoding_arrays[j]}: logic {logic_result}, protocol: {result}")

print("Different values for: ")
print(exceptions)
print("---------------")
print("Same values for: ")
print(correct)
