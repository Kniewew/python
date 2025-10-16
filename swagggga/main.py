# a = int(input("Введите первое число = "))
# b = int(input("Введите второе число  = "))
# print("Сложение = ", a+b)
# print("Разность = ", a-b)
# print("Частное = ", a/b)
# print("Произведение = ", a*b)
#from PIL.ImagePalette import sepia
#from platform import android_ver
# from subprocess import
from os import getcwd
from sys import orig_argv

from sqlalchemy import values
from sqlalchemy.sql.operators import truediv

# t = int(input("Введите первое число = "))
# y = int(input("Введите второе число  = "))
# u = int(input("Введите третье число  = "))
# print("Сложение = ", (t+y)+u)
# print("Разность = ", (t-y)-u)
# print("Частное = ", (t/y)/u)
# print("Произведение = ", (t*y)*u)

# v = int(input("скорость = "))
# t = int(input("время = "))
# print(" путь = ", v*t, "м" )
# a = int(input("Введите первое число = "))
# b = int(input("Введите второе число = "))
# c = int(input("Введите третье число = "))

# n = int(input("введите пароль: "))
# if n== 7355608:
#     # print("доступ разрешен")
#     # a = int(input("Введите первое число = "))
#     # b = int(input("Введите второе число = "))
#     # c = int(input("Введите третье число = "))
#     # if (a!=b) and (b!=c):
#     #     if (a>b) and (b>c):
#     #         print('Число "a" наибольшее')
#     #     elif (a<b) and (b>c):
#     #         print('Число "b" наибольшее')
#     #     elif (c>a) and (c>b):
#     #         print('Число "c" наибольшее')
#     #     else:
#     #         print('числа равны1')
#     #         print('Наибольшее число',a)
# else:
#     print("фу нельзя")
# n=int(input("введите пароль: "))
# if n==2580:
#     print("можно")
#     a = int(input("Введите первое число = "))
#     b = int(input("Введите второе число = "))
#     c = int(input("Введите третье число = "))
#     m = int(input("выбирете действие (1 сравнить) (2 вычеслить) - "))
#     if m == 1:
#         if (a >= b) and (a >= c):
#             enter = a
#         elif (b >= a) and (b >= c):
#             enter = b
#         else:
#             enter = c
#         print("Максимальное число =", enter)
#     if m == 2:
#         q = int(input("выберете действие (1 сложение) (2 вычитание) (3 умножение) (4 деление): "))
#         if q==1:
#             print("сумма =  ", a+b+c)
#         if q==2:
#             print("разность = ", a-b-c)
#         if q==3:
#             print("произведение = ", a*b*c)
#         if q==4:
#             print("частное = ", a/b/c)
#
# else:
#     print(f"пароль {n} не верный")



# n = int(input("Введите число n: "))
# s = 0
# for i in range(1, n + 1):
#     s += i
#     if s >= 100:
#         print(f"Сумма достигла 100 или больше на повторении: {i}")
#         break
# else:
#     print("Сумма не достигла 100 в диапазоне от 1 до n.")
#
# a = int(input("Введите число a: "))
# b = int(input("Введите число b(не должен быть больше числа) a: "))
# n = 0
# for i in range(a, 11):
#     if i == b:
#         continue
#     n += i
# print(f"Сумма чисел от {a} до 10, исключая {b}, равна: {n}")
#
# height = int(input("высота елки "))
# for i in range(height):
#     print(' ' * (height - i - 1), end='')
#     print('*' * (2 * i + 1))
# print(5*"2")

# a=0
# b=16
# s=0
# s1=0
# for i in range(15):
#     a+=1
#     b=b-1
#     s=s+a
#     s1= s1 + b
#     print(a,b,sep=('|'))
# print('_____')
# print(s,s1,sep=( "|" ))

