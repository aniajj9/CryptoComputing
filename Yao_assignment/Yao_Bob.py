import secrets
from Yao_Party import Yao_Party
import hashlib
import random
from utils import left_indexes, right_indexes


class Yao_Bob(Yao_Party):
    e_value = []  # e_value.append((key0, key1))
    d_value = None
    keys = []  # keys.append((key0, key1))
    Z_value = 0
    garbled_y = []
    y = []

    def __init__(self, y=[0, 1, 0]):
        self.y = y

    def garbling(self, T=11, n=6, leq_gates=9):
        def generate_key_pair():  # TODO: add randomness
            return (random.randint(0, 2 ^ 128), random.randint(0, 2 ^ 128))
            # return (secrets.token_bytes(16), secrets.token_bytes(16))

        def compute_garbled_gate(self, i, a, b, C, leq=False):
            # Concatenate the keys
            key = self.keys[left_indexes[i]][a] + \
                self.keys[right_indexes[i]][b]

            # Calculate hash of the key
            sha256_hash = hashlib.sha256(key.to_bytes(
                (key.bit_length() + 7) // 8, 'big')).digest()

            # Convert hash bytes to integer
            hash_int = int.from_bytes(sha256_hash, byteorder='big')

            # Get the key integer based on the indices and leq flag
            key_int = self.keys[i][a <= b if leq else a * b]

            # Perform the XOR operation on integers and convert the result back to bytes
            result_bytes = (hash_int ^ key_int).to_bytes(
                (hash_int.bit_length() + 7) // 8, byteorder='big')

            # Update the dictionary C with the result bytes
            C[f'{a}{b}'] = result_bytes

        def generate_wire_keys(self, T, n):
            for i in range(1, T+1):
                self.keys.append(generate_key_pair())
                if i <= n:
                    self.e_value.append(self.keys[i])
                elif i == T:
                    self.d_value = self.keys[i]

        def compute_on_wires(self, T, n):
            for i in range(n+1, T+1):
                C = {}
                if i <= leq_gates:  # use leq
                    for a in range(2):
                        for b in range(2):
                            compute_garbled_gate(self, i, a, b, C, leq=True)
                else:
                    for a in range(2):  # use AND
                        for b in range(2):
                            compute_garbled_gate(self, i, a, b, C)
                # TODO: Permutation of C
                self.F_values.append(C)

        self.keys.append((0, 0))  # TODO: REMOVE
        generate_wire_keys(self, T, n)
        compute_on_wires(self, T, n)

        return self.F_values

    def encoding(self, even=True):  # only used for Bob
        encoded_y = []
        j = 0
        for i in range(2 if even else 1, len(self.y)*2 + 1, 2):  # Even indices for Bob
            encoded_y.append(self.keys[i][self.y[j]])
            j += 1
        self.garbled_y = encoded_y
        return encoded_y

    def decode(self, Z):
        if Z == self.d_value[0]:
            return 0
        elif Z == self.d_value[1]:
            return 1
        return Exception(f"Decoding failed. Z: {Z}, d values: {self.d_value}")
