from Alice import Alice
from Bob import Bob
from itertools import product

# Your protocol function (replace with your actual implementation)
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




# Generate all combinations of two 3-bit arrays
combinations = list(product([0, 1], repeat=3))

# Iterate through all combinations
for input_bits1 in combinations:
    for input_bits2 in combinations:
        result = protocol(input_bits1, input_bits2)
        print(f"Input 1: {input_bits1}, Input 2: {input_bits2}, Result: {result}")
