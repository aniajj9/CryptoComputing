from Alice import Alice
from Bob import Bob
from utils import encode_blood_type

def run_homomorphic_encryption(alice_blood, bob_blood, key_gen=None):
    alice = Alice(encode_blood_type(alice_blood), key_gen)
    bob = Bob(encode_blood_type(bob_blood))

    alice.send_public_keys(bob)
    alice.compute_ciphertexts()
    alice.send_alice_encrypted_blood_type(bob)

    bob.compute_compatibility()
    bob.send_encrypted_result(alice)
    result = alice.decrypt(alice.encrypted_result)
    print(f"alice blood: {alice_blood}, bob blood: {bob_blood}, result: {result}")
    return result
