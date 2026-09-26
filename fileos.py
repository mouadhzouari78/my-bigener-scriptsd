import os
from os import *
file_path = "C:/Users/poazw/Desktop/dd"
if os.path.exists(file_path):
    print("file exists")
    if os.path.isfile(file_path):
        print("its a file")
    elif os.path.isdir(file_path):
        print("its a folder")
chaine = input("Enter a file path: ")
l = chaine.replace ("\\" , "/")
print(l)
