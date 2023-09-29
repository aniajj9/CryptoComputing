
import random


class Party:
    def __init__(self, q, g):
        self.q = q
        self.p = self.q * 2 + 1
        self.g = g
        self.public_keys = []
        self.ciphertexts = []
        self.blood_type = -1
    
    def choose_blood_type(self, blood_type=-1):
        if(blood_type != -1):
            self.blood_type = blood_type
        else:
            self.blood_type = random.randint(0, 7)