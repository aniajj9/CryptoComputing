import secrets
from Party import Party
import hashlib


class Bob():

    def __init__(self, input_bits):
        self.input = input_bits
        self.F_values = []
        self.e_value = [(0, 0)]  # append with dummy, since in notes we start notation at 1, and in python at 0
        self.d_value = None
        self.keys = [(0, 0)]  # append with dummy, since in notes we start notation at 1, and in python at 0
        self.Z_value = 0
        self.left_indexes = {7: 1, 8: 3, 9: 5, 10: 7, 11: 9}
        # making R(i) for blood type circuit
        self.right_indexes = {7: 2, 8: 4, 9: 6, 10: 8, 11: 10}
        # F_values.append((i, C0, C1, C2, C3))
        self.F_values = []

    # Fake OT (send values straightforward) for debugging
    def fake_ot(self, alice):
        first_keys = self.keys[1]
        third_keys = self.keys[3]
        fifth_keys = self.keys[5]

        alice_input = alice.get_input()
        alice.set_X_values([first_keys[alice_input[0]], third_keys[alice_input[1]], fifth_keys[alice_input[2]]])

    # Compute value for gate
    # i - id of wire
    # a, b- values of bits
    # C - dictionary to hold values
    def compute_garbled_gate(self, i, a, b, C, leq=False):
        sha256_hash = hashlib.sha256()

        # Update the hash object with the data
        key = self.keys[self.left_indexes[i]][a] + self.keys[self.right_indexes[i]][b]
        sha256_hash.update(key)
        hash_bytes = sha256_hash.digest()

        assert len(hash_bytes) == 32

        # Evaluate funtion ("leq" or "and") and add padding
        key_eval = self.keys[i][a <= b if leq else a * b] + b'\x00' * 16

        # Convert bytes to integers
        hash_int = int.from_bytes(hash_bytes, byteorder='big')
        key_int = int.from_bytes(key_eval, byteorder='big')

        # Perform the XOR operation on integers
        result_int = hash_int ^ key_int

        # Convert the result back to bytes
        result_bytes = result_int.to_bytes((result_int.bit_length() + 7) // 8, byteorder='big')

        C[str(a) + str(b)] = result_bytes

    def generate_key_pair(self):
        return secrets.token_bytes(16), secrets.token_bytes(16)

    def garbling_boolean_compatibility(self, alice, T=11, n=6):


        for i in range(1, T + 1):  # Generate keys for each wire
            self.keys.append(self.generate_key_pair())
            if i <= n:  # Input
                self.e_value.append(self.keys[i])
            elif i == T:
                self.d_value = self.keys[i]
        for i in range(n + 1, T + 1):  # Compute on wires
            C = {}  # { 00: ..., 01: ..., 10: ..., 11: ...}
            if i in {7, 8, 9}:  # use leq
                for a in range(2):
                    for b in range(2):
                        self.compute_garbled_gate(i, a, b, C, leq=True)

            else:  # use AND
                for a in range(2):
                    for b in range(2):
                        self.compute_garbled_gate(i, a, b, C, leq=False)

            # TODO: Permutation of C
            self.F_values.append(C)

        alice.set_f_values(self.F_values)

        return self.F_values, self.e_value

    def encoding(self, alice, even=True):  # only used for Bob
        encoded_y = []
        j = 0
        for i in range(2 if even else 1, len(self.input) * 2 + 1, 2):  # Even indices for Bob
            encoded_y.append(self.keys[i][self.input[j]])
            j += 1
        alice.set_Bobs_encoded_y(encoded_y)
        return encoded_y

    def set_Z(self, Z):
        self.Z = Z

    def decode(self):
        if self.Z == self.d_value[0]:
            return 0
        elif self.Z == self.d_value[1]:
            return 1
        else:
            raise Exception("Z value doesnt fit either of d values")
