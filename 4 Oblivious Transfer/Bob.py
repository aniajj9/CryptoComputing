from Party import Party
from utils import modular_exponentiation


class Bob(Party):

    # need to call random_number and store random values in a list(?) used for encryption

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

    def receive_pk(self, pk_gen, pk_ogen):
        self.pk_gen = pk_gen
        self.pk_ogen = pk_ogen
