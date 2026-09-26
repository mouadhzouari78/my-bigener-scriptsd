import json
file_path = input("Please enter the file path: ")
with open(file_path) as file:
    content = file.read()
    print(content)