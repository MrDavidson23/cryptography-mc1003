# Seguridad y Criptografía (MC1003)

Labs and homework for the **Security and Cryptography** course (MC1003), fall 2026.
Textbook: *Cryptography Made Simple*, Nigel Smart (Springer, 2016). The book is not included in this repo.

## Contents

| Folder | Topic | Description |
|---|---|---|
| [`lab1/`](lab1) | Classical XOR ciphers | Breaks a single-byte XOR cipher and a repeating-key (Vigenère-style) XOR cipher by using English letter-frequency scoring and Hamming-distance key-length detection. |
| [`homework2/`](homework2) | One-time pad & LFSRs | Bit-flipping attack on a one-time pad (malleability) and brute-force linear complexity of LFSR sequences. Solutions are in `Homework2_Solutions.pdf`. |

### Lab 1: Breaking XOR ciphers

```bash
cd lab1
python3 1_2.py
```

- **Exercise 1:** Decodes `ct1.txt` (base64) and tries all 255 single-byte keys. It ranks each candidate plaintext by its chi-squared distance from English letter frequencies.
- **Exercise 2:** Decodes `ct2.txt` and estimates the key length from the normalized Hamming distance between blocks. It then splits the ciphertext into one stream per key byte and breaks each stream as a single-byte XOR.

### Homework 2: One-time pad & LFSR

Assignment: [`homeworks_02-homework.pdf`](homeworks_02-homework.pdf)

```bash
cd homework2
python3 ex1.py   # OTP malleability: "Trust Charlie" -> "Trust Mallory"
python3 ex3.py   # Linear complexity examples for L(s ⊕ t)
```

- **ex1.py:** One-time pad encryption is malleable. XOR-ing the ciphertext with `"Trust Charlie" ⊕ "Trust Mallory"` changes the plaintext without the attacker knowing the key.
- **ex3.py:** Finds the shortest LFSR that generates a sequence (brute force over tap sets). It gives examples where `L(s ⊕ t) < min(L(s), L(t))` and where `L(s ⊕ t) = L(s) + L(t)`.

## Course schedule

| Week | Wednesday | Saturday |
|---|---|---|
| 41 | Introduction & Historical Ciphers | Enigma & Security Definitions |
| 42 | Information Theory | Lab 1 |
| 43 | Stream Ciphers & Block Ciphers | AES |
| 44 | Attacks on Symmetric Ciphers | Other Symmetric Primitives |
| 45 | Public-Key Encryption | RSA |
| 46 | ECC & Hardness Assumptions | Lab 2 |
| 47 | Public-Key Cryptography Use Cases | Post-Quantum Cryptography I |
| 48 | Post-Quantum Cryptography II | Multi-Party Computation |
| 49 | Zero-Knowledge Proofs | Watermarking |
| 50 | Recap & Q&A | Exam |

## Requirements

Python 3.8+. Only the standard library is used.
