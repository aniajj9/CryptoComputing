# d-Homomorphic encryption

## Questions



# Encryption Function and Subset Selection

In the encryption function, a subset `S` is to be selected at random from the set of indices `N = {1,2, \ldots n}` of the `y_i` values in the public key. In our implementation, `S` is chosen by flipping a coin of equal probability for each element of `N`, and then adding the element to the set `S` if the value of the coin is 1. Note that this method gives us that no element of N can be added to `S` twice. This implementation also gives us that S is chosen from the power set of N uniformly.

The expected size of `S` is `n/2`, since the coins all have probability `\frac{1}{2}` of being 1. Further, the probability of an adversary correctly guessing a subset `S` correctly is `\frac{1}{2^{n}}`, which is negligible in n. By our implementation, the probability of having an empty set for `S` is also `\frac{1}{2^{n}}`, and the probability of having only one element in `S` is `\frac{n}{2^{n}}`. These are both negligible in `n`, since `2^{n}` grows exponentially as `n` increases. It is crucial that `S` is non-empty such that when encrypting we are not just sending clear text, and it should not be too small such that an adversary can brute-force attack by subtracting parts of the public key from a given ciphertext to reveal the message.



The size of this subset, denoted as `subset_size`, is half of the total length of the public key set. The way the subset `S` is chosen ensures that each key in the subset is unique.

Generally, the number of possible subsets of a set of size `n` is `2^n`. However, when we are specifically interested in subsets of size `k` (where `k` is `n/2`). The number of such subsets is given by the binomial coefficient:

![Subset Formula](https://latex.codecogs.com/png.latex?%5Cbinom%7Bn%7D%7Bk%7D)

Now, to calculate the probability of an adversary correctly guessing the subset `S`, we need to consider that there's only one correct subset among the total number of possible subsets. Hence, the probability `P` of a correct guess is the reciprocal of the total number of possible subsets, which is given by:

![Probability Formula](https://latex.codecogs.com/png.latex?P%28%5Ctext%7Bguessing%20%7D%20S%29%20%3D%20%5Cdfrac%7B1%7D%7B%5Cbinom%7Bn%7D%7Bk%7D%7D)
