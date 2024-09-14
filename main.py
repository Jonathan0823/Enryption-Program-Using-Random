import random
import string

chars = list(" " + string.ascii_letters + string.digits + string.punctuation)
keys = chars.copy()

random.shuffle(keys)

plain_text = input("Enter a message you want to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += keys[index]

print(cipher_text)

cipher_text = input("Enter a message you want to decrypt: ")
plain_text = ""

for letter in cipher_text:
    index = keys.index(letter)
    plain_text += chars[index]

print(plain_text)