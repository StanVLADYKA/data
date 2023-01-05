# Создать файл, прочесть его, вывести количество строк файла

l_ = ["str_1\n","str_2\n","str_3"]

new_file = open("test1.txt","w+")
new_file.writelines(l_)
new_file.close()

n = len(open('test1.txt').readlines())
print(n)