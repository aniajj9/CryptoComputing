import random
from Party import Party
from utils import find_modulo_inverse, is_safe_prime
from blood_types import blood_types_encoding


class Alice(Party):
    ciphertexts = []
    plaintext = 0
    sk_gen = 0
    sk_ogen = []

    def choose_blood_type(self):
        self.blood_type = blood_types_encoding[random.randint(0, 7)]

    def generate_keys(self):
        self.set_sk_gen(random.randint(0, self.q))
        self.key_generation()

        for i in range(0, 7):
            self.sk_ogen.append(random.randint(0, self.q))

        self.multiple_oblivious_key_generation(7)
    
    def receive_ciphertexts(self, ciphertexts):
        self.ciphertexts = ciphertexts

    def send_public_keys(self, other_party):
        other_party.receive_public_keys(self.public_keys)

    def decrypt_blood_compatibility(self):
        self.decrypt(self.sk_gen, self.ciphertexts[self.blood_type][0], self.ciphertexts[self.blood_type][1])

    '''sk: secret key used to create corresponding pk,
    q: prime such that 2q + 1 is also prime,
    g: generator in Zp of order q'''

    def key_generation(self):
        self.public_keys.append((self.g**(self.sk_gen)) % self.p)

    '''r: randomness,
    q: prime such that 2q + 1 is also prime,
    g: generator in Zp of order q,
    '''
    def single_oblivious_key_generation(self, r):
        h = (r ** 2) % self.p
        self.public_keys.append(h)

    def multiple_oblivious_key_generation(self, n):
        for i in range(0, n):
            self.single_oblivious_key_generation(self.sk_ogen[i])

    def set_sk_gen(self, sk):
        self.sk_gen = sk

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
