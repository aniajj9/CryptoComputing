import random
from Party import Party
from utils import find_modulo_inverse, is_safe_prime
from blood_types import blood_types_encoding


class Alice(Party):
    ciphertexts = []
    plaintext = 0
    secret_keys = []

    def generate_keys(self, secret_keys=[]):
        self.initialize_secret_keys(secret_keys)
        for i in range(0, 7):
            if i != self.blood_type:
                self.perform_oblivious_key_generation(self.secret_keys[i])
            else:
                self.perform_normal_key_generation()

    def receive_ciphertexts(self, ciphertexts):
        self.ciphertexts = ciphertexts

    def send_public_keys(self, other_party):
        other_party.receive_public_keys(self.public_keys)

    def decrypt_blood_compatibility(self):
        self.decrypt(
            self.secret_keys[self.blood_type], self.ciphertexts[self.blood_type][0], self.ciphertexts[self.blood_type][1])

    '''sk: secret key used to create corresponding pk,
    q: prime such that 2q + 1 is also prime,
    g: generator in Zp of order q'''

    def perform_normal_key_generation(self):
        self.public_keys.append(
            (self.g**(self.secret_keys[self.blood_type])) % self.p)

    '''r: randomness,
    q: prime such that 2q + 1 is also prime,
    g: generator in Zp of order q,
    '''

    def perform_oblivious_key_generation(self, r):
        h = (r ** 2) % self.p
        self.public_keys.append(h)

    '''sk: secret key,
    c0: first part of ciphertext,
    c1: second part of ciphertext,
    q: prime such that 2q+1 is also prime
    Used third method from notes
    '''

    def decrypt(self, sk, c0, c1):
        value = find_modulo_inverse(c0**(sk), self.p)
        M = (c1 * value) % self.p
        return M - 1 if M <= self.q else -M - 1

    def initialize_secret_keys(self, secret_keys=[]):
        if secret_keys != []:
            self.secret_keys = secret_keys
            return

        for i in range(len(blood_types_encoding)):
            self.secret_keys.append(random.randint(1, self.q - 1))
