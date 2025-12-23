from ecdsa.ecdsa import curve_256, generator_256, Public_key, Private_key
from Crypto.Util.number import bytes_to_long, long_to_bytes
from hashlib import sha256
import random

def extended_euclid(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_euclid(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def inverse_mod(a, m):
    gcd, x, y = extended_euclid(a % m, m)
    if gcd != 1:
        raise ValueError("Inverse doesn't exist")
    else:
        return x % m

curve = curve_256
generator = generator_256
n = generator.order()

secret_key = random.randrange(1, n)
public_key = Public_key(generator, generator * secret_key)
private_key = Private_key(public_key, secret_key)

k = random.randrange(curve.p())
message1 = "I fell in love with Trang."
message2 = "You never know how it feels."
z1 = bytes_to_long(sha256(message1.encode()).digest())
z2 = bytes_to_long(sha256(message2.encode()).digest())

signature1 = private_key.sign(z1, k)
signature2 = private_key.sign(z2, k)

found_k = (z1 - z2) * inverse_mod(signature1.s - signature2.s, n) % n
assert k == found_k

found_key = inverse_mod(signature1.r, n) * (found_k * signature1.s - z1) % n
assert found_key == secret_key
print("success!")