# v=0
# x=6
# while v<=10:
#     v += 1
#     x += 1
#     if v!=5  and x!=11:
#         continue
# if v ==8 and x==24:
#     break
#  print(v,x,sep=(" | "))
# for i in range(3):
#     for j in range(3):
#         print(f"i={i},j={j}")

# for i in range(1,3):
#     print("верхний цикл = ",i,"-ое повторение")
#     for j in range(1,7):
#         print("hello world",end="")
#         print(" вложенный цикл = ",j,"-ое повторение")

# a = 0
# for i in range(3):
#     # print(i)
#     for j in range(3):
#         a+=1
#         print(a,end=" ")
#     print(end="\n")
#
# n = 3
# matrix = [[0 for _ in range(n)] for _ in range(n)]
# for i in range(n):
#     matrix[i][i] = "?"
# for row in matrix:
#     print(' '.join(map(str, row)))


# a=0
# for i in range(3):
#     for j in range(3):
#         print(a,end='')

# list1 = [4,'ser',True,34,67,'wer','rtt']
# for k in range(7):
#     print(list1[k])

# list5 = [r for r in range (9)]
# print(list5)

# str1 = "hello world"

# list6 = list(str1)
# print(list6)

# list7 = [i for i in range(5)]
# print(list7)
# list7.append("erer")
# print(list7)
# list8 = list7.reverse()
# print(list8)
# print(sum(list7))

# print([i for i in range (22,28)])
# print([i for i in range (22,28),if!=25])

# list8 = [22,23,25,26,27]
# for j in range(5):
#     if list8[j]!=25:
#         print(list8[j], end= " ")
#
# print("\n")
# print("-"*10)
# s = 0
# for k in range (5):
#     s+=list8[k]
# print(s)

# list1 = [1,2,3,4,5]
# list1.append(777)
# print(list1)
# a = int(input("число"))
# list2 = [8,7,2,4,6,8]
# list2.append(a)
# print(list2)
# print(a)

# list3 = [8,4,8,9,2,7]
# list3.append(42)
# print(list3)
#
# list3.insert(5,2)
# print(list3)
#
# list3 = [36,89,53,41,99,]
# list3.extend(list3)
# print(list3)
#
# list3.remove(36)
# print(list3)
#
# list3.clear()
# print(list3)
# list4 = [3,5,6,87,12]
# list4.extend(list3)
# print(list3.index(2))

# list42 = [11,22,33,44,55]
# a = list42.pop(2)
# print(a)
# print(list42)
# b = list42.pop()
# print(list42)
# print(b)



# . Создать отсортированный по возрастанию числовой массив
# # Для этого сначала выделим все числовые элементы
# numeric_list = [item for item in list1 if isinstance(item, (int, float))]
#
# # Отсортируем числовой список
# sorted_numeric = sorted(numeric_list)
#
# print("Отсортированный числовой массив:", sorted_numeric)
#
# # 2. Все строковые элементы собрать в отдельный список
# string_list = [item for item in list1 if isinstance(item, str)]
# print("Строковые элементы:", string_list)
#
# # 3. Найти максимальный и минимальный элемент из числового массива
# max_num = max(numeric_list) if numeric_list else None
# min_num = min(numeric_list) if numeric_list else None
# print("Максимальный элемент:", max_num)
# print("Минимальный элемент:", min_num)
#
# # 4. Удалить максимальный и минимальный элементы из исходного списка
# # Для этого удалим их только один раз (если они есть)
# if max_num in list1:
#     list1.remove(max_num)
# if min_num in list1:
#     list1.remove(min_num)
#
# print("Обновленный список после удаления максимального и минимального:", list1)



# a = list42.remove(3)
# print(a)

# list52 = [23,34,45,32,23]
# a = list52.count(23)
# print(a)

# list34 = [223,34,45,32,123,23]
# list35 = list34.copy()
# print(list35)

# list34.reverse()
# print(list34)
# list34 = list35.copy

