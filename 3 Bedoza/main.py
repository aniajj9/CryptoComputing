import random


class Alice:
    def __init__(self, x):
        self.__x = x
        self.dictionary = {}
        self.and_wire_values = {}

    def share(self, bit, bob):
        # TODO correct this
        random_bit = random.randint(0, 1)
        self.__xa = random_bit
        # TODO: add share to dict
        bob.set_xb(random_bit ^ bit)

    def open(self):
        pass

    def xor_constant(self, constant, share_id, function_id):
        self.dictionary[function_id] = self.dictionary[share_id] ^ constant

    def xor_wires(self, share_1_id, share_2_id, function_id):
        self.dictionary[function_id] = self.dictionary[share_1_id] ^ self.dictionary[share_2_id]

    def and_constant(self, constant, share_id, function_id):
        self.dictionary[function_id] = self.dictionary[share_id] * constant

    def share_and_wires(self, share_1_id, share_2_id, function_id, dealer, bob):
        U_a, V_a = dealer.generate_and_wires_randoms()
        self.set_and_wire_values("U_a", U_a)
        self.set_and_wire_values("V_a", V_a)
        bob.set_and_wire_values("d", self.dictionary[share_1_id] ^ U_a)
        bob.set_and_wire_values("e", self.dictionary[share_2_id] ^ V_a)

    def and_wires(self):

    def set_and_wire_values(self, key, value):
        self.and_wire_values[key] = value


class Bob:
    def __init__(self):
        self.dictionary = {}
        self.and_wire_values = {}

    def share(self):
        pass

    def open(self):
        pass

    def xor_constant(self, share_id, function_id):
        self.dictionary[function_id] = self.dictionary[share_id]

    def xor_wires(self, share_1_id, share_2_id, function_id):
        self.dictionary[function_id] = self.dictionary[share_1_id] ^ self.dictionary[share_2_id]

    def and_constant(self, constant, share_id, function_id):
        self.dictionary[function_id] = self.dictionary[share_id] * constant

    def share_and_wires(self, share_1_id, share_2_id, alice):
        alice.set_and_wire_values("d", self.dictionary[share_1_id] ^ self.and_wire_values["U_b"])
        alice.set_and_wire_values("e", self.dictionary[share_2_id] ^ self.and_wire_values["V_b"])

    def set_and_wire_values(self, key, value):
        self.and_wire_values[key] = value


class Dealer:
    def __init__(self):
        pass

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


xa, xb, xr, ya, yb, yr = 0, 0, 0, 0, 0, 0
dealer = Dealer(1)
part_1 = dealer.xor_constant(1, xa)
part_2 = dealer.and_wires(part_1, ya)
part_3 = dealer.xor_constant(1, part_2)
part_4 = dealer.xor_constant(1, xb)
part_5 = dealer.and_wires(part_4, yb)
part_6 = dealer.xor_constant(1, part_5)
part_7 = dealer.and_wires(part_3, part_6)
part_8 = dealer.xor_constant(1, xr)
part_9 = dealer.and_wires(part_8, yr)
part_10 = dealer.xor_constant(1, part_9)
part_11 = dealer.and_wires(part_7, part_10)

result = part_11

