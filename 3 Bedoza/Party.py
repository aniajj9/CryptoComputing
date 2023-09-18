import random


''' Class representing a party in the protocol
    This class is used as a base class for Alice and Bob
    It contains the basic functions that are used by both parties
'''
class Party:
    def __init__(self):
        self.received_shares = {}
        self.and_wire_values = {} 
    
    def share(self, bit, other_party, function_id):
        ''' Share bit, save it yourself and make other_party save it '''
        self.received_shares[function_id] = random.randint(0, 1)
        other_party.set_received_shares(function_id, self.received_shares[function_id] ^ bit) 
    
    def xor_wires(self, share_1_id, share_2_id, function_id):
        self.received_shares[function_id] = self.received_shares[share_1_id] ^ self.received_shares[share_2_id]
    
    def set_and_wire_values(self, key, value):
        self.and_wire_values[key] = value

    def set_received_shares(self, key, value):
        self.received_shares[key] = value
