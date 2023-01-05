#Перевести csv файл в json.

import json
import csv

with open("inv.csv",'r') as f:
    reader = csv.reader(f,delimiter=';')
    next(reader)
    di_1 = {"data": []}
    for row in reader:
        print(row)
        print(type(row))
        di_1 ["data"].append({"No":row[0],"Doc":row[1],"Sum":row[2]})
print(di_1)


with open("inv.json","w") as f_2:
    json.dump(di_1,f_2,indent=4)


