import secrets

class Party():
    def __init__(self, bloodtype):
        self.ciphertexts = []
        self.bloodtype = bloodtype
        self.result_ciphertext = None
        self.C = 0
        self.S = []

    def encryption(self, m):
        def random_subset(pk_len):
            subset_size = secrets.randbelow(pk_len - 1 ) + 1
            self.S = secrets.sample(list(range(pk_len)), subset_size)
            return self.S
        
        self.S = random_subset(len(self.pk))
        for i in self.S:
            self.C += self.y_values[i]
        self.C += m
        return self.C

    def receive_ciphertexts(self, ciphertexts):
        self.ciphertexts = ciphertexts