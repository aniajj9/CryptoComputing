import math
import random


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
    print(a, p)
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


def are_bits_compatible(number1, number2, bit_position) -> bool:
    bit1 = (number1 >> bit_position) & 1
    bit2 = (number2 >> bit_position) & 1
    return bit1 == bit2 or not (number1 & (1 << bit_position))
