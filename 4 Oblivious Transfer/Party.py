
import random


class Party:
    def __init__(self, q, g):
        self.q = q
        self.p = self.q * 2 + 1
        self.g = g
        self.public_keys = []
        self.ciphertexts = []
        self.chosen_input = -1

    def choose(self, chosen_input=-1, posssibilities=8):
        if (chosen_input != -1):
            self.chosen_input = chosen_input
        else:
            self.chosen_input = random.randint(0, posssibilities - 1)
