import random

# Truth table that the protocol is based on. Public for later check of correctness, but Alice and Bob do not use it (it is secret to them)
blood_type_table_2D = [
    #   0-,  0+,  A-,  A+,  B-,  B+, AB-, AB+
    [True, True, True, True, True, True, True, True],  # 0-
    [False, True, False, True, False, True, False, True],  # 0+
    [False, False, True, True, False, False, True, True],  # A-
    [False, False, False, True, False, False, False, True],  # A+
    [False, False, False, False, True, True, True, True],  # B-
    [False, False, False, False, False, True, False, True],  # B+
    [False, False, False, False, False, False, True, True],  # AB-
    [False, False, False, False, False, False, False, True]  # AB+
]

# Number of bits that the blood is encoded by
n = 3


# Method that shifts matrix by r (columns) and s (rows)
def circular_shift_matrix(matrix, r, s):
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    shifted_matrix = [[0 for _ in range(num_cols)] for _ in range(num_rows)]

    for i in range(num_rows):
        for j in range(num_cols):
            shifted_matrix[(i + r) % num_rows][(j + s) % num_cols] = matrix[i][j]

    return shifted_matrix


# Generate random boolean matrix of dimensions 2**n x 2**n
def generate_random_matrix(n):
    return [[random.choice([True, False]) for _ in range(2 ** n)] for _ in range(2 ** n)]


# XOR of two 2D matrices
def two_dimensions_xor(array1, array2):
    result = []
    for i in range(len(array1)):
        result_row = []
        for j in range(len(array1[i])):
            result_element = array1[i][j] ^ array2[i][j]
            result_row.append(result_element)
        result.append(result_row)
    return result


# Class representing Alice in the protocol
class Alice:
    def __init__(self, x):
        self.__r = None
        self.__Ma = None
        self.__x = x
        self.__V = None
        self.__U = None
        self.__zb = None
        self.__z = None

    def set_r(self, r):
        self.__r = r

    def set_Ma(self, Ma):
        self.__Ma = Ma

    def set_V(self, V):
        self.__V = V

    def compute_U(self):
        assert self.__x is not None and self.__r is not None
        self.__U = (self.__x + self.__r) % (2 ** n)

    def send_U_to_Bob(self, bob):
        bob.set_U(self.__U)

    def set_zb(self, zb):
        self.__zb = zb

    def calculate_z(self):
        self.__z = self.__zb ^ self.__Ma[self.__U][self.__V]

    def get_z(self):
        return self.__z


# Class representing Bob in the protocol
class Bob:
    def __init__(self, y):
        self.__s = None
        self.__Mb = None
        self.__y = y
        self.__V = None
        self.__U = None
        self.__zb = None

    def set_s(self, s):
        self.__s = s

    def set_Mb(self, Mb):
        self.__Mb = Mb

    def set_U(self, U):
        self.__U = U

    def compute_V(self):
        assert self.__y is not None and self.__s is not None
        self.__V = (self.__y + self.__s) % (2 ** n)

    def send_V_to_Alice(self, alice):
        alice.set_V(self.__V)

    def calculate_zb(self):
        assert self.__Mb is not None and self.__U is not None and self.__V is not None
        self.__zb = self.__Mb[self.__U][self.__V]

    def send_zb_to_Alice(self, alice):
        alice.set_zb(self.__zb)


# Class representing Dealer in the protocol
class Dealer:
    def __init__(self, truth_table):
        self.__truth_table = truth_table # Only dealer knows the truth table
        self.__r = None
        self.__s = None
        self.__Mb = None
        self.__Ma = None
        self.__zb = None

    def pick_random_r(self):
        self.__r = random.randint(0, 2 ** n)

    def pick_random_s(self):
        self.__s = random.randint(0, 2 ** n)

    def pick_random_Mb(self):
        self.__Mb = generate_random_matrix(n)

    def calculate_ma(self):
        shifted_table = circular_shift_matrix(self.__truth_table, self.__r, self.__s)
        self.__Ma = two_dimensions_xor(shifted_table, self.__Mb)

    def set_Alice_values(self, alice):
        assert self.__r is not None and self.__Ma is not None
        alice.set_r(self.__r)
        alice.set_Ma(self.__Ma)

    def set_Bob_values(self, bob):
        assert self.__s is not None and self.__Mb is not None
        bob.set_s(self.__s)
        bob.set_Mb(self.__Mb)


def one_time_truth_table_protocol(x, y, truth_table):
    # Initialize parties with their secrets
    dealer = Dealer(truth_table)
    alice = Alice(x)
    bob = Bob(y)

    # Dealer sends values to Alice and Bob
    dealer.pick_random_s()
    dealer.pick_random_r()
    dealer.pick_random_Mb()
    dealer.calculate_ma()
    dealer.set_Alice_values(alice)
    dealer.set_Bob_values(bob)

    # Exchange secrets between Alice and Bob
    alice.compute_U()
    bob.compute_V()
    alice.send_U_to_Bob(bob)
    bob.send_V_to_Alice(alice)
    bob.calculate_zb()
    bob.send_zb_to_Alice(alice)

    # Calculate result
    alice.calculate_z()
    return alice.get_z()


# Function that checks if for two inputs the result of the function is equal to the result of the truth table
def is_function_equal_to_truth_table(function, truth_table):
    for i in range(len(truth_table)):
        for j in range(len(truth_table[i])):
            if function(i, j, truth_table) is not truth_table[i][j]:
                return False
    return True


# Print the one time truth table protocol for all blood combinations
def one_time_truth_table_blood_compatibility(table):
    index_to_blood_type = {
    0: "0-",
    1: "0+",
    2: "A-",
    3: "A+",
    4: "B-",
    5: "B+",
    6: "AB-",
    7: "AB+",
    }
    for i in range(len(table)):
        for j in range(len(table[i])):
            print(
                f"{index_to_blood_type.get(i)} can receive blood from {index_to_blood_type.get(j)}: {one_time_truth_table_protocol(i, j, table)}")


if is_function_equal_to_truth_table(one_time_truth_table_protocol, blood_type_table_2D):
    one_time_truth_table_blood_compatibility(blood_type_table_2D)
