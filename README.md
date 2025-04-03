# CIPHEIVE

**Cipheive** is an enhanced version of the classic Caesar Cipher. It uses a 5-digit key to cyclically shift each letter of the input text, providing a more secure encryption method than the traditional single-number Caesar Cipher.

## Description

Cipheive is a substitution cipher that applies multiple shifts to enhance security. It uses a 5-digit random key, with each digit being applied cyclically to each character of the input text.

## Features:

- Key Generation: Random generation of a 5-digit key. 
- Encryption: Encrypts the input text using the 5-digit key, where each character is shifted cyclically based on the key.

## How to Use

### Key Generation:
from utils import key_gen

key = key_gen()
print("Generated Key:", key)


### Encrypting Text:
from utils import encrypt

text = "Hello, World!"
encrypted_text = encrypt(text, key)
print("Encrypted Text:", encrypted_text)



