from Party import Party
from utils import find_modulo_inverse

class Alice(Party):
    ciphertexts = []

    '''sk: secret key used to create corresponding pk,
    q: prime such that 2q + 1 is also prime,
    g: generator in Zp of order q'''
    def key_generation(self, sk, q, g):
        p = 2 * q + 1
        pk = (g**(sk)) % p
        return pk

    '''r: randomness,
    q: prime such that 2q + 1 is also prime,
    g: generator in Zp of order q'''
    def oblivious_key_generation(self, r, q, g):
        p = 2 * q + 1
        h = pow(r, 2, p)
        return (g, h)

    '''sk: secret key,
    c0: first part of ciphertext,
    c1: second part of ciphertext,
    q: prime such that 2q+1 is also prime
    Used third method from notes
    '''
    def decryption(self, sk, c0, c1, q):
        p = 2 * q + 1
        value = find_modulo_inverse(c0**(sk), p)
        M = (c1* value)%p
        if M <= q:
            return M - 1
        else:
            return -M - 1
    
    def receive_ciphertext(self, ciphertext):
        self.ciphertexts.append(ciphertext)