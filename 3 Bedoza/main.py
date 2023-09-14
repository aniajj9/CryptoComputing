import random


class Alice:
    def __init__(self):
        self.dictionary = {}
        self.and_wire_values = {}

    def share(self, bit, bob, function_id):
        self.dictionary[function_id] = random.randint(0, 1)
        bob.set_dictionary(function_id, self.dictionary[function_id] ^ bit)

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
    def __init__(self):
        self.dictionary = {}
        self.and_wire_values = {}

    def share(self, bit, alice, function_id):
        self.dictionary[function_id] = random.randint(0, 1)
        alice.set_dictionary(function_id, self.dictionary[function_id] ^ bit)

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

blood_types = {
    '0-': "000",
    '0+': "001",
    'A-': "100",
    'A+': "101",
    'B-': "010",
    'B+': "011",
    'AB-': "110",
    'AB+': "111"
}


def blood_compatibility_bedoza(bloodtype_receiver, bloodtype_donor):
    dealer = Dealer()
    alice = Alice()
    bob = Bob()

    receiver_encoded = blood_types.get(bloodtype_receiver)
    alice.share(int(receiver_encoded[0]), bob, "xa")
    alice.share(int(receiver_encoded[1]), bob, "xb")
    alice.share(int(receiver_encoded[2]), bob, "xr")

    donor_encoded = blood_types.get(bloodtype_donor)
    bob.share(int(donor_encoded[0]), alice, "ya")
    bob.share(int(donor_encoded[1]), alice, "yb")
    bob.share(int(donor_encoded[2]), alice, "yr")

    def xor_constant(constant, share_id, function_id):
        alice.xor_constant(constant, share_id, function_id)
        bob.xor_constant(share_id, function_id)

    def and_wires(share_1_id, share_2_id, function_id):
        dealer.generate_and_wires_randoms(alice, bob)
        alice.and_wires(share_1_id, share_2_id, bob, function_id)
        bob.and_wires(function_id)

    xor_constant(1, "xa", "part1")
    and_wires("part1", "ya", "part2")
    xor_constant(1, "part2", "part3")
    xor_constant(1, "xb", "part4")
    and_wires("part4", "yb", "part5")
    xor_constant(1, "part5", "part6")
    and_wires("part3", "part6", "part7")
    xor_constant(1, "xr", "part8")
    and_wires("part8", "yr", "part9")
    xor_constant(1, "part9", "part10")
    and_wires("part7", "part10", "part11")

    return bool(alice.dictionary["part11"] ^ bob.dictionary["part11"])


# Print blood compatibility for all blood types
def print_blood_compatibility():
    # If both functions return the same, display the results
    for blood_receiver in blood_types:
        for blood_donor in blood_types:
            print(
                f"{blood_receiver} can receive blood from {blood_donor}: {blood_compatibility_bedoza(blood_receiver, blood_donor)}")


print_blood_compatibility()

