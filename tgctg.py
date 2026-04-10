import matplotlib.pyplot as plt
import numpy as np

# Генерация данных для графика
x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)

# Тангенс
y_tan = np.tan(x)
y_tan = np.where(np.abs(y_tan) > 10, np.nan, y_tan)

# Котангенс
y_cot = 1 / np.tan(x)
y_cot = np.where(np.abs(y_cot) > 10, np.nan, y_cot)

plt.figure(figsize=(12, 7))
plt.plot(x, y_tan, label='tan(x)', color='blue')
plt.plot(x, y_cot, label='cot(x)', color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Графики функций тангенса и котангенса')
plt.grid(True, alpha=0.3)
plt.legend()
plt.show()













