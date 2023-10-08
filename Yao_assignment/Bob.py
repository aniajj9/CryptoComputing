import secrets
from utils import get_sha256_digest
from Party import Party


class Bob(Party):
    e_value = []  # e_value.append((key0, key1))
    d_value = None
    keys = []  # keys.append((key0, key1))
    Z_value = 0

    def garbling_boolean_compatibility(self, T=11, n=6, leq_gates=9):
        def generate_key_pair():  # TODO: add randomness
            return (secrets.token_bytes(16), secrets.token_bytes(16))

        def compute_garbled_gate(i, a, b, C, leq=False):
            C[str(a) + str(b)] = get_sha256_digest(self.keys[self.left_indexes[i]][a] +
                                                   self.keys[self.right_indexes[i]][b], i) ^ (self.keys[i][a <= b if leq else a * b] + b'\x00' * 128)

        self.keys.append((0, 0))  # TODO: REMOVE
        for i in range(1, T+1):  # Generate keys for each wire
            self.keys.append(generate_key_pair())
            if i <= n:  # Input
                self.e_value.append(self.keys[i])
            elif i == T:
                self.d_value = self.keys[i]
        for i in range(n + 1, T + 1):  # Compute on wires
            C = {}  # { 00: ..., 01: ..., 10: ..., 11: ...}
            if i <= leq_gates:  # use leq
                for a in range(2):
                    for b in range(2):
                        compute_garbled_gate(i, a, b, C, leq=True)

            else:  # use AND
                for a in range(2):
                    for b in range(2):
                        compute_garbled_gate(i, a, b, C)

            # TODO: Permutation of C
            self.F_values.append(C)

        return (self.F_values, self.e_value)

    def encoding(self, y, even=True):  # only used for Bob
        encoded_y = []
        for i in range(0 if even else 1, len(y), 2):  # Even indices for Bob
            encoded_y.append(self.keys[i][y[i]])
        return encoded_y

    def decode(self, Z):
        if Z == self.d_value[0]:
            return 0
        elif Z == self.d_value[1]:
            return 1
        return Exception(f"Decoding failed. Z: {Z}, d values: {self.d_value}")
