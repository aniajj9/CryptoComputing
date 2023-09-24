from Party import Party

class Bob(Party):

    #need to call random_number and store random values in a list(?) used for encryption

    '''m: input message that is the be encryption,
    r: randomness used for encryption,
    g: group generator,
    pk: public key,
    q: prime such that p = 2q+1 is also prime
    Used third method from notes'''
    def encryption(self, m, r, g, pk, q):
        p = 2 * q + 1
        if ((m+1)**q)%p == 1:
            M = m + 1
        else:
            M = -(m+1)
        c0 = self.square_and_multiply(g, r, p)
        c1 = self.square_and_multiply(pk, r, p) * M
        return c0, c1

    def send_ciphertext(self, other_party, ciphertext):
        return