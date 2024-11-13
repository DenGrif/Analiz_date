import pandas as pd

# Загружаем данные из файла CSV в DataFrame
data = pd.read_csv('dz.csv')

# Выводим первые 5 строк данных, чтобы понять структуру и содержание DataFrame
print("Первые 5 строк данных:")
print(data.head())

# Выводим общую информацию о данных (например, типы данных и наличие пропусков)
print("\nИнформация о данных:")
print(data.info())

# Выводим статистическое описание числовых колонок, чтобы оценить основные показатели
print("\nСтатистическое описание данных:")
print(data.describe())

# Рассчитываем среднюю зарплату (Salary) по каждому городу (City) и выводим результат
average_salary_by_city = data.groupby('City')['Salary'].mean()
print("\nСредняя зарплата по городу:")
print(average_salary_by_city)
