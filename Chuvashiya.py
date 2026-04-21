import matplotlib.pyplot as plt
nas = [1159768,758900,666202,4019606,3060000, 1165334]
xle = ["чувашия", "Мордовия", "Марий Эл", "Татарстан", "Нижегородская область", "Ульяновская область"]
for i in range(len(xle)):
    print(f"{i}- {xle[i]} - {nas[i]}")
def pie1():
    region = [nas[0]]
    labels = [xle[0]]
    plt.title("схема 1") # название графика
    plt.pie(region, labels=labels, ) # круговая диаграмма
    plt.show()
pie1()
def pie2():
    region = [i for i in nas]
    labels = [i for i in xle]
    plt.title("схема 2")
    plt.pie(region, labels=labels,autopct='%.2f' )
    plt.show()
# autopct='%.2f' - выводит проценты
pie2()
def pie3():
    region = [i for i in nas]
    labels = [i for i in xle]
    plt.title("схема 3")
    plt.pie(region, labels=labels,autopct='%.2f', shadow=True, wedgeprops=dict(width=0.5))
    # plt.legend(labels, loc="right") # по желанию
    plt.show()
# shadow=True добавляет тень
# wedgeprops=dict(width=0.5) - это передаёт параметры внешнего вида клиньев (без него будет ошибка)
# width=0.5 - размер удаления графика от центра
pie3()
def pie4():
    region = [i for i in nas]
    labels = [i for i in xle]
    plt.title("схема 4")
    exp = (0.2,0,0,0,0,0)
    plt.pie(region, labels=labels,autopct='%.2f', shadow=True, explode=exp, wedgeprops=dict(width=0.5))
    plt.show()
# exp = (0.2,0,0,0,0,0) - расстояние на которое будет выдвинут пункт из гистаграммы
# explode=exp - использует exp
pie4()