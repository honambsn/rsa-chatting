from math import sqrt
#required for the sqrt() function, if you want to avoid doing **0.5
import random
#required for randrange
from random import randint as rand

#just to use the well known keyword rand() from C++

nMin = 6703903964971298549787012499102923063739682910296196688861780721860882015036773488400937149083451713845015929093243025426876941405973284973216824503042048
nMax = 13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084095

start = 57896044618658097711785492504343953926634992332820282019728792003956564819968
stop = 231584178474632390847141970017375815706539969331281128078915168015826259279872

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return -1

def isprime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, int(sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
    return True

p = rand(1, 1000)
q = rand(1, 1000)


def generate_keypair(p, q, keysize):
    # nMin = 1 << (keysize - 1)
    # nMax = (1 << keysize) - 1
    primes = [2]
    # start = 1 << (keysize // 2 - 1)
    # stop = 1 << (keysize // 2 + 1)

    if start >= stop:
        return []

    for i in range(3, stop + 1, 2):
        for p in primes:
            if i % p == 0:
                break
        else:
            primes.append(i)

    while (primes and primes[0] < start):
        del primes[0]

    while primes:
        p = random.choice(primes)
        primes.remove(p)
        q_values = [q for q in primes if nMin <= p * q <= nMax]
        if q_values:
            q = random.choice(q_values)
            break
    print(p, q)
    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randrange(1, phi)
    g = gcd(e, phi)

    while True:
        e = random.randrange(1, phi)
        g = gcd(e, phi)
        #generate private key
        d = mod_inverse(e, phi)
        if g == 1 and e != d:
            break


    return ((e, n), (d, n))


def encrypt(msg_plaintext, package):
    e, n = package
    msg_ciphertext = [pow(ord(c), e, n) for c in msg_plaintext]
    return msg_ciphertext


def decrypt(msg_ciphertext, package):
    d, n = package
    msg_plaintext = [chr(pow(c, d, n)) for c in msg_ciphertext]
    # No need to use ord() since c is now a number
    # After decryption, we cast it back to character
    # to be joined in a string for the final result
    return (''.join(msg_plaintext))



def gen_public_private_key():
    bit_length = 3
    print("Running RSA...")
    print("Generating public/private keypair...")
    public, private = generate_keypair(
        p, q, 2 ** bit_length)  # 8 is the keysize (bit-length) value.
    print("Public Key: ", public)
    print("Private Key: ", private)
    return public,private



#-------------------------------------------------------------
#driver program
if __name__ == "__main__":
    bit_length = 512
    print("Running RSA...")
    print("Generating public/private keypair...")
    public, private = generate_keypair(
        p, q, 2**bit_length)  # 8 is the keysize (bit-length) value.
    print("Public Key: ", public)
    print("Private Key: ", private)
    # msg = input("Write msg: ")
    msg = "hi"
    print([ord(c) for c in msg])
    encrypted_msg = encrypt(msg, public)
    print(encrypted_msg)
    print(type(encrypted_msg))
    print("type of encrypted msg: " , type(encrypted_msg))

    print("Encrypted msg: ")
    print(''.join(map(lambda x: str(x), encrypted_msg))) # print as string
    print(type(public))
    print("Decrypted msg: ")
    print(decrypt(encrypted_msg, private))