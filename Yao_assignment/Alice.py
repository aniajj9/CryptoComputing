from utils import get_sha256_digest
from Party import Party


class Alice(Party):
    garbled_x = []
    X_values = []  # need to get it from outside
    Y_values = []  # need to get it from outside
    K_values = []  # store keys used for circuit evaluation, must order keys correctly

    def choose_input(self, input=[0, 1, 0]):
        self.input = input

    def evaluate(self, T=11, n=6):
        for i in range(3):
            self.K_values.append(self.X_values[i])
            self.K_values.append(self.Y_values[i])

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
