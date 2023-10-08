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
We had problems connected Yao's protocol to the OT, since we were struggling with changing bytes to integers and the other way around. 
The OT works when the keys are integers, but the Yao protocol works when the keys are bytes. 
We also had to add a dummy for index 0 in the different lists, such that it matches the notes we made for the implementation of the protocol.
We started indexing the wires with 1 in the notes, and wanted to do the same in the implementation.