
import string
import random
chars = string.punctuation + string.digits + string.ascii_letters + " "
chars = list(chars)
key = chars.copy()
print(f"chars: {chars}")
random.shuffle(key)
print(f"usable key is {"".join(key)}")
encrypted_text = ""
print(f"key  : {key}")
cypher_text = input("enter the text u wanna encrypt: ")
encrypted_text = ""
for letter in cypher_text:
    index = chars.index(letter)
    encrypted_text += key[index]
print(f"encrypted_text: {encrypted_text}")


