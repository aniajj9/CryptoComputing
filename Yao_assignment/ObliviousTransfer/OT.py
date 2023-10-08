from Yao_assignment.ObliviousTransfer.OT_Alice import OT_Alice
from Yao_assignment.ObliviousTransfer.OT_Bob import OT_Bob


def run_OT(x, y, n=2, alice=None, bob=None):
    if alice is None:
        alice = OT_Alice()

    if bob is None:
        bob = OT_Bob()

    alice.choose(x)
    bob.choose(y)
    alice.generate_keys()
    alice.send_public_keys(bob)
    bob.encrypt_inputs(keys=y)
    bob.send_ciphertexts(alice)
    return alice.decrypt_output()


def run_Yao_OT(alice, bob):
    j = 1
    # Run OT for each of Alice's bits
    for i in range(len(alice.input)):
        alice.garbled_x.append(
            run_OT(alice.input[i], bob.keys[j]))
        j += 2