# list8 = [23,4,5,6,7,8,234,456,5,77]
# print(len(list8))
# print(max(list8))
# d = min(list8)
# print(d)
# 1. Создать отсортированный по возрастанию числовой массив
# 2. Все строковые элементысобратьв отдельный список
# 3. Найти максимальный и минимаьный элемент из числовго масива
# 4. Удалить максимальны, вытолкнуьб минимальный

# list1 = [1,True,2,"x",'eret',-237,'list1',3-77,'Hello World',4,-200,':-)','index',]

        #1111111111111111111
# list1 = [i for i in list1 if isinstance(i, (int, float))]
# e = sorted(list1)
# print("Отсортированный числовой массив:", e)

        #2222222222222222222
# list1 = [i for i in list1 if isinstance(i, str)]
# print("Строковые элементы:", list1)

        #3333333333333333333
# print(min(list1))
# print(max(list1))

        #4444444444444444444
# if "max_num" in list1:
#      list1.remove("max_num")
# if "min_num" in list1:
#      list1.remove("min_num")
#
#  print(list1)


###код сергея валерьевича


# list1 = [1,True,2,"x",'eret',-237,'list1',3-77,'Hello World',4,-200,':-)','index',]
# # list3 = list1.copy()
# # # 1. Создать отсортированный по возрастанию числовой массив
# # # 2. Все строковые элементы собрать в отдельный список
# # # 3.Найти максимальый и минимальный элементы из числового массива
# # # 4. Удалить максимальный, вытолкунть минимальный
# list2 = []
# a = list1.pop(0)
# print(a)
# list2.append(a)
# print(list2)
# a = list1.pop(1)
# list2.append(a)
# print(list1)
# print(list2)
# print(list1)
# list2.append(list1.pop(3))
# print(list1)
# print(list2)
# list2.append(list1.pop(4))
# print(list1)
# print(list2)
# list2.append(list1.pop(-4))
# print(list1)
# print(list2)
# list2.append(list1.pop(-3))
# print(list1)
# print(list2)
# list2.sort()
# print(list2)
# list1.remove(True)
# print(list1)
# print(min(list2))
# print(max(list2))
# list2.remove(min(list2))
# print(list2)
# s = list2.pop(-1)
# print(s)
# print(list2)


# list1 = [1,2,3,4,5]
# list2 = ["a","b","c","d","e"]
# list3 = []

        # [1, 'a',2'b',3'c',4,'d',5,'e']

# list3 = []
# for i in range(5):
#     list3.append(list1.pop(0))
#     list3.append(list2.pop(0))
#     print(list3)

# list1 = [1,2,'we',3,'wer',4,5,6,'sad',7]

#Найти сумму чисел

# for i in range(len(list1)):
#     if isinstance(list1 [i], (int, float)):
#         list2 += list1 [i]
#
# print(list2)
# list1.pop (2)
# list1.pop (3)
# list1.pop (-2)
# print(sum(list1))
# print(list1)
#
# print(list1[0]+list1[1]+list1[3]+list1[5]+list1[6]+list1[7]+list1[9])
#
# s = 0
# for i in list1:
#     if type(i) == int:
#         s+=i
#         print(a)


# b = 23
# c = True

# a = 2,5
#
# if type(a)==list:
#     print('список')
#
# elif type(a) == int:
#     print("целок ")
# elif type (a)== float:
#     print('вещественное число')
# elif type (a)== bool:
#     print('Логическая переменная')





# total_sum = 0
# for item in list1:
#     if isinstance(item, (int, float)) and not isinstance(item, bool):
#         total_sum += item


# print("Сумма чисел в списке:", total_sum)


# Найти сумму чисел
# Найти количество целых чисел, вещественных чисел
# Найти количество логических значений
# Найти количество строковых значений



