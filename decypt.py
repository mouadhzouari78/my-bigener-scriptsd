import string
encrypted_text = input("Please enter your encrypted text: ")
key = input("Please enter your key: ")
key = list(key)
chars = string.punctuation + string.digits + string.ascii_letters + " "
chars = list(chars)
dycripted_message = ""
for letters in encrypted_text:
    index = key.index(letters)
    dycripted_message += chars[index]
print(dycripted_message)