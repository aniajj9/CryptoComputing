class Party:
    def __init__(self):
        # making L(i) for blood type circuit
        self.left_indexes = {7: 1, 8: 3, 9: 5, 10: 7, 11: 9}
        # making R(i) for blood type circuit
        self.right_indexes = {7: 2, 8: 4, 9: 6, 10: 8, 11: 10}
        # F_values.append((i, C0, C1, C2, C3))
        self.F_values = []