##### Найти количество целых чисел, вещественных чисел
# list1 = [1, True, 2, "x", 'eret', -2, 'list1', 2.5, False, 3 - 77, 'Hello World', 4, -7, ':-)', 4.5, 'index']
#
#
# a = 0
# b = 0
# c = 0
# s = 0
# f = 0
#
# # Проходим по всем элементам списка
# for i in list1:
#     if isinstance(i, int):
#         a += i
#         b += 1
#     elif isinstance(i, float):
#         a += i
#         c += 1
#     elif isinstance(i, bool):
#         s += 1
#     elif isinstance(i, str):
#         f += 1
#
#     # результаты
# print(f"Сумма чисел: {a}")
# print(f"Количество целых чисел: {b}")
# print(f"Количество вещественных чисел: {c}")
# print(f"Количество логических значений: {s}")
# print(f"Количество строковых значений: {f}")


# list1 = [1,True,2,"x",'eret',-237,'list1',3-77,'Hello World',4,-200,':-)','index',]


# list1 = [1, True, 2, "x", 'eret', -237, 'list1', 3 - 77, 'Hello World', 4, -200, ':-)', 'index']
# list3 = list1.copy()
#
# # 1. числовой массив
# numbers = [x for x in list3 if isinstance(x, (int, float))]
# numbers.sort()
# print("Отсортированный числовой массив:", numbers)
#
# # 2. строковые элементы
# strings = [x for x in list3 if isinstance(x, str)]
# print("Список строк:", strings)
#
# # 3. максимальный и минимальный элементы
# max_num = max(numbers)
# min_num = min(numbers)
# print("Максимальный элемент:", max_num)
# print("Минимальный элемент:", min_num)
#
#
# numbers.remove(max_num)
# popped_min = numbers.pop(0)
# print("Числовой массив после изменений:", numbers)
# print("Вытолкнутый минимальный элемент:", popped_min)
# list1 = [1, True, 2, "x", 'eret', -2, 'list1', 2.5, False, 3 - 77, 'Hello World', 4, -7, ':-)', 4.5, 'index']
# a = 0
# b = 0
# c = 0
# s = 0
# f = 0
#
# # Проходим по всем элементам списка
# for i in list1:
#     if isinstance(i, int):
#         a += i
#         b += 1
#     elif isinstance(i, float):
#         a += i
#         c += 1
#     elif isinstance(i, bool):
#         s += 1
#     elif isinstance(i, str):
#         f += 1
#
#     # результаты
# print(f"Сумма чисел: {a}")
# print(f"Количество целых чисел: {b}")
# print(f"Количество вещественных чисел: {c}")
# print(f"Количество логических значений: {s}")
# print(f"Количество строковых значений: {f}")

# list1 = [1,True,2,"x",'eret',-237,'list1',3-77,'Hello World',4,-200,':-)','index',]
# list3 = list1.copy()
#
# list2 = []
# a = list1.pop(0)
# print(a)
# list2.append(a)
# print(list2)
# a = list1.pop(1)
# list2.append(a)
# print(list1)
# print(list2)
# print(list1)
# list2.append(list1.pop(3))
# print(list1)
# print(list2)
# list2.append(list1.pop(4))
# print(list1)
# print(list2)
# list2.append(list1.pop(-4))
# print(list1)
# print(list2)
# list2.append(list1.pop(-3))
# print(list1)
# print(list2)
# list2.sort()
# print(list2)
# list1.remove(True)
# print(list1)
# print(min(list2))
# print(max(list2))
# list2.remove(min(list2))
# print(list2)
# s = list2.pop(-1)
# print(s)
# print(list2)

# list3 = [3,4,'b'] удалить из лист 1 и лист 2 значениия из лист 3
# list1 = [1,2,3,4,5]
# list2 = ["a","b","c","d","e"]
# list3 = [3,4,'b']
# for i in list3:
#
#     for j in list1:
#         # print(i)
#         # print(j)
#         if i==j:
#             list1.remove(j)
# print(list1)


