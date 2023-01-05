# Требуется реализовать программу,которая выводит слово, имеющее
# максимальную длину (или список слов, если таковых несколько).

with open("open_f.txt","r") as f:
    f_s = f.read()
    f_s2 = f_s.split()
    dic_1 = {}
    n=0
    for i in f_s2:
        dic_1 [i] = len(i)
        if n<len(i):
            n = len(i)

print(n)

for i in dic_1:
    if dic_1[i] == n:
        print(i)

