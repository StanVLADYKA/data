# Удалить строку из файла по ее индексу. (например вторую)

with open("test_3.txt", "r") as f:
    f_n = f.readlines()
    f_n.pop(1)

with open("test_3.txt", "w") as f:
    for f_2 in f_n:
        f.write(str(f_2))











# with open("test_3.txt", "r+") as f:
#     f_n = f.readlines()
#     print(type(f_n))
#     print(f_n)
#     f_n.pop(1)
#     print(f_n)
#     f.seek(0)
#     for f_2 in f_n:
#         f.write(str(f_2))
#         print(f_2)
#
#     print(f_n)
