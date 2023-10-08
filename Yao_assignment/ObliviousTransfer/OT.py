from Yao_assignment.ObliviousTransfer.Alice_OT import Alice_OT
from Yao_assignment.ObliviousTransfer.Bob_OT import Bob_OT


def run_OT(x, y, n=1, f=lambda x: x, encoding=None, alice=None, bob=None):
    if encoding is None:
        encoding = y

    if alice is None:
        alice = Alice_OT()

    if bob is None:
        bob = Bob_OT()

    alice.choose(x)
    #print(alice.chosen_input)
    bob.choose(y)
    alice.generate_keys()
    alice.send_public_keys(bob)
    bob.encrypt_inputs(n=n, encoding=encoding, f=f)
    bob.send_ciphertexts(alice)
    return alice.decrypt_output()
