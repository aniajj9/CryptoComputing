import sys
sys.path.append('../')
from CryptoComputing.OT_assignment.OT import run_OT

def run_Yao_OT(alice, bob):
    j = 1
    # Run OT for each of Alice's bits
    for i in range(len(alice.input)):
        alice.garbled_x.append(
            run_OT(alice.input[i], bob.keys[j]))
        j += 2