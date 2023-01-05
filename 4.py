#Вставить строку в указанную позицию файла.

str_1 = "new str"
num = int(input("input pos num  :"))

with open("test_4.txt", "r+") as f:
    f_a = f.readlines()
    f_a.insert(num-1,str_1)
    f.seek(0)
    for i in f_a:
        f.write(i)