from Alice import Alice
from Bob import Bob
from utils import encode_blood_type

def run_homomorphic_encryption(alice_blood, bob_blood, key_gen=None):
    print("log 1")
    encoded_alice_blood = encode_blood_type(alice_blood)
    encoded_bob_blood = encode_blood_type(bob_blood)

    print("log 2")
    alice = Alice(encoded_alice_blood, key_gen)
    bob = Bob(encoded_bob_blood, key_gen)

    print("log 3")
    alice.generate_keys()
    print("log 4")
    alice.send_public_keys(bob)
    print("log 5")
    alice.compute_ciphertexts()
    print("log 6")
    alice.send_own_ciphertexts(bob)

    print("log 7")
    bob.compute_function()

    print("log 8")
    bob.send_result_ciphertext(alice)

    print("log 9")
    result = alice.decrypt_output(alice.result_ciphertext)
    print(f"alice blood: {alice_blood}, bob blood: {bob_blood}, result: {result}")
    return result
