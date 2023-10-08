from utils import get_sha256_digest
from Yao_Party import Yao_Party


class Yao_Alice(Yao_Party):
    garbled_x = []
    garbled_y = []
    K_values = []  # store keys used for circuit evaluation, must order keys correctly
    F_values = []  # store garbled gates

    def __init__(self, input=[0, 1, 0]):
        self.input = input

    def evaluate(self, T=11, n=7):
        # To make the keys in correct order
        for i in range(3):
            self.K_values.append(self.garbled_x[i])
            self.K_values.append(self.garbled_y[i])

        result = []
        for i in range(n, T+1):
            C = self.F_values[i]
            for entry in C:
                result = get_sha256_digest(self.K_values[self.left_indexes[i]][0] +
                                           self.K_values[self.right_indexes[i]][1], i) ^ entry
                if result[-128:] == bytes([0] * 128):
                    print("zeros")
                    # TODO: not checking for uniqueness
                    result.append((i, entry))
            if len(result[i]) == 1:
                self.K_values.append(result[i][0])
            else:
                return Exception(f"No solution for {i}'th run")
        return result[-1][0]
