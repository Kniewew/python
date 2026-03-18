print("1 - в двоичную систему")
print("2 - в десятеричную")
v = input("Выберите: ")

if v == "1":
    a = int(input("Число: "))
    if a == 0:
        print("0")
    else:
        b = ""
        while a > 0:
            if a % 2 == 1:
                b = "1" + b
            else:
                b = "0" + b
            a = a // 2
        print(b)

if v == "2":
    a = input("Число: ")
    b = 0
    c = 1
    for i in a:
        b = b * 2 + int(i)
    print(b)