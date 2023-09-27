
class Party:
    def __init__(self, q, g):
        self.q = q
        self.p = self.q * 2 + 1
        self.g = g
        self.pk_gen = 0
        self.pk_ogen = []  # public keys corresponding to sk
        self.r_encryption = []  # eight random values
