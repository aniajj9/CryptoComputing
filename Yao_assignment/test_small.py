from Alice import Alice
from Bob import Bob
from blood_types import blood_types_encoding, logic_compatibility


blood_types_encoding_arrays = [[0, 0, 0], [0, 0, 1], [1, 0, 0], [1, 0, 1], [0, 1, 0], [0, 1, 1], [1, 1, 0], [1, 1, 1]]

exceptions = []
correct = []

def protocol(alice_values, bob_values):
    while True:
        try:
            alice = Alice(alice_values)
            bob = Bob(bob_values)

            bob.garbling_boolean_compatibility(alice)
            bob.fake_ot(alice)
            bob.encoding(alice)
            alice.evaluate()
            alice.send_Z_to_Bob(bob)
            result = bob.decode()
            return result
        except Exception:
            continue

for i in range(len(blood_types_encoding)):
    for j in range(len(blood_types_encoding)):
        logic_result = logic_compatibility(blood_types_encoding[i], blood_types_encoding[j])
        result = protocol(blood_types_encoding_arrays[i], blood_types_encoding_arrays[j])

        if result != logic_result:
            exceptions.append(
                f"different values for {blood_types_encoding_arrays[i]}, {blood_types_encoding_arrays[j]}: logic {logic_result}, protocol: {result}")
        else:
            correct.append(
                f"{blood_types_encoding_arrays[i]}, {blood_types_encoding_arrays[j]}: {bool(result)}")

print("Values for which logic function and Yao protocol returned different results: ")
for val in exceptions:
    print(val)
print("---------------")
print("Values for which logic function and Yao protocol returned same results: ")
for val in correct:
    print(val)
