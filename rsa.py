# ==============================
# IMPLEMENTASI RSA FROM SCRATCH
# ==============================

# Fungsi GCD
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Extended Euclidean Algorithm
def mod_inverse(e, phi):
    def extended_gcd(a, b):
        if a == 0:
            return b, 0, 1
        gcd, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y

    gcd_val, x, y = extended_gcd(e, phi)
    return x % phi

# Key Generation
p = 61
q = 53
n = p * q
phi = (p - 1) * (q - 1)
e = 17
d = mod_inverse(e, phi)

# Enkripsi & Dekripsi
message = 65
cipher = pow(message, e, n)
plain = pow(cipher, d, n)

print("Public Key:", (e, n))
print("Private Key:", (d, n))
print("Ciphertext:", cipher)
print("Decrypted:", plain)