#Напишите программу в которой создается текстовый файл. Имя файла вводится пользователем.
# Текст для файла вводится пользователем.
# При записи текста в файл все маленькие буквы заменяются на большие.

text = input("enter text")
nf = input("enter name file")

text_u = text.upper()
print(text_u)
nf_ = nf + ".txt"
print(nf_)

with open(nf_, "w") as f:
    f.write(text_u)
