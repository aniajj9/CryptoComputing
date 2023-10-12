from Party import Party
from functools import reduce

class Bob(Party):

    def compute_function(self):
        c1 = self.encryption(1)
        c_values = []
        for i in range(3):
            c_values.append((c1 + ((c1 + self.ciphertexts[i]) * self.encryption(self.bloodtype[i]))))
        self.result_ciphertext = reduce(lambda x, y: x*y, c_values) # Multiply all elements of a list with eachother
    
    def send_result_ciphertext(self, other_party):
        other_party.receive_result_ciphertext(self.result_ciphertext)

    def receive_ciphertexts(self, ciphertexts):
        self.ciphertexts = ciphertexts
        
    def receive_public_keys(self, pk):
        self.pk = pk

                