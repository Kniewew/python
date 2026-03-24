import pandas as pd
import numpy as np
df = pd.read_excel('1s.xlsx')
# Средний балл
a = ['Предмет1', 'Предмет2', 'Предмет3', 'Предмет4', 'Прдемет5']
df['средний_балл'] = df[a].mean(axis=1)
ball = df['средний_балл'].mean()
print(f"Средний балл группы: {ball}")
# 2. Студенты без троек (все оценки >= 4)
bez_troek = df[(df[a] >= 4).all(axis=1)]
print("\nСтуденты без троек:")
print(bez_troek['name'].tolist())

# 3. Список тех, кто не получает стипендию (stepen = 0)
bez_stip = df[df['stepen'] == 0]
print("\nСтуденты, не получающие стипендию:")
print(bez_stip['name'].tolist())

# 4. Проживающие в Шумерле с баллом выше 4.5
shumerla_vysokiy = df[(df['Город проживания'] == 'Шумерля') & (df['средний_балл'] > 4.5)]
print("\nСтуденты из Шумерли с баллом выше 4.5:")
print(shumerla_vysokiy['name'].tolist())

# 5. Студенты не из Шумерли, имеющие хотя бы одну оценку 5
ne_shumerla_pyat = df[(df['Город проживания'] != 'Шумерля') & ((df[a] == 5).any(axis=1))]
print("\nСтуденты не из Шумерли, имеющие оценку 5:")
print(ne_shumerla_pyat['name'].tolist())

# 6. Количество студентов, которым есть 18 (age = 18)
kol_18 = len(df[df['aga'] == 18])
print(f"\nКоличество студентов в возрасте 18 лет: {kol_18}")