# вариант 1
# list1 = [1,2,3,4,5]
#
# tuple1 = tuple(list1)
# print(tuple1)
# print(tuple1[0])
# print(tuple1[-1])
#
# a,b,c,d,e = tuple1
# print(a)
#
# # вариант 2
#
# tuple3 = tuple([1,2,3,4,5])
# print(tuple3)
#
# tuple4 = 1,2,3,4,5
# print(tuple4)
#
# tuple5 = 9,
# print(tuple5)
#
# for i in tuple4:
#     print(i)


# tuple1= (1,2,3,4,5)
# list1 = list(tuple1)
# print(list1)
# list1.append(23)
# print(list1)
# tuple2 =tuple(list1)
# print(tuple2)

# db_connect = ("host",'root',123)
#
# print(db_connect)
# del db_connect
# print(db_connect)

#
# tuple1= (1,2,3,4,5)
# print(len(tuple1))
#
# tuple3 = tuple1+tuple2

# tuple1 = tuple([1,2,3])
# tuple2 = (1,2,3)
# l1=[1,2,3]
# l2=[1,2,3,4]

# tuple1 = (1,2,3)
# print(tuple1*3)
# list1 = [1,2,3]
# print(list1*3)

# tuple1 = ()
# # print(tuple1)
# #
# # while True:
# #     user_num = int(input("vedite chislo dlya dobavleniya v kortezh: "))
# #     list1 = list(tuple1)
# #     list1.append(user_num)
# #     tuple1 = tuple(list1)
# #
# #     if i==3:
# #         break
# #     i+=1
# #
# # print(tuple1)

# t1 = 2,3,4,5,6
# print(t1)

# user_num = input("vedite chislo dlya dobavleniya v kortezh: ")
# print(list(user_num))
# print(tuple(list(user_num)))

# list1 = ['1', ',', '2', ',', '3']
# list2 = []
# for i in list1:
#     if i!=',':
#         list2.append(int(i))
# print(tuple(list2))
# #    рдактпрование кортежа
# tuple1 = 1,2,3,4,5
# for i in tuple1:
#     print(i)
#
# tuple2 = (1,2,3,4,5)
# print(tuple2)
# list1 = list(tuple2)
# list1.append(6)
# print(list1)
# tuple2 = tuple(list1)
# print(tuple2)

# # словарь
# dict1 = {
#     "1":23,
#     23:23,
#     'wrewre':'sgw',
#     (2,3): True,
#     True:34
#
# }
# print(dict1)
# print(dict1['1'])

# dict3 = {
#     1:1,
#     2:2,
#     3:3,
#     4:4,
#     5:5,
# }
# print(dict3)

# student = {
#     "name":"Ivan",
#     "dr":'28.01,2008',
#     "step":721,
#     "adress":"Shumerlya",
#     "pred":["информатика"],
#     (4,5):"yes"
# }
# # print(student["dr"])
# del student[(4,5)]
#
# print(student)
# del student["dr"]
#
# # print(student)
# a = student.get("dr","нет значения")
# print(a)
#
# b = student.get("adress")
# print(b)
#
# c = student.get("aqwerty","нет значения")
# print(c)
#
# student["step"] = 1220
# d = student.get("step")
# print(d)
# # добавление
# student["email"] = ".com"
# print(student)
#
# # student.clear()
# print(student)
# st1 = student.copy()
# print(st1)
# print(id(st1))
# print(id(student))
# print(student)
# a = st1.pop("email")
# print(a)
# print(st1)
# print(st1.keys())
# print(st1.items())
# print(st1.values())
#
# print(st1.setdefault("ergve",123))
# print(st1)

# dogs ={
#     "name":"Дин",
#     "old":"8",
#     "porod":"такса",
#     "color":"черная",
#     "pol":"мальчик",
#     "kg":10,
#     "sherst":"короткая",
#
# }
# print(dogs)
# print(dogs["name"])
#
# dogs["coloreyes"] = "карие"
# print(dogs)
#
# dg1 = dogs.copy()
# print(dg1)
# dg1.clear()
# print(dg1)
#
# dg1["name"] = "Nelma"
# dg1["color"] = "white"
# dg1["old"] = "3"
# dg1["animal"] = "dog"
# print(dg1)

