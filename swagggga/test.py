import sys

# Открытие файла
# myfile = open("hello.txt", "a")
# #  Запись в файл
# myfile.write("yyy")
# print("test")
# print("test",file=myfile)
# # Закрытие файла
# myfile.close()
# f = open("hello.txt", "r")
# print(f.read())
# print("--------------")
# print(f.readline())
# f.close()

# Создать папку под названием 111
# Внутри папки 111 создать файл под название test.txt
# Записать в файл Hello, World
# Создать папку 222 рядом с папкой 111.
# Перенести (или скопировать) файл test.txt в папку 222
# Удалить файл из папки 111
# Дописать в файл test.txt следующую строку "Hello,<Имя>"
# Вывести содержимое файла в консоль

# import sys
# import os
# os.mkdir('111')
# os.chdir('111')
# myfile = open('test.txt','a')
# print("hello world", file=myfile)
# os.chdir('C:/Users/Администратор/PycharmProjects/swagggga')
# os.mkdir('222')
# a = input('имя - ')
# print(f'hello {a}', file=myfile)
# os.chdir('C:/Users/Администратор/PycharmProjects/swagggga/222')
# myfile = open('test.txt','a')
# print("hello world", file=myfile)
# print(f'hello {a}', file=myfile)
# os.chdir('C:/Users/Администратор/PycharmProjects/swagggga/111')
# os.remove('test.txt')
# C:\Users\Администратор\PycharmProjects\swagggga

import os
import sys

if not os.path.exists('C:/Users/Администратор/PycharmProjects/swagggga/111'):
    os.mkdir('111')
    print('папка 111 создана')
else:
    print('папка 111 уже существует')

os.chdir('111')

if not os.path.exists("C:/Users/Администратор/PycharmProjects/swagggga/111/test.txt"):
    if not os.path.exists('C:/Users/Администратор/PycharmProjects/swagggga/222/test.txt'):
        myfile = open('test.txt','a')
        print('файл test создан')
        print('hello world',file = myfile)
        a = input('name - ')
        print(f'hello {a}',file=myfile)
    else:
        pass
else:
    print('папка test уже существует')

os.chdir('C:/Users/Администратор/PycharmProjects/swagggga')

if not os.path.exists('C:/Users/Администратор/PycharmProjects/swagggga/222'):
    os.mkdir('222')
