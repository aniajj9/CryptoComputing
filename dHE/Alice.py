from Party import Party
import secrets

class Alice(Party):
    def __init__(self, bloodtype):
        super.__init__(bloodtype)
        self.key_gen = KeyGenerator()
        self.own_ciphertexts = None

    def generate_keys(self):
        self.p, self.y_values = self.key_gen.generate_keys()    
        return self.p, self.y_values
    
    def decrypt_output(self, c):
        return (c % self.p) % 2

    def send_public_keys(self, other_party):
        other_party.receive_public_keys(self.public_keys)

    def receive_result_ciphertext(self, result_ciphertext):
        self.result_ciphertext = result_ciphertext

    def compute_ciphertexts(self):
        self.own_ciphertexts = [self.encryption(x) for x in self.bloodtype]

    def send_own_ciphertexts(self, other_party):
        other_party.receive_ciphertexts(self.own_ciphertexts)
           

class KeyGenerator:
    p_bits = 2000
    q_bits = 10**7
    r_bits = 60
    n = 2000

    def generate_keys(self):
        '''This function generates secret and public keys for a homomorphic encryption scheme.'''
        p = self.generate_secret_key()
        q_values = self.generate_random_integers(self.q_bits, self.n)
        r_values = self.generate_random_integers(self.r_bits, self.n)
        y_values = self.compute_public_key_values(p, q_values, r_values)
        return p, y_values

    def generate_secret_key(self):
        '''Generate the secret key p (odd integer).'''
        p = secrets.randbelow(2**self.p_bits)
        if p % 2 == 0:
            p += 1
        return p

    def generate_random_integers(self, bit_length, count):
        '''Generate a list of random integers of a given bit length.'''
        return [secrets.randbelow(2**bit_length) for _ in range(count)]

    def compute_public_key_values(self, p, q_values, r_values):
        '''Compute the public key values y1, y2, ..., yn.'''
        return [(p * q_values[i] + 2 * r_values[i]) for i in range(len(q_values))]