# dict_num = {
#     "a":1,"b":2,"c":3,"d":4,"e":5
# }
# print(dict_num)
# print(dict_num.keys())
#
# a = dict_num["a"]+dict_num["b"]+dict_num["c"]+dict_num["d"]+dict_num["e"]
# print(a)
#
# print(sum(dict_num.values()))
# print(dict_num.values())
#
# print(list(dict_num))

# import os
#
#
# print(os,getcwd())
# a = os.getcwd()
# print(type(a))
# print(os.listdir())
# b = os.listdir()
# print(type(b))
#
# # os.mkdir('test.txt')
# # print(os.listdir())
#
# l1 = os.path.exists("test.txt")
# print(l1)

# import os
# import sys
# print(os.getcwd()) # Получает путь
# a = os.getcwd()
# print(type(a))
# print(os.listdir()) # Выводит объекты в виде списка
# b = os.listdir()
# print(type(b))
# print(b[2])
# # os.mkdir("test") # Создает папку
# # os.mkdir("test2")
# # os.mkdir("test3")
# # os.rmdir("test3")
# print(os.listdir())
# # os.rename('test.txt','test2.txt')
# print(os.listdir())
# l1 = os.path.exists('test2.txt') # поревряет существование файла
# print(l1)
# # os.remove('test2.txt')
# print(os.path.exists('test2.txt'))
# os.rename('test2.txt','D:/PythonProject10/test2/test2.txt')

# import os
#
# print(os.getcwd())
# # os.mkdir("test1")
# if not os.path.exists("C:/Users/Администратор/PycharmProjects/swagggga/test1"):
#     os.mkdir('test2')
#     print("папка test создана")
# else:
#     print("папка уже есть")
#
# if os.path.exists("C:/Users/Администратор/PycharmProjects/swagggga/turbo"):
#     os.rename("turbo","C:/Users/Администратор/PycharmProjects/swagggga/turbo")
#     print("файл turbo ")

# dict1 = dict()
# print(dict1)
# print(type(dict1))
#
# dict2 = {
#         1:1,
#         2:2,
#         2:2,
# }
# print(dict2)
# a = dict2["key1"]+dict2['key2']+dict2["key3"]
# print(a)

# s= 0
# for i in dict2.values():
#     s+=i
# print(s)
#
# s1 = 0
# for j in dict2.keys():
#     s1+=j
#     print(s1)

# dict2 = {
#     1:1,
#     4:2,
#     5:3,
#     7:5,
#     8:11,
#     9:3
#     #5,7,8,9
#  }
#
# # j=0
# # for k,v  in dict2.items():
# #      if v%2!=0:
# #          j+=v
# # print(j)
#
# j2 =0
#
# for i in dict2:
#       if not dict2[i]% 2 == 0:
#  print(j1)
#




# s = 0
# for i in dict1.values():
#     s+=i
# print(s)
# s1 = 0
# for i in dict1.keys():
#     s1+=i
# print(s+s1)
# a=0
# b=0
# for k,v in dict1.items():
#     a+=k
#     b+=v
#     print(f'Ключ={k},значение={v} ')
# print(a+b)

# import os
# import sys
# print(os.getcwd()) # Получает путь
# a = os.getcwd()
# print(type(a))
# print(os.listdir()) # Выводит объекты в виде списка
# b = os.listdir()
# print(type(b))
# print(b[2])
# # os.mkdir("test") # Создает папку
# # os.mkdir("test2")
# # os.mkdir("test3")
# # os.rmdir("test3")
# print(os.listdir())
# # os.rename('test.txt','test2.txt')
# print(os.listdir())
# l1 = os.path.exists('test2.txt') # поревряет существование файла
# print(l1)
# # os.remove('test2.txt')
# print(os.path.exists('test2.txt'))
# os.rename('test2.txt','D:/PythonProject10/test2/test2.txt')

