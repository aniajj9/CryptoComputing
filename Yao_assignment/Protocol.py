from Alice import Alice
from Bob import Bob

def protocol(alive_values, bob_values):

    alice = Alice(alive_values)
    bob = Bob(bob_values)

    bob.garbling_boolean_compatibility(alice)
    bob.fake_ot(alice)
    bob.encoding(alice)
    alice.evaluate()
    alice.send_Z_to_Bob(bob)
    result = bob.decode()
    print(result)

protocol([0,1,1], [1,0,1])
protocol([0,0,1], [1,0,1])
