import random


'''
    Class representing the Dealer in the protocol
    The dealer is responsible for generating random values for the AND gates
'''
class Dealer:
    def generate_and_wires_randoms(self, alice, bob):
        U = random.randint(0, 1)
        V = random.randint(0, 1)
        W = U * V

        U_a = random.randint(0, 1)
        V_a = random.randint(0, 1)
        W_a = random.randint(0, 1)

        U_b = U ^ U_a
        V_b = V ^ V_a
        W_b = W ^ W_a

        alice.set_and_wire_values("U_a", U_a)
        alice.set_and_wire_values("V_a", V_a)
        alice.set_and_wire_values("W_a", W_a)

        bob.set_and_wire_values("U_b", U_b)
        bob.set_and_wire_values("V_b", V_b)
        bob.set_and_wire_values("W_b", W_b)