# set1 = {1,2,3,4,5}
# print(set1)
# print(type(set1))
#
# list1 = [1,2,2,3,4,5,5,5,5,5,5,5,5,5,5,5]
#
# set2 = set(list1)
# print(set2)
#
# list2 = ['h','h','e','l','l']
# print(set(list2))
#
# print(list2[0])
#
# set3 = {1,'hello',2,3,True,'world'}
# print(set3)
# set3.add(45)
# # print(set3[0])
# for i in set3:
#     print(i)
#
# set3.remove(1)
# print(set3)
#
# set4 = set(list4)
# list4 =[1,1,1,1,1,1,1,1,1,1,1,1]

# set1 = {1,2,2,3,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,4,4}
# print(set1)
#
# set1.add('goblin')
# print(set1)
#
# list1 = list(set1)
# print(type(set1))
#
# set1.remove(2)
# print(set1)
#
#
# print(set1)
#
# set5 = {4,5,6,7,89,10}
# set5.remove(89)
# set5.add(8)
# set5.add(9)
# print(set5)
# print(id(set5))

# set1 = {0}
# list1 = []
# for i in range(5):
#     a = input('введите число ')
#     if i%2==0:
#         set1.add(a)
#     else:
#         list1.append(a)
# set1.remove(0)
# print(set1)
# print(list1)

# set1 = {i for i in range(5)}
# print(set1)
#
# dict1 = {'key'+str(1):i for i in range(5)}
# print(dict1)
#
# list1 =[i for i in range(5)]
# print(list1)

# list1 = [1,2,3]
# list2 = list()
#
# tuple1 = (1,2,3)
# tuple2 = tuple()
#
# dict1 = {
#     1:1,
#     2:2,
#     3:3,
# }
# dict2 = dict()
# #множества
# set1 = {1,2,3}
# set2 = set()
#
# # строки как массивы
# str1= 'hello world'
# # print(str1[1])
# for i in range(len(str1)):
#     print(str1[i],i)

# list3 = list(str1)
# print(list3)
# print(str(list3))

# a = 78
# print(type(a))
# b = '78'
#
#
# str2 = 'АРАРРАА'
# if str2.isalpha():
#     print('алофовитные символы')
# elif str2.isupper():
#     print('все символы - символы чисел')
# elif str2.isdigit():
#     print('все символы - в верхнем регистре')
#
# str4 = 'hello wpn'):
#     print('yes')
# else:
#     print('no')
#
# str7 = 'qwerty'
# print(str7.upper())
# str8 =  'QWERTY'
# print(str8.lower())

# name_user = input('введите имя')
# print(name_user.listrip())


# str4 = 'hello, wpn'
# print(str4.find('ivan'))
#
# str5 = str4.replace('wpn','world')
# print(str5)
#
# str6 = str5.split(',')
# print(str6)
#
# str7 = "йоу че как"
# str8 = str7.split(',')
# print(str8)
#
# list3 = ()
# for _ in list3:
#     str3

# "Привет факел78 все что45 нужно"
"Привет ФАКЕЛ78 Все ЧТО45 Нужно"

# Получить от пользователя предложение из пяти слов
# В двух словах имеются числа
# Полученную строку преобразовать в список слов
# Слова, там где есть числа преобразовать в заглавные буквы
# А в тех словах где чисел нет, преобразовать
# только первые символы в заглавные
# После преобразования, собрать полученые слова в строку

# list2 = []
# a = input('пишите - ')
# list1 = a.split(' ') #split - разделяет
# for i in list1:
#     if i.isalpha() == False:
#         list2.append(i.upper()) #append - дополняет лист
#     else:
#         list2.append(i.title()) #append - дополняет лист
# str_final = " ".join(list2) # join - соединяет
# print(str_final)































































































