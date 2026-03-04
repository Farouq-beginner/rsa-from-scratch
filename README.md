Berikut adalah versi **README.md** yang lebih teknis, lebih profesional, dan bernuansa engineering/cryptography-level.
Siap langsung dipakai di GitHub.

---

# 🔐 RSA From Scratch — Mathematical & Algorithmic Implementation (Python)

## 📖 Overview

Repository ini berisi implementasi algoritma **RSA** yang dibangun *from scratch* menggunakan Python tanpa memanfaatkan library kriptografi eksternal.

Tujuan utama proyek ini adalah:

* Merealisasikan algoritma RSA secara matematis
* Mengimplementasikan komponen inti (number theory primitives)
* Memvalidasi proses enkripsi–dekripsi end-to-end
* Memahami aspek keamanan dan batasan implementasi akademik

⚠️ Implementasi ini bersifat **edukatif**, bukan production-grade cryptosystem.

---

# 🧠 Cryptographic Background

RSA adalah algoritma kriptografi kunci publik yang diperkenalkan pada 1977 oleh:

* Ron Rivest
* Adi Shamir
* Leonard Adleman

Keamanan RSA bergantung pada:

> Computational hardness of integer factorization problem

Secara formal, diberikan:

```
n = p × q
```

di mana `p` dan `q` adalah bilangan prima besar, maka memfaktorkan `n` menjadi `p` dan `q` adalah masalah yang secara komputasional sulit untuk ukuran besar (≥2048 bit).

---

# ⚙️ Mathematical Foundation

## 1️⃣ Key Generation

### Step 1 — Prime Selection

Pilih dua bilangan prima:

```
p, q ∈ ℙ
```

### Step 2 — Modulus Computation

```
n = p × q
```

### Step 3 — Euler Totient

```
φ(n) = (p − 1)(q − 1)
```

### Step 4 — Public Exponent

Pilih `e` sehingga:

```
1 < e < φ(n)
gcd(e, φ(n)) = 1
```

### Step 5 — Private Exponent

Hitung modular inverse:

```
d ≡ e⁻¹ (mod φ(n))
```

Menggunakan **Extended Euclidean Algorithm**.

---

## 2️⃣ Encryption

Untuk plaintext integer `M`:

```
C = M^e mod n
```

---

## 3️⃣ Decryption

```
M = C^d mod n
```

Korektness RSA dijamin oleh Euler’s Theorem:

```
M^(e·d) ≡ M (mod n)
```

---

# 🏗 Project Structure

```
rsa-from-scratch/
│
├── rsa.py
└── README.md
```

---

# 🛠 Implemented Components

Implementasi ini secara eksplisit membangun:

* Euclidean Algorithm (GCD)
* Extended Euclidean Algorithm
* Modular Inverse Computation
* Key Pair Generation
* Modular Exponentiation (via built-in pow with modulus)
* End-to-End Encryption & Decryption

Tidak menggunakan:

```
import rsa
import cryptography
import pycrypto
```

---

# 💻 Installation & Execution

## Requirements

* Python 3.8+
* No external dependencies

## Run Program

```bash
python rsa.py
```

---

# 🧪 Example Execution

Example parameters (academic scale):

```
p = 61
q = 53
e = 17
```

Output:

```
Public Key: (17, 3233)
Private Key: (2753, 3233)

Ciphertext: 2790
Decrypted: 65
```

Verification:

```
Decrypt(Encrypt(M)) = M ✔
```

---

# 🔍 Complexity Considerations

| Operation              | Complexity                             |
| ---------------------- | -------------------------------------- |
| GCD                    | O(log n)                               |
| Modular Inverse        | O(log n)                               |
| Modular Exponentiation | O(log e)                               |
| Factoring n (attacker) | Sub-exponential (best known classical) |

Untuk ukuran kecil (contoh akademik), faktorisasi sangat mudah.
Untuk ukuran 2048-bit, secara praktis tidak feasible dengan classical computing.

---

# 🔐 Security Analysis

## Strengths

* Public-key infrastructure compatible
* Mathematical proof of correctness
* Widely standardized and analyzed
* Strong security with ≥2048-bit keys

## Weaknesses

* Computationally heavy compared to symmetric crypto
* Vulnerable to small key sizes
* Deterministic without padding
* Broken under quantum computing (Shor’s Algorithm)

Production systems menggunakan:

* OAEP Padding
* 2048/3072-bit modulus
* Hybrid encryption (RSA + AES)

---

# 🚫 Limitations of This Implementation

This implementation intentionally:

* Uses small primes
* Does not implement padding (PKCS#1 / OAEP)
* Does not include probabilistic prime generation
* Does not defend against timing attacks
* Does not use constant-time arithmetic

⚠️ Do NOT use this implementation in real systems.

---

# 📈 Possible Extensions

Future improvements:

* Miller–Rabin primality test
* Random large prime generation
* Implement PKCS#1 v1.5
* Add OAEP padding
* Add digital signature mode
* Benchmark performance for large key sizes

---

# 📚 Academic Context

This repository was developed for:

Course: Keamanan Data dan Informasi
Assignment: Analisis dan Implementasi Mekanisme Kriptografi
Type: Individual
Year: 2026

---

# 👤 Author

Nama  : [Farouq Gusmo Abdilah]
NIM   : [25051204337]
Kelas : [2024TIH]
Prodi : [S1 Teknik Informatika]

---

# 📌 Final Note

This project demonstrates that RSA can be fully reconstructed from number theory fundamentals without relying on cryptographic black-box libraries.

Understanding the mathematics behind RSA is essential before trusting real-world cryptographic frameworks.

---

Jika Anda mau, saya bisa:

* 🔥 Tambahkan versi dengan input string → otomatis dikonversi ke integer
* 🔥 Tambahkan diagram alur RSA (Markdown + ASCII visual)
* 🔥 Tambahkan mode digital signature
* 🔥 Tambahkan versi dengan prime generator (Miller–Rabin) agar terlihat lebih advanced

Tinggal pilih ingin versi “nilai A” atau “nilai A+ dengan keunggulan teknis tambahan”.
