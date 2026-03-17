import pandas as pd
# список с индексами
xle = pd.Series([4, 7, -5, 3])
print(xle)
# преобразование значений
xle1 = pd.Series(['cat', 'dog', 'bird'])
print(xle1.map({'cat': 'кошка', 'dog': 'собака'}))
# сортировка
xle2 = pd.Series([3, 1, 4, 2])
print(xle2.sort_values())
# уникальные значения
xle3 = pd.Series([1, 2, 2, 3, 3, 3])
print(xle3.unique())
# убирает ноне
xle4 = pd.Series([1, None, 3, None, 5])
print(xle4.dropna())
# сбрасывает индекс
xle5 = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print(xle5.reset_index(drop=True))
# проверяет числа в диапазоне
xle6 = pd.Series([1, 5, 10, 15, 20])
print(xle6.between(5, 15))
# наибольшие и наименьшие числа
xle7 = pd.Series([5, 2, 8, 1, 9, 3])
print(xle7.nlargest(3))
print(xle7.nsmallest(2))
# показывает дубликаты
xle8 = pd.Series([1, 2, 2, 3, 3, 3])
print(xle8.duplicated())
# удалит дубликаты
xle9 = pd.Series([1, 2, 2, 3, 3, 3])
print(xle9.drop_duplicates())
# сдвигает вверх или вниз
s = pd.Series([10, 20, 30, 40])
print(s.shift(1))  # сдвиг вниз
print(s.shift(-1)) # сдвиг вверх
# накопительные операции
s = pd.Series([1, 2, 3, 4])
print(s.cumsum())  # накопительная сумма
print(s.cumprod()) # накопительное произведение