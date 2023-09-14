import random


class Alice:
    def __init__(self, x):
        self.__x = x
        self.dictionary = {}
        self.and_wire_values = {}

    def share(self, bob, function_id):
        self.dictionary[function_id] = random.randint(0, 1)
        bob.set_dictionary(function_id, self.dictionary[function_id] ^ self.__x)

    def open(self):
        pass

    def xor_constant(self, constant, share_id, function_id):
        self.dictionary[function_id] = self.dictionary[share_id] ^ constant

    def xor_wires(self, share_1_id, share_2_id, function_id):
        self.dictionary[function_id] = self.dictionary[share_1_id] ^ self.dictionary[share_2_id]

    def and_constant(self, constant, share_id, function_id):
        self.dictionary[function_id] = self.dictionary[share_id] * constant

    def and_wires(self, share_1_id, share_2_id, bob, function_id):
        self.share_and_wires(share_1_id, share_2_id, bob)
        bob.share_and_wires(share_1_id, share_2_id, self)
        self.compute_e_and_d()

        W_a = self.and_wire_values["W_a"]
        e = self.and_wire_values["e"]
        d = self.and_wire_values["d"]
        x_a = self.and_wire_values["x_a"]
        y_a = self.and_wire_values["y_a"]
        self.dictionary[function_id] = W_a ^ (e * x_a) ^ (d * y_a) ^ (e * d)

    def share_and_wires(self, share_1_id, share_2_id, bob):
        self.and_wire_values["x_a"] = self.dictionary[share_1_id]
        self.and_wire_values["y_a"] = self.dictionary[share_2_id]

        bob.set_and_wire_values("B_d", self.and_wire_values["x_a"] ^ self.and_wire_values["U_a"])
        bob.set_and_wire_values("B_e", self.and_wire_values["y_a"] ^ self.and_wire_values["V_a"])


    def compute_e_and_d(self):
        assert "U_a" in self.and_wire_values and "x_a" in self.and_wire_values
        assert "V_a" in self.and_wire_values and "y_a" in self.and_wire_values
        assert "A_d" in self.and_wire_values and "A_e" in self.and_wire_values
        d = self.and_wire_values["x_a"] ^ self.and_wire_values["U_a"] ^ self.and_wire_values["A_d"]
        e = self.and_wire_values["y_a"] ^ self.and_wire_values["V_a"] ^ self.and_wire_values["A_e"]
        self.and_wire_values["d"] = d
        self.and_wire_values["e"] = e

    def set_and_wire_values(self, key, value):
        self.and_wire_values[key] = value

    def set_dictionary(self, key, value):
        self.dictionary[key] = value


class Bob:
    def __init__(self, x):
        self.__x = x
        self.dictionary = {}
        self.and_wire_values = {}

    def share(self, alice, function_id):
        self.dictionary[function_id] = random.randint(0, 1)
        alice.set_dictionary(function_id, self.dictionary[function_id] ^ self.__x)

    def open(self):
        pass

    def xor_constant(self, share_id, function_id):
        self.dictionary[function_id] = self.dictionary[share_id]

    def xor_wires(self, share_1_id, share_2_id, function_id):
        self.dictionary[function_id] = self.dictionary[share_1_id] ^ self.dictionary[share_2_id]

    def and_constant(self, constant, share_id, function_id):
        self.dictionary[function_id] = self.dictionary[share_id] * constant

    def share_and_wires(self, share_1_id, share_2_id, alice):
        self.and_wire_values["x_b"] = self.dictionary[share_1_id]
        self.and_wire_values["y_b"] = self.dictionary[share_2_id]

        alice.set_and_wire_values("A_d", self.and_wire_values["x_b"] ^ self.and_wire_values["U_b"])
        alice.set_and_wire_values("A_e", self.and_wire_values["y_b"] ^ self.and_wire_values["V_b"])

    def and_wires(self, function_id):
        self.compute_e_and_d()

        W_b = self.and_wire_values["W_b"]
        e = self.and_wire_values["e"]
        d = self.and_wire_values["d"]
        x_b = self.and_wire_values["x_b"]
        y_b = self.and_wire_values["y_b"]
        self.dictionary[function_id] = W_b ^ (e * x_b) ^ (d * y_b)

    def compute_e_and_d(self):
        assert "U_b" in self.and_wire_values and "x_b" in self.and_wire_values
        assert "V_b" in self.and_wire_values and "y_b" in self.and_wire_values
        assert "B_d" in self.and_wire_values and "B_e" in self.and_wire_values
        d = self.and_wire_values["x_b"] ^ self.and_wire_values["U_b"] ^ self.and_wire_values["B_d"]
        e = self.and_wire_values["y_b"] ^ self.and_wire_values["V_b"] ^ self.and_wire_values["B_e"]
        self.and_wire_values["d"] = d
        self.and_wire_values["e"] = e

    def set_and_wire_values(self, key, value):
        self.and_wire_values[key] = value

    def set_dictionary(self, key, value):
        self.dictionary[key] = value




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


'''xa, xb, xr, ya, yb, yr = 0, 0, 0, 0, 0, 0
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

result = part_11'''

dealer = Dealer()

alice = Alice(1)
bob = Bob(0)

alice.share(bob, "alice_share")
bob.share(alice, "bob_share")

dealer.generate_and_wires_randoms(alice, bob)
alice.and_wires("alice_share", "bob_share", bob, "and_wires")
bob.and_wires("and_wires")

print(alice.dictionary["alice_share"])
print(bob.dictionary["alice_share"])

print(alice.dictionary["and_wires"])
print(bob.dictionary["and_wires"])

