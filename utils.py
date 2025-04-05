import random
import string


# Generate a 5-digit random key
def key_gen():
    key=[random.randint(0,9) for _ in range(5)]
    return key

def encrypt(text,key):
    letters=list(string.ascii_letters)
    encrypted_txt=""
    for i,char in enumerate(text):
        if char in letters:
            shift=key[i%len(key)]
            idx=letters.index(char)
            new_idx=(idx+shift)%len(letters)
            new_char=letters[new_idx]
            encrypted_txt+=new_char
        else:
            encrypted_txt+=char
    print(encrypted_txt)
    return encrypted_txt

def decrypt(text,key):
    letters=list(string.ascii_letters)
    decrypted_txt=""
    for i,char in enumerate(text):
        if char in letters:
            shift=key[i%len(key)]
            idx=letters.index(char)
            new_idx=(idx-shift)%len(letters)
            new_char=letters[new_idx]
            decrypted_txt+=new_char
        else:
            decrypted_txt+=char
    print(decrypted_txt)
    return decrypted_txt







            
            

   










