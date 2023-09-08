import random

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

blood_type_to_index = {
    '0-': 0,
    '0+': 1,
    'A-': 2,
    'A+': 3,
    'B-': 4,
    'B+': 5,
    'AB-': 6,
    'AB+': 7
}

def circular_shift_matrix(matrix, r, s):
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    
    shifted_matrix = [[0 for _ in range(num_cols)] for _ in range(num_rows)]
    
    for i in range(num_rows):
        for j in range(num_cols):
            shifted_matrix[(i + r) % num_rows][(j + s) % num_cols] = matrix[i][j]
    
    return shifted_matrix

def generate_random_matrix(n):
    return [[random.choice([True, False]) for _ in range(n)] for _ in range(n)]


class Alice:
    def __init__(self, x):
        self.__r = None
        self.__Ma = None
        self.__x = x
    
    def set_r(self, r):
        self.__r = r
    
    def set_Ma(self, Ma):
        self.__Ma = Ma

class Bob:
    def __init__(self, y):
        self.s = None
        self.Mb = None
        self.y = y
    
    def set_s(self, s):
        self.s = s
    
    def set_Mb(self, Mb):
        self.Mb = Mb

class Dealer:
    def __init__(self):
        self.__r = None
        self.__s = None
        self.__Mb = None
        self.__Ma = None
    
    def pick_random_r(self):
        self.__r = random.randint(0, 8)
    
    def pick_random_s(self):
        self.__s = random.randint(0, 8)
    
    def pick_random_Mb(self):
        self.__Mb = generate_random_matrix(8)
    
    def calculate_ma(self):
        shifted_table = circular_shift_matrix(self.__Mb, self.__r, self.__s)
        self.__Ma = 


    
    


