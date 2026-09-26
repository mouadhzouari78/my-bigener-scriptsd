import json

file_path = "C:/Users/poazw/Desktop/niggie.json"
content = {"name" : "spongbob" , "age" : 5 }
with open(file_path,"w") as file:
    json.dump(content,file ,indent=4)