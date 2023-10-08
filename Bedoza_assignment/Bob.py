from Party import Party

''' 
    Class representing Bob in the protocol
    This class inherits from Party
    It contains the functions that are used by Bob
'''
class Bob(Party):
    def xor_constant(self, share_id, function_id):
        self.received_shares[function_id] = self.received_shares[share_id]

    def and_constant(self, constant, share_id, function_id):
        self.received_shares[function_id] = self.received_shares[share_id] * constant

    def share_and_wires(self, share_1_id, share_2_id, alice):
        self.and_wire_values["x_b"] = self.received_shares[share_1_id]
        self.and_wire_values["y_b"] = self.received_shares[share_2_id]

        alice.set_and_wire_values("A_d", self.and_wire_values["x_b"] ^ self.and_wire_values["U_b"])
        alice.set_and_wire_values("A_e", self.and_wire_values["y_b"] ^ self.and_wire_values["V_b"])

    def and_wires(self, function_id):
        self.compute_e_and_d()

        W_b = self.and_wire_values["W_b"]
        e = self.and_wire_values["e"]
        d = self.and_wire_values["d"]
        x_b = self.and_wire_values["x_b"]
        y_b = self.and_wire_values["y_b"]
        self.received_shares[function_id] = W_b ^ (e * x_b) ^ (d * y_b)

    def compute_e_and_d(self):
        assert "U_b" in self.and_wire_values and "x_b" in self.and_wire_values
        assert "V_b" in self.and_wire_values and "y_b" in self.and_wire_values
        assert "B_d" in self.and_wire_values and "B_e" in self.and_wire_values
        d = self.and_wire_values["x_b"] ^ self.and_wire_values["U_b"] ^ self.and_wire_values["B_d"]
        e = self.and_wire_values["y_b"] ^ self.and_wire_values["V_b"] ^ self.and_wire_values["B_e"]
        self.and_wire_values["d"] = d
        self.and_wire_values["e"] = e

