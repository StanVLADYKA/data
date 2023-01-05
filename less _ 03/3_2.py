# Запросить у пользователя данные (имя, фамилия, возраст) и создать файл с этими значениями.

n_1 = input("enter firstname:  ")
n_2 = input("enter surname:  ")
n_3 = input("enter age:  ")

with open("Full_name.txt","w") as f:
    fr = "firstname: " + n_1 + ",  surname:  " + n_2 + ",   age:  "+n_3
    f.write(fr)