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

        print("Alice k values")
        print(self.K_values)
        self.final_results = []
        for i in range(1, 6):
            print("index i")
            print(i)
            C = self.F_values[i-1]
            results = []
            isFound = False
            for C_key, entry in C.items():

                sha256_hash = hashlib.sha256()

                # Update the hash object with the data

                print("error")
                print(i+n)
                print("len keys")
                print(len(self.K_values))
                key = self.K_values[self.left_indexes[i+n]-1] + self.K_values[self.right_indexes[i+n]-1]
                print(len(key))
                print(len(entry))
                print(key)
                sha256_hash.update(key)
                hash_bytes = sha256_hash.digest()


                # Convert bytes to integers
                hash_int = int.from_bytes(hash_bytes, byteorder='big')
                entry_int = int.from_bytes(entry, byteorder='big')

                # Perform the XOR operation on integers
                result_int = hash_int ^ entry_int

                # Convert the result back to bytes
                result = result_int.to_bytes((result_int.bit_length() + 7) // 8, byteorder='big')
                print(len(result))
                print("---ALICE---")
                print(i+n)
                print("zeros key")
                print(result)
                print("L R")
                print(key)
                print("garbled L R")
                print(hash_bytes)
                print("C result")
                print(entry)

                print("result last 16")
                print(result[-16:])
                #result = get_sha256_digest(self.K_values[self.left_indexes[i]][0] + self.K_values[self.right_indexes[i]][1], i) ^ entry
                if result[-16:] == b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00':
                    print("zeros!!!")
                    # TODO: not checking for uniqueness
                    self.K_values.append(result[:16])
                    isFound = True
                    break
            if not isFound:
                raise Exception(f"No solution for {i}'th run")
        return result[:16]
