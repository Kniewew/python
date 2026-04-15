import matplotlib.pyplot as plt
import numpy as np

# Константы
g = 9.81  # ускорение свободного падения

# Ввод данных
try:
    mass = int(input("Введите массу тела (кг): "))
    angle_deg = int(input("Введите угол броска (градусы, от 0 до 90): "))
    speed_kmh = int(input("Введите скорость броска (км/ч): "))
except ValueError:
    print("Ошибка: введите числовые значения!")
    exit()
# Перевод скорости из км/ч в м/с
speed_ms = speed_kmh / 3.6 #TypeError: unsupported operand type(s) for /: 'str' and 'float'

# Перевод угла в радианы
angle_rad = np.radians(angle_deg)
# Начальные скорости по осям
v0_x = speed_ms * np.cos(angle_rad)
v0_y = speed_ms * np.sin(angle_rad)
# Время полёта (до падения на начальную высоту y=0)
t_flight = 2 * v0_y / g
# Временные точки для построения (более 100 точек для гладкости)
t = np.linspace(0, t_flight, num=200)
# Координаты в зависимости от времени
x = v0_x * t
y = v0_y * t - 0.5 * g * t**2
# Построение графика
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Траектория тела', color='blue', linewidth=2)
plt.scatter([x[0], x[-1]], [y[0], y[-1]], color='red', zorder=5)
plt.text(x[0], y[0], ' Старт', ha='right', va='bottom')
plt.text(x[-1], y[-1], ' Финиш', ha='left', va='bottom')
# Настройки графика
plt.title(f'Движение тела, брошенного под углом {angle_deg}° к горизонту\n'
          f'Масса = {mass} кг, Нач. скорость = {speed_kmh} км/ч ({speed_ms:.2f} м/с)')
plt.xlabel('Дальность полёта (м)')
plt.ylabel('Высота (м)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.axis('equal')  # Сохраняет пропорции осей для корректного отображения угла
plt.legend()
# Дополнительная информация на графике
info_text = f'Время полёта: {t_flight:.2f} с\n' \
            f'Дальность: {x[-1]:.2f} м\n' \
            f'Макс. высота: {max(y):.2f} м'
plt.text(0.05, 0.95, info_text, transform=plt.gca().transAxes,
         fontsize=10, verticalalignment='top',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
plt.show()
# Вывод в консоль
print(f"Начальная скорость: {speed_ms:.2f} м/с")
print(f"Время полёта: {t_flight:.2f} с")
print(f"Дальность полёта: {x[-1]:.2f} м")
print(f"Максимальная высота: {max(y):.2f} м")