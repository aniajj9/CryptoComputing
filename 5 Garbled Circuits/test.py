import secrets
import hashlib

# making L(i) for blood type circuit
left_indexes = {7: 1, 8: 3, 9: 5, 10: 7, 11: 9}
# making R(i) for blood type circuit
right_indexes = {7: 2, 8: 4, 9: 6, 10: 8, 11: 10}
e_value = [] # e_value.append([key0, key1])
d_value = []

def leq(a, b):
    return a <= b

def boolean_and(a, b):
    return a*b

def get_sha256_digest(value):
    hash = hashlib.sha256()
    hash.update(value.encode('utf-8'))
    return hash.digest()

def generate_key_pair():
    return secrets.token_bytes(16), secrets.token_bytes(16)


print(get_sha256_digest("123"))
print(generate_key_pair())
