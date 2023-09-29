
class Party:
    blood_type = 0

    def __init__(self, q, g):
        self.q = q
        self.p = self.q * 2 + 1
        self.g = g
        self.public_keys = []
        self.ciphertexts = []
