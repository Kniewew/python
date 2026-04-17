import matplotlib.pyplot as plt
import numpy as np
np.random.seed(42)
d = np.random.randn(500)
plt.figure(figsize=(12, 6))
n, b, p = plt.hist(d, bins=30, edgecolor='black', alpha=0.7)
# больше предыдущего красный, меньше зеленый
colors = ['gray']  # первый столбец серый, так как нет предыдущего
for i in range(1, len(n)):
    if n[i] > n[i-1]:
        colors.append('red')
    else:
        colors.append('green')
# Применяем цвета
for i, bar in enumerate(p):
    bar.set_color(colors[i])
plt.title('Гистограмма: график рынка', fontsize=12)
plt.xlabel('Знач', fontsize=12)
plt.ylabel('Част', fontsize=12)
plt.grid(True, alpha=0.3)
plt.show()
