import secrets
from utils import get_sha256_digest
from Party import Party


class Bob(Party):
    # making L(i) for blood type circuit
    left_indexes = {7: 1, 8: 3, 9: 5, 10: 7, 11: 9}
    # making R(i) for blood type circuit
    right_indexes = {7: 2, 8: 4, 9: 6, 10: 8, 11: 10}
    e_value = []  # e_value.append((key0, key1))
    d_value = []
    keys = []  # keys.append((key0, key1))
    F_values = []  # F_values.append((i, C0, C1, C2, C3))

    def generate_key_pair(self):
        return (secrets.token_bytes(16), secrets.token_bytes(16))

    def garbling_boolean_compatibility(self, T=11, n=6, leq_gates=9):
        def compute_garbled_gate(i, a, b, C, leq=False):
            C[str(a) + str(b)] = get_sha256_digest(self.keys[self.left_indexes[i]][a] +
                                                   self.keys[self.right_indexes[i]][b]) ^ (self.keys[i][a <= b if leq else a * b] + b'\x00' * 128)

        self.keys.append((0, 0))  # TODO: REMOVE
        for i in range(1, T+1):  # Generate keys for each wire
            self.keys.append(self.generate_key_pair())
            if i <= n:  # Input
                self.e_value.append(self.keys[i])
            elif i == T:
                self.d_value.append(self.keys[i])
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

        return (self.F_values, self.e_value, self.d_value)

    def encoding(self, y, even=True): #only used for Bob
        encoded_y = []
        for i in range(0 if even else 1, len(y), 2): # Even indices for Bob
            encoded_y.append(self.keys[i][y[i]])
        return encoded_y
        
    def decode(self):
        pass

    # ??? is it good?
    def evaluate(self, T=11, n=6):
        result = []
        for i in range(n, T+1):
            C = self.F_values[i] # TODO: Handle permutation?
            for entry in C:
                result = get_sha256_digest(self.keys[self.left_indexes[i]][0] +
                                                   self.keys[self.right_indexes[i]][1]) ^ entry
                if result[-128:] ==  bytes([0] * 128):
                    result.append((i, entry)) # TODO: not checking for uniqueness
                    break
                return Exception(f"No solution for {i}'th run")
        return result


