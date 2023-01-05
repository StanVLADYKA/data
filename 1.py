# В файле nums.txt находятся вещественные числа. Вывести их на экран и подсчитать к-во
n = 0
with open("nums.txt","r") as f:
    for num in f:
        print(num)
        n += 1

print(f"num =", n)