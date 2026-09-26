txt_data = "nigafication"
file_path = "C:/Users/poazw/Desktop/hellow"
with open(file_path,"w") as file:
    file.write(txt_data)
    print("file written")
with open (file_path,"r") as file:
    print(file.read()) 
