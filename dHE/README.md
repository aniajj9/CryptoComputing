# d-Homomorphic encryption

## Questions



# Encryption Function and Subset Selection

In the encryption function, a subset $S$ is to be selected at random from the set of indices $N = {1,2, \ldots n}$ of the $y_i$ values in the public key. In our implementation, $S$ is chosen by flipping a coin of equal probability for each element of $N$, and then adding the element to the set $S$ if the value of the coin is 1. Note that this method gives us that no element of N can be added to $S$ twice. This implementation also gives us that S is chosen from the power set of N uniformly.

The expected size of $S$ is $\frac{n}{2}$, since the coins all have probability $\frac{1}{2}$ of being 1. Further, the probability of an adversary correctly guessing a subset $S$ correctly is $\frac{1}{2^{n}}$, which is negligible in n. By our implementation, the probability of having an empty set for $S$ is also $\frac{1}{2^{n}}$, and the probability of having only one element in $S$ is $\frac{n}{2^{n}}$. These are both negligible in $n$, since $2^{n}$ grows exponentially as $n$ increases. It is crucial that $S$ is non-empty such that when encrypting we are not just sending clear text, and it should not be too small such that an adversary can brute-force attack by subtracting parts of the public key from a given ciphertext to reveal the message.|
