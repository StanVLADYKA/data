# Напишите программу, которая будет открывать определенный файл file
# и выводить на печать построчно последние строки в количестве lines
# (на всякий случай проверим, что задано положительное целое число).


try:
    lines = int(input("enter last lines for print : "))
    if lines <= 0:
        raise ValueError
except ValueError:
    print("only int and >0")
    raise ValueError

with open("open_f.txt","r") as f:
    f_r = f.readlines()
    n = 0
    for i in f_r:
        n +=1
        if n > len(f_r) - lines:
            print(i)


