from Yao_assignment.ObliviousTransfer.OT import run_OT

def run_Yao_OT(alice, bob):
    j = 1
    # Run OT for each of Alice's bits
    for i in range(len(alice.input)):
        alice.X_values.append(
            run_OT(alice.input[i], bob.keys[j], n=8) )
        j += 2


