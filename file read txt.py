file_path = input("Enter a file path: ")
with open(file_path) as file:
    content = file.read()
    print(content)