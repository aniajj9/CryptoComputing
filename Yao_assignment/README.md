## YAO GARBLED CIRCUIT

The presented project implements Garbled Circuit for computing blood compatibility function.

Project structure:
- **Test.py** - function, that if run without paramethers, returns output of Garbled Blood Compatibility Circuit for all bloodtype combinations
- Alice.py, Bob.py - protocol parties, where Bob is blood receiver, and Alice donor. Bob wants to know if he can receive Alice's blood
- blood_types.py, utils.py - helper functions
- ObliviousTransfer folder - folder containing classes for Oblivious Transfer.

To run the code:
- Run **Test.py** without arguments

Note:
We have attempted at modifying Oblivious transfer for the previous assignment to fit this task. However, at the current state of the project, oblivious transfer is not implemented in the Garbled Circuit.