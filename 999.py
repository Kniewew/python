def R(N):
    # 1. Двоичная запись числа N
    b = bin(N)[2:]
    # 2. Замена: 0 -> 1, 1 -> 0, затем удаление нулей
    b = ''.join('1' if x == '0' else '0' for x in b)
    b = b.replace('0', '')
    # 3. Перевод обратно в десятичную систему (если строка пустая → 0)
    x = int(b, 2) if b else 0
    # 4. Разность N и x
    return N - x
# Ввод числа с клавиатуры
target = int(input("Введите число: "))
# Поиск наименьшего N, при котором R(N) = target
n = 1
while True:
    if R(n) == target:
        print(n)
        break
    n += 1