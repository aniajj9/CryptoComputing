import math
import random
import hashlib

'''
encoding of blood types:
0: O-
1: O+
2: A-
3: A+
4: B-
5: B+
6: AB-
7: AB+
'''

blood_types_encoding = [0b000, 0b001, 0b100, 0b101, 0b010, 0b011, 0b110, 0b111]


'''
blood_type_receiver: blood type of the receiver
blood_type_donor: blood type of the donor
computes the logic compatibility between the two blood types
'''


def logic_compatibility(blood_type_receiver, blood_type_donor) -> bool:

    # Sub-function that checks if two binary numbers are compatible at a bit specified by a bit position
    # Returns true if:
    #   - The two bits are the same
    #   or
    #   - The bit in the first number is 0
    def are_bits_compatible(number1, number2, bit_position) -> bool:
        bit1 = (number1 >> bit_position) & 1
        bit2 = (number2 >> bit_position) & 1
        return bit1 == bit2 or not (number1 & (1 << bit_position))

    return all(
        are_bits_compatible(blood_type_receiver, blood_type_donor, bit_position) for bit_position in
        range(3))


def get_sha256_digest(message):
    return hashlib.sha256(message).digest()


'''n: number we want to check if is prime'''


def is_prime(n):
    result = True
    if n <= 1:
        result = False
    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if n % i == 0:
            result = False
    return result


'''n: number we want to check if is safe prime i.e if 2n + 1 is also prime'''


def is_safe_prime(n):
    return is_prime(n) and is_prime(2 * n + 1)


'''q: prime such that 2q + 1 is also prime'''


def generate_generator(q):
    p = 2 * q + 1
    x = random.randint(2, p - 1)
    if is_safe_prime(q):
        return (x ** 2) % p


'''
input: a, p
Want x and y such that ax + py = gcd(a,p)
output: x, y
'''


def extended_euclidian_algorithm(a, p):
    if a == 0:
        x = 0
        y = 0
        return
    x_0 = 0
    x_1 = 1

    y_0 = 1
    y_1 = 0
    while (a != 0):
        r = p % a
        q = p // a  # finds the coefficient such that p = a*q + r
        if r == 0:
            break
        p = a
        a = r

        x = x_0 - x_1 * q
        x_0 = x_1
        x_1 = x

        y = y_0 - y_1 * q
        y_0 = y_1
        y_1 = y
    return x, y


'''finds inverse of a mod p'''


def find_modulo_inverse(a, p):
    x, y = extended_euclidian_algorithm(a, p)
    inverse = x % p
    return inverse


'''start: lowest value allowed for result,
stop: highest value allowed for result'''


def generate_safe_prime(start, stop):
    flag = True
    while flag:
        prime_candidate = random.randint(start, stop)
        if is_safe_prime(prime_candidate):
            flag = False
    # generate large numbers and run primality test on p and on 2p+1
    return prime_candidate


'''g: generator in Zp of order q, 
a: power we want to compute of g,
p: modulus'''


def modular_exponentiation(g, a, p):
    if a == 0:
        return 1
    elif a % 2 == 0:
        z = modular_exponentiation(g, a / 2, p)
        z = (z ** 2) % p
    else:
        z = modular_exponentiation(g, (a - 1) / 2, p)
        z = ((z ** 2) * g) % p
    return z


'''
q: prime such that 2q + 1 is also prime,
'''


def generate_random_group_elements(q):
    p = 2 * q + 1
    return random.randint(1, p - 1)


'''
number1: first number to check
number2: second number to check
bit_position: position of the bit to check
'''


def are_bits_compatible(number1, number2, bit_position) -> bool:
    bit1 = (number1 >> bit_position) & 1
    bit2 = (number2 >> bit_position) & 1
    return bit1 == bit2 or not (number1 & (1 << bit_position))


def is_tuple_of_bytes(var):
    if not isinstance(var, tuple):
        return False
    return all(isinstance(item, bytes) for item in var)


def tuple_of_bytes_to_ints(var):
    if not is_tuple_of_bytes(var):
        raise Exception("Input is not a tuple of bytes")
    return tuple(int.from_bytes(item, 'big') for item in var)
