import random
from Party import Party
from utils import find_modulo_inverse, is_safe_prime


class Alice(Party):
    ciphertexts = []
    x = 0
    sk_gen = 0
    sk_ogen = []

    def choose(self, x):
        self.x = x

    '''sk: secret key used to create corresponding pk,
    q: prime such that 2q + 1 is also prime,
    g: generator in Zp of order q'''

    def key_generation(self):
        print(self.p, self.sk_gen, self.g)
        self.pk_gen = (self.g**(self.sk_gen)) % self.p

    def set_sk_gen(self, sk):
        self.sk_gen = sk

    '''r: randomness,
    q: prime such that 2q + 1 is also prime,
    g: generator in Zp of order q,
    '''

    def single_oblivious_key_generation(self, r):
        h = (r ** 2) % self.p
        self.pk_ogen.append(h)

    def multiple_oblivious_key_generation(self, n):
        for i in range(0, n):
            self.single_oblivious_key_generation(self.sk_ogen[i])

    def send_pk(self, other_party):
        other_party.receive_pk(self.pk_gen, self.pk_ogen)

    '''sk: secret key,
    c0: first part of ciphertext,
    c1: second part of ciphertext,
    q: prime such that 2q+1 is also prime
    Used third method from notes
    '''

    def decryption(self, sk, c0, c1):
        value = find_modulo_inverse(c0**(sk), self.p)
        M = (c1 * value) % self.p
        return M - 1 if M <= self.q else -M - 1
