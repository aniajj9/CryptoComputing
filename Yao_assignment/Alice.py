from utils import get_sha256_digest
from Party import Party
import hashlib


class Alice:

    def __init__(self, input_bits):
        self.final_results = None
        self.input = input_bits
        self.F_values = []
        self.garbled_x = []
        self.X_values = []
        self.Y_values = []
        self.K_values = []
        self.left_indexes = {7: 1, 8: 3, 9: 5, 10: 7, 11: 9}
        # making R(i) for blood type circuit
        self.right_indexes = {7: 2, 8: 4, 9: 6, 10: 8, 11: 10}
        # F_values.append((i, C0, C1, C2, C3))
        self.F_values = []

    def set_X_values(self, keys):
        self.X_values = keys

    def set_f_values(self, f_values):
        self.F_values = f_values

    def set_Bobs_encoded_y(self, y):
        self.Y_values = y

    def get_input(self):
        return self.input

    def evaluate(self, n=6):
        # Set input values keys: xa ya xb yb xr yr
        global results, result
        for i in range(3):
            self.K_values.append(self.X_values[i])
            self.K_values.append(self.Y_values[i])
        self.final_results = []
        for i in range(1, 6):  # Number of inner wires
            C = self.F_values[i - 1]  # shift since i starts at 1
            results = []
            for C_key, entry in C.items():
                sha256_hash = hashlib.sha256()
                key = self.K_values[self.left_indexes[i + n] - 1] + self.K_values[self.right_indexes[i + n] - 1]
                sha256_hash.update(key)
                hash_bytes = sha256_hash.digest()
                # Convert bytes to integers
                hash_int = int.from_bytes(hash_bytes, byteorder='big')
                entry_int = int.from_bytes(entry, byteorder='big')
                # Perform the XOR operation on integers
                result_int = hash_int ^ entry_int
                # Convert the result back to bytes
                result = result_int.to_bytes((result_int.bit_length() + 7) // 8, byteorder='big')
                # Check if result ends in 0s:
                if result[-16:] == b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00':
                    #print("zeros!!!")
                    results.append(result[:16])
            # Check for uniqueness
            if len(results) == 1:
                self.K_values.append(results[0])
                #print(f"Unique solution FOUND for {i}'th run :) :) :)")
            elif len(results) == 0:
                raise Exception(f"No solution for {i}'th run")
            else:
                raise Exception(f"Duplicated solution for {i}'th run")
        self.Z = results[-1]
        return result[:16]

    def send_Z_to_Bob(self, bob):
        bob.set_Z(self.Z)
