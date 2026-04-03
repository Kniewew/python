import pandas as pd

df = pd.read_excel('GroupPerformanceAndAttendance.xlsx', sheet_name='Отчёт', skiprows=5)
df = df.iloc[:, [1, 11]]  # ФИО и "Пропущено часов занятий: Всего"
# Убирает строки с пустыми ФИО и итоговые строки
df = df.dropna(subset=[df.columns[0]])
# число часов из строки
df[df.columns[1]] = df[df.columns[1]].astype(str).str.extract(r'(\d+) ч').astype(float)
# Сортируем по убыванию пропущенных часов
df_sorted = df.sort_values(by=df.columns[1], ascending=False)
# Добавляем рейтинг
df_sorted['Рейтинг'] = range(1, len(df_sorted) +1)
# Переименовываем столбцы для читаемости
df_sorted.columns = ['ФИО', 'Пропущено часов', 'Рейтинг']
# Выводим результат преобразуя меторд dataframe в обычную строку
print(df_sorted.to_string(index=False))