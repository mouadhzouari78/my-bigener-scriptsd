import csv
file_path = "C:/Users/poazw/Desktop/clown.csv"
content = [["blob"  , 2],
           ["slime" , 3 ]]
with open(file_path,"w") as file:
    writer = csv.writer(file)
    for row in content:
        writer.writerow(row)