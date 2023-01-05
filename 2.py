#Создать файл, заменить в этом файле строку.

new_file = open("test2","w")
new_file.write("str 1")
new_file.close()

with open("test2","r") as f:
    print(f.read())

new_str = "str 2"

ad_file = open("test2","w")
ad_file.writelines(new_str)
ad_file.close()

with open("test2","r") as f:
    print(f.read())