import secrets
from utils import get_sha256_digest
from Party import Party
import hashlib
import random


class Bob(Party):
    e_value = [(0,0)]  # e_value.append((key0, key1))
    d_value = None
    keys = []  # keys.append((key0, key1))
    Z_value = 0

    def fake_ot(self, alice):
        first_keys = self.keys[1]
        third_keys = self.keys[3]
        fifth_keys = self.keys[5]

        alice_input = alice.get_input()

        alice.set_Bobs_keys([first_keys[alice_input[0]], third_keys[alice_input[1]], fifth_keys[alice_input[2]]])


    def garbling_boolean_compatibility(self, alice, T=11, n=6, leq_gates=9):
        def generate_key_pair():  # TODO: add randomness
            return (secrets.token_bytes(16), secrets.token_bytes(16))
            # Set a fixed seed (change the value to your desired seed)
            #seed_value = 42
            #random.seed(seed_value)

            # Generate random bytes
            #return bytes([random.randint(0, 255) for _ in range(16)]), bytes([random.randint(0, 255) for _ in range(16)])


        def compute_garbled_gate(i, a, b, C, leq=False):
            sha256_hash = hashlib.sha256()

            # Update the hash object with the data
            key = self.keys[self.left_indexes[i]][a] + self.keys[self.right_indexes[i]][b]
            sha256_hash.update(key)
            hash_bytes = sha256_hash.digest()

            assert len(hash_bytes) == 32



            key_eval = self.keys[i][a <= b if leq else a * b] + b'\x00' * 16


            # Convert bytes to integers
            hash_int = int.from_bytes(hash_bytes, byteorder='big')
            key_int = int.from_bytes(key_eval, byteorder='big')

            # Perform the XOR operation on integers
            result_int = hash_int ^ key_int

            # Convert the result back to bytes
            result_bytes = result_int.to_bytes((result_int.bit_length() + 7) // 8, byteorder='big')

            C[str(a) + str(b)] = result_bytes

            print("---BOB---")
            print(i)
            print("zeros key")
            print(key_eval)
            print("L R")
            print(key)
            print("garbled L R")
            print(hash_bytes)
            print(f"C {a}, {b}")
            print(result_bytes)


        self.keys.append((0, 0))  # TODO: REMOVE
        for i in range(1, T+1):  # Generate keys for each wire
            self.keys.append(generate_key_pair())
            if i <= n:  # Input
                self.e_value.append(self.keys[i])
            elif i == T:
                self.d_value = self.keys[i]
        for i in range(n + 1, T + 1):  # Compute on wires
            C = {}  # { 00: ..., 01: ..., 10: ..., 11: ...}
            if i in {7, 8, 9}:  # use leq
                for a in range(2):
                    for b in range(2):
                        compute_garbled_gate(i, a, b, C, leq=True)

            else:  # use AND
                for a in range(2):
                    for b in range(2):
                        compute_garbled_gate(i, a, b, C, leq = False)

            # TODO: Permutation of C
            self.F_values.append(C)

        alice.set_f_values(self.F_values)

        print("Bob keys")
        print(self.keys)
        return (self.F_values, self.e_value)

    def encoding(self, alice, y=[0,0,1], even=True):  # only used for Bob
        encoded_y = []
        j = 0
        for i in range(2 if even else 1, len(y)*2+1, 2):  # Even indices for Bob
            encoded_y.append(self.keys[i][y[j]])
            j+=1
        alice.set_Bobs_encoded_y(encoded_y)
        return encoded_y

    def decode(self, Z):
        if Z == self.d_value[0]:
            return 0
        elif Z == self.d_value[1]:
            return 1
        return Exception(f"Decoding failed. Z: {Z}, d values: {self.d_value}")

    def set_Z(self, Z):
        self.Z = Z

    def decode(self):
        if self.Z == self.d_value[0]:
            return 0
        elif self.Z == self.d_value[1]:
            return 1
        else:
            raise Exception("Z value doesnt fit either of d values")

