import random
from blood_types import logic_compatibility, blood_types_encoding
from Party import Party
from utils import modular_exponentiation


class Bob(Party):
    r_encryption = []

    def encrypt_blood_types(self, r_encryption=[]):
        encrypted_blood_types = []
        self.initialize_r_encryption(r_encryption)
        for i in range(7):
            pk = self.public_keys[i]
            r = self.r_encryption[i]
            b = blood_types_encoding[i]
            blood_type_table_result = logic_compatibility(
                blood_types_encoding[self.blood_type], b)

            encryption = self.encryption(blood_type_table_result, r, pk)
            encrypted_blood_types.append(encryption)

        self.ciphertexts = encrypted_blood_types

    def send_ciphertexts(self, other_party):
        other_party.receive_ciphertexts(self.ciphertexts)

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

    def receive_public_keys(self, public_keys):
        self.public_keys = public_keys

    def initialize_r_encryption(self, r_encryption=[]):
        if r_encryption != []:
            self.r_encryption = r_encryption
            return

        for i in range(len(blood_types_encoding)):
            self.r_encryption.append(random.randint(1, self.q - 1))
