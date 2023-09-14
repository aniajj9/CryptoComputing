import random


# Class representing Alice
class Alice:
    def __init__(self):
        self.dictionary = {}  # Here Alice stores her shares that she received, where the keys are IDs of the functions that led to the share
        self.and_wire_values = {}  # Here Alice stores values needed for AND WIRE gate

    # Share bit, save it yourself and make bob save it
    def share(self, bit, bob, function_id):
        self.dictionary[function_id] = random.randint(0, 1)
        bob.set_dictionary(function_id, self.dictionary[function_id] ^ bit)

    # XOR with constant
    def xor_constant(self, constant, share_id, function_id):
        self.dictionary[function_id] = self.dictionary[share_id] ^ constant

    # XOR with 2 shares
    def xor_wires(self, share_1_id, share_2_id, function_id):
        self.dictionary[function_id] = self.dictionary[share_1_id] ^ self.dictionary[share_2_id]

    # AND with constant
    def and_constant(self, constant, share_id, function_id):
        self.dictionary[function_id] = self.dictionary[share_id] * constant

    # AND with 2 shares
    def and_wires(self, share_1_id, share_2_id, bob, function_id):
        self.share_and_wires(share_1_id, share_2_id, bob)
        bob.share_and_wires(share_1_id, share_2_id, self)
        self.compute_e_and_d()

        W_a = self.and_wire_values["W_a"]
        e = self.and_wire_values["e"]
        d = self.and_wire_values["d"]
        x_a = self.and_wire_values["x_a"]
        y_a = self.and_wire_values["y_a"]
        self.dictionary[function_id] = W_a ^ (e * x_a) ^ (d * y_a) ^ (e * d) # Z_a

    # Save shares to the dictionary, and send to Bob what he should know
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


# Class representing Bob
class Bob:
    def __init__(self):
        self.dictionary = {}  # Here Bob stores past shares, lookable by function ID
        self.and_wire_values = {}  # Here Bob stores shares needed for AND WIRE gate

    # Share bit, save it to dictionary, make Alice save her share
    def share(self, bit, alice, function_id):
        self.dictionary[function_id] = random.randint(0, 1)
        alice.set_dictionary(function_id, self.dictionary[function_id] ^ bit)

    # XOR constant, but only Alice multiplies by constant
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
    # Initialize parties
    dealer = Dealer()
    alice = Alice()
    bob = Bob()

    # Encode receiver blood into 3 bits, and share those bits
    receiver_encoded = blood_types.get(bloodtype_receiver)
    alice.share(int(receiver_encoded[0]), bob, "xa")
    alice.share(int(receiver_encoded[1]), bob, "xb")
    alice.share(int(receiver_encoded[2]), bob, "xr")

    # Encode donor blood into 3 bits, and share those bits
    donor_encoded = blood_types.get(bloodtype_donor)
    bob.share(int(donor_encoded[0]), alice, "ya")
    bob.share(int(donor_encoded[1]), alice, "yb")
    bob.share(int(donor_encoded[2]), alice, "yr")

    # For code clarity, make one function for Alice's, Bob's, Dealer's actions
    def xor_constant(constant, share_id, function_id):
        alice.xor_constant(constant, share_id, function_id)
        bob.xor_constant(share_id, function_id)

    def and_wires(share_1_id, share_2_id, function_id):
        dealer.generate_and_wires_randoms(alice, bob)
        alice.and_wires(share_1_id, share_2_id, bob, function_id)
        bob.and_wires(function_id)

    # The logic function, divided into parts - each part equals to 1 gate
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
    for blood_receiver in blood_types:
        for blood_donor in blood_types:
            print(
                f"{blood_receiver} can receive blood from {blood_donor}: {blood_compatibility_bedoza(blood_receiver, blood_donor)}")


print_blood_compatibility()
