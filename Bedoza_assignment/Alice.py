from Party import Party

'''
    Class representing Alice in the protocol
    This class inherits from Party
    It contains the functions that are used by Alice
'''
class Alice(Party):
    def xor_constant(self, constant, share_id, function_id):
        self.received_shares[function_id] = self.received_shares[share_id] ^ constant

    def and_constant(self, constant, share_id, function_id):
        self.received_shares[function_id] = self.received_shares[share_id] * constant

    def and_wires(self, share_1_id, share_2_id, bob, function_id):
        self.share_and_wires(share_1_id, share_2_id, bob)
        bob.share_and_wires(share_1_id, share_2_id, self)
        self.compute_e_and_d()

        W_a = self.and_wire_values["W_a"]
        e = self.and_wire_values["e"]
        d = self.and_wire_values["d"]
        x_a = self.and_wire_values["x_a"]
        y_a = self.and_wire_values["y_a"]
        self.received_shares[function_id] = W_a ^ (e * x_a) ^ (d * y_a) ^ (e * d)

    def share_and_wires(self, share_1_id, share_2_id, bob):
        self.and_wire_values["x_a"] = self.received_shares[share_1_id]
        self.and_wire_values["y_a"] = self.received_shares[share_2_id]

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