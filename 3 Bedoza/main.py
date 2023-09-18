from Alice import Alice
from Bob import Bob
from Dealer import Dealer

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

    return bool(alice.received_shares["part11"] ^ bob.received_shares["part11"])


# Print blood compatibility for all blood types
def print_blood_compatibility():
    for blood_receiver in blood_types:
        for blood_donor in blood_types:
            print(
                f"{blood_receiver} can receive blood from {blood_donor}: {blood_compatibility_bedoza(blood_receiver, blood_donor)}")
            

print_blood_compatibility()