# d-Homomorphic encryption

## Questions



### Security of the subset S

In the encryption function, a subset S is chosen at random from the set of public keys. The size of the subset, *subset_size*, is also chosen at random between 1 and n (the length of the public key). This means that for any given encryption, the subset S is chosen **uniformly from the powerset of the public keys**.
The number of possible subsets of a set of size n is 2^n. This is because for each element in the set, there are two possibilities: it's either in the subset or it's not. So, for n elements, there are 2^n possible subsets. Given that n is around 2000 (as per the provided parameters), the number of possible subsets is astronomically large.
For an adversary to guess the exact subset S used in a particular encryption, they would have to correctly guess the presence or absence of each of the n indices in S. The probability of correctly guessing a single index's presence or absence is 1/2. Therefore, the probability of guessing the entire subset (1/2)^2, which is negligible for large n.