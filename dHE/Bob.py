from Party import Party
from functools import reduce

class Bob(Party):

    def compute_compatibility(self):
        one_encryption = self.encrypt(1)
        c_values = []
        for i in range(3):
            c_value = (one_encryption + ((one_encryption + self.alice_encrypted_blood_type[i]) * self.encrypt(self.bloodtype[i])))
            #c_value = (one_encryption + ((one_encryption + self.encrypt(self.bloodtype[i])) * self.alice_encrypted_blood_type[i] ))
            c_values.append(c_value)
        self.encrypted_result = reduce(lambda x, y: x*y, c_values) # Multiply all elements of a list with eachother
    
    def send_encrypted_result(self, other_party):
        other_party.receive_encrypted_result(self.encrypted_result)
        
    def receive_public_keys(self, pk):
        self.pk = pk
    
    def receive_alice_encrypted_blood_type(self, alice_encrypted_blood_type):
        self.alice_encrypted_blood_type = alice_encrypted_blood_type