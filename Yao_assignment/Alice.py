from utils import get_sha256_digest
from Party import Party
import hashlib

class Alice(Party):
    garbled_x = []
    X_values = []  # need to get it from outside
    Y_values = []  # need to get it from outside
    K_values = []  # store keys used for circuit evaluation, must order keys correctly

    def __init__(self, input=[0, 1, 0]):
        self.bobs_keys = None
        self.input = input

    def set_Bobs_keys(self, keys):
        self.X_values = keys

    def set_f_values(self, f_values):
        self.F_values = f_values

    def set_Bobs_encoded_y(self, y):
        self.Y_values = y

    def get_input(self):
        return self.input

    def evaluate(self, T=11, n=6):
        for i in range(3):
            self.K_values.append(self.X_values[i])
            self.K_values.append(self.Y_values[i])


        for i in range(0, T+1-n):
            print(i)
            C = self.F_values[i]
            results = []
            for entry in C:

                sha256_hash = hashlib.sha256()

                # Update the hash object with the data
                print(i+n)
                key = self.K_values[self.left_indexes[i+n+1]] + self.K_values[self.right_indexes[i+n+1]]
                sha256_hash.update(key)
                hash_bytes = sha256_hash.digest()

                # Convert bytes to integers
                hash_int = int.from_bytes(hash_bytes, byteorder='big')
                entry_int = int(entry)

                # Perform the XOR operation on integers
                result_int = hash_int ^ entry_int

                # Convert the result back to bytes
                result = result_int.to_bytes((result_int.bit_length() + 7) // 8, byteorder='big')
                print("---result---")
                print(result)
                #result = get_sha256_digest(self.K_values[self.left_indexes[i]][0] + self.K_values[self.right_indexes[i]][1], i) ^ entry
                if result[-128:] == bytes([0] * 128):
                    print("zeros")
                    # TODO: not checking for uniqueness
                    results.append((i, entry))
            print(len(results))
            if len(results) == 1:
                self.K_values.append(results[0])
            else:
                raise Exception(f"No solution for {i}'th run")
        return results[-1][0]
