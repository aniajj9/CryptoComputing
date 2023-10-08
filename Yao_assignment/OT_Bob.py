import random
from OT_Party import OT_Party
from utils import is_tuple_of_bytes, modular_exponentiation, tuple_of_bytes_to_ints


class OT_Bob(OT_Party):
    r_encryption = []

    ######################### Main functions to run OT #########################

    '''
    keys: list of keys to encrypt,
    r_encryption: list of randomness used for encryption,
    '''

    def encrypt_inputs(self, keys):
        self.initialize_r_encryption(n=len(keys))

        if is_tuple_of_bytes(keys):
            keys = tuple_of_bytes_to_ints(keys)

        for i in range(len(keys)):
            pk = self.public_keys[i]
            r = self.r_encryption[i]
            encryption = self.encryption(keys[i], r, pk)
            print(f"Encryption: {encryption}")
            self.ciphertexts.append(encryption)

    ######################### Encryption #########################

    '''m: input message that is the be encryption,
    r: randomness used for encryption,
    g: group generator,
    pk: public key,
    q: prime such that p = 2q+1 is also prime
    Used third method from notes'''

    def encryption(self, m, r, pk):
        if ((m+1)**self.q) % self.p == 1:
            M = m + 1
        else:
            M = - (m + 1)
        c0 = modular_exponentiation(self.g, r, self.p)
        c1 = modular_exponentiation(pk, r, self.p) * M
        return c0, c1

    def initialize_r_encryption(self, n=2):
        for i in range(n):
            self.r_encryption.append(random.randint(1, self.q - 1))

    ######################### Helper functions #########################

    def receive_public_keys(self, public_keys):
        self.public_keys = public_keys

    def send_ciphertexts(self, other_party):
        other_party.receive_ciphertexts(self.ciphertexts)
