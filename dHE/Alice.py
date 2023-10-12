from Party import Party
from KeyGenerator import KeyGenerator

class Alice(Party):
    def __init__(self, bloodtype, key_gen=None):
        super().__init__(bloodtype)

        if(key_gen):
            self.key_gen = key_gen
        else:
            self.key_gen = KeyGenerator()

        self.own_ciphertexts = None

    def generate_keys(self):
        self.p = self.key_gen.get_p()
        self.pk = self.key_gen.get_pk()  
        return self.p, self.pk
    
    def decrypt_output(self, c):
        return (c % self.p) % 2

    def send_public_keys(self, other_party):
        other_party.receive_public_keys(self.pk)

    def receive_result_ciphertext(self, result_ciphertext):
        self.result_ciphertext = result_ciphertext

    def compute_ciphertexts(self):
        self.own_ciphertexts = [self.encryption(x) for x in self.bloodtype]

    def send_own_ciphertexts(self, other_party):
        other_party.receive_ciphertexts(self.own_ciphertexts)
           
