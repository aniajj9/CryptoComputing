from Alice import Alice
from Bob import Bob


def run_OT(x, y, n=1, f=lambda x: x, encoding=None, alice=None, bob=None):
    if encoding is None:
        encoding = y

    if alice is None:
        alice = Alice()

    if bob is None:
        bob = Bob()

    alice.choose(x)
    bob.choose(y)
    alice.generate_keys()
    alice.send_public_keys(bob)
    bob.encrypt_inputs(n=n, encoding=encoding, f=f)
    bob.send_ciphertexts(alice)
    return alice.decrypt_output()
