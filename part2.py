import pandas as pd

# Создаем DataFrame с данными об оценках учеников по пяти предметам
data = {
    'Ученик': [f'Ученик {i+1}' for i in range(10)],
    'Математика': [5, 4, 3, 4, 5, 2, 4, 5, 3, 4],
    'Физика': [4, 5, 4, 3, 4, 5, 4, 5, 3, 4],
    'Химия': [3, 4, 5, 2, 4, 3, 5, 4, 4, 5],
    'Биология': [4, 4, 3, 5, 4, 4, 5, 3, 4, 5],
    'Литература': [5, 5, 4, 4, 5, 3, 4, 5, 4, 5]
}

df = pd.DataFrame(data)

# Выводим первые несколько строк DataFrame
print("Первые строки DataFrame:")
print(df.head())

# Средняя оценка по каждому предмету
mean_scores = df.mean(numeric_only=True)
print("\nСредняя оценка по каждому предмету:")
print(mean_scores)

# Медианная оценка по каждому предмету
median_scores = df.median(numeric_only=True)
print("\nМедианная оценка по каждому предмету:")
print(median_scores)

# Первый и третий квартили для оценок по математике
Q1_math = df['Математика'].quantile(0.25)
Q3_math = df['Математика'].quantile(0.75)
print("\nПервый квартиль по математике (Q1):", Q1_math)
print("Третий квартиль по математике (Q3):", Q3_math)

# Вычисляем IQR для оценок по математике (разница между Q3 и Q1)
IQR_math = Q3_math - Q1_math
print("Межквартильный размах по математике (IQR):", IQR_math)

# Стандартное отклонение по каждому предмету
std_dev = df.std(numeric_only=True)
print("\nСтандартное отклонение по каждому предмету:")
print(std_dev)