import random
import math

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def is_prime(n):
    if n < 2:
        return False
    elif n == 2 or n == 3:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True

def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("p dan q harus prima")
    elif p == q:
        raise ValueError("p dan q tidak boleh sama")
    
    n = p * q
    phi = (p - 1) * (q - 1)
    
    e = random.randrange(1, phi)
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)
    
    d = mod_inverse(e, phi)
    
    return ((e, n), (d, n))

def encrypt(public_key, plaintext):
    e, n = public_key
    ciphertext = [(ord(char) ** e) % n for char in plaintext]
    return ciphertext

def decrypt(private_key, ciphertext):
    d, n = private_key
    plaintext = [chr((char ** d) % n) for char in ciphertext]
    return ''.join(plaintext)

# Contoh penggunaan program
p = 61
q = 53
public_key, private_key = generate_keypair(p, q)

plaintext = "Ini adalah teks yang akan dienkripsi dengan algoritma RSA"
print("Plaintext:", plaintext)

ciphertext = encrypt(public_key, plaintext)
print("Ciphertext:", ciphertext)

decrypted_text = decrypt(private_key, ciphertext)
print("Hasil dekripsi:", decrypted_text)
