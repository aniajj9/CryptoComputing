import secrets

class KeyGenerator:
    p_bits = 2000 #100
    q_bits = 10**7 #100
    r_bits = 60 #5
    n = 2000 #200
    p = None
    y_values = None

    def __init__(self):
        self.generate_keys()
    
    def generate_keys(self):
        '''This function generates secret and public keys for a homomorphic encryption scheme.'''
        p = self.generate_secret_key()
        q_values = self.generate_random_integers(self.q_bits, self.n)
        r_values = self.generate_random_integers(self.r_bits, self.n)
        y_values = self.compute_public_key_values(p, q_values, r_values)
        self.p = p
        self.y_values = y_values
    
    def get_pk(self):
        return self.y_values
    
    def get_p(self):
        return self.p
    
    def generate_secret_key(self):
        '''Generate the secret key p (odd integer).'''
        p = secrets.randbelow(2**self.p_bits)
        p |= 1  # Set the least significant bit to ensure the number is odd
        return p

    def generate_random_integers(self, bit_length, count):
        '''Generate a list of random integers of a given bit length.'''
        return [secrets.randbelow(2**bit_length) for _ in range(count)]

    def compute_public_key_values(self, p, q_values, r_values):
        '''Compute the public key values y1, y2, ..., yn.'''
        return [(p * q_values[i] + 2 * r_values[i]) for i in range(len(q_values))]