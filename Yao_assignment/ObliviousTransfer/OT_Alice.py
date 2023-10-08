import random
from Yao_assignment.ObliviousTransfer.OT_Party import OT_Party
from Yao_assignment.utils import find_modulo_inverse


class OT_Alice(OT_Party):
    ciphertexts = []
    plaintext = 0
    secret_keys = []

    ######################### Main functions to run OT #########################

    '''n: number of keys to generate'''

    def generate_keys(self, n=2):
        self.initialize_secret_keys(n)

        for i in range(0, n):
            if i != self.chosen_input:
                self.perform_oblivious_key_generation(self.secret_keys[i])
            else:
                self.perform_normal_key_generation()

    '''function to decrypt the output'''

    def decrypt_output(self):
        return self.decrypt_ciphertext(
            self.secret_keys[self.chosen_input], self.ciphertexts[self.chosen_input][0], self.ciphertexts[self.chosen_input][1])

    ######################### Key generation #########################

    '''sk: secret key used to create corresponding pk,
    q: prime such that 2q + 1 is also prime,
    g: generator in Zp of order q'''

    def perform_normal_key_generation(self):
        self.public_keys.append(
            (self.g**(self.secret_keys[self.chosen_input])) % self.p)

    '''r: randomness,
    q: prime such that 2q + 1 is also prime,
    g: generator in Zp of order q,
    '''

    def perform_oblivious_key_generation(self, r):
        h = (r ** 2) % self.p
        self.public_keys.append(h)

    ######################### Decryption #########################

    '''sk: secret key,
    c0: first part of ciphertext,
    c1: second part of ciphertext,
    q: prime such that 2q+1 is also prime
    Used third method from notes
    '''

    def decrypt_ciphertext(self, sk, c0, c1):
        value = find_modulo_inverse(c0**(sk), self.p)
        M = (c1 * value) % self.p
        return M - 1 if M <= self.q else -M - 1

    ######################### Initialization of the secret keys #########################

    '''n: number of keys to generate'''

    def initialize_secret_keys(self, n=2):
        for i in range(n):
            self.secret_keys.append(random.randint(1, self.q - 1))

    ######################### Helper functions #########################

    def receive_ciphertexts(self, ciphertexts):
        self.ciphertexts = ciphertexts

    def send_public_keys(self, other_party):
        other_party.receive_public_keys(self.public_keys)
