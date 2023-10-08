### bloodtype_compatibility_test.py is a Python script that verifies if two blood types are compatible.
To run it, no arguments are needed.
It contains two functions that compute compatibility:
 - Truth table based
 - Logic based
The truth table based function is based on a list of tuples of blood that are compatible.
The logic based function performs a series of bit comparisons, and uses OR, NOT and AND logical operations.
The script prints an error message if the result of the two functions deviates for at least one pair.
If the functions are in accordance, all blood type pairs are printed out, alongside the decision if they are compatible (True) or not (False)