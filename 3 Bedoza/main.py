from random import random


class Alice:
    def __init__(self):
        self.__Xa = None

    def set_Xa(self, Xa):
        self.__Xa = Xa


class Bob:
    def __init__(self, Xb):
        self.__Xb = None

    def set_Xb(self, Xb):
        self.__Xb = Xb


class Bedoza:
    def __init__(self, X):
        self.__X = X
        self.__Xa = None
        self.__Xb = None

    def create_shares(self):
        X_a = random.randint(0, 1) # TODO: how are shares defined? modulo?
        X_b = self.__X ^ X_a
        self.__Xa = X_a
        self.__Xb = X_b

    def distribute_shares(self, alice, bob):
        assert self.__Xa is not None and self.__Xb is not None
        alice.set_Xa(self.__Xa)
        bob.set_Xb(self.__Xb)


