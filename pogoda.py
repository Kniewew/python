import numpy as np
xle1 = np.array(["Пн", 6, 93, 766])
xle2 = np.array(["Вс", -20, 50, 754])
class Weather:
    def __init__(self, d, t, h, p):
        self.d = d  # день
        self.t = t  # температура
        self.h = h  # влажность
        self.p = p  # давление
    def __add__(self, other):
        self.t =self.t + other.t
        self.h = self.h + other.h
        self.p = self.p + other.p
        return self.h, self.p, self.t
    def __truediv__(self):
        self.t = self.t / 7
        self.h = self.h / 7
        self.p = self.p / 7
        return self.h, self.p, self.t
    def __str__(self):
        return f"средние показатели погоды за неделю {xle1[0]} - {xle2[0]} \nсредняя температура на неделю = {self.t} С,\nвлажность = {self.h},\nдавление = {self.p}"
# (текущая неделя)
d7 = Weather("Вс", xle1[1], xle1[2], xle1[3])
d2 = Weather("Пн", xle2[1], xle2[2], xle2[3])
print(d7,d2)













