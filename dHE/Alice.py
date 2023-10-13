from Party import Party
from KeyGenerator import KeyGenerator

class Alice(Party):
    def __init__(self, bloodtype, key_gen=None):
        super().__init__(bloodtype)

        self.key_gen = key_gen or KeyGenerator()
        self.p = self.key_gen.get_p()
        self.pk = self.key_gen.get_pk() 

    def get_keys(self): 
        return self.p, self.pk
    
    def decrypt(self, ciphertext):
        return (ciphertext % self.p) % 2

    def send_public_keys(self, other_party):
        other_party.receive_public_keys(self.pk)

    def receive_encrypted_result(self, encrypted_result):
        self.encrypted_result = encrypted_result

    def compute_ciphertexts(self):
        self.alice_encrypted_blood_type = [self.encrypt(x) for x in self.bloodtype]
        return self.alice_encrypted_blood_type

    def send_alice_encrypted_blood_type(self, other_party):
        other_party.receive_alice_encrypted_blood_type(self.alice_encrypted_blood_type)
    
           
