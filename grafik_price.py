import pandas as pd
import matplotlib.pyplot as plt

# Чтение данных из CSV-файла
df = pd.read_csv('cleaned_cian_prices1.csv')

# Получение массива цен
prices = df['Цена']

# Создание фигуры и оси
fig, ax = plt.subplots(figsize=(12, 6))  # Размер графика 12x6 дюймов

# Построение гистограммы
ax.hist(prices, bins=20, color='skyblue', edgecolor='black')

# Настройка осей и заголовков
ax.set_xlabel('Цена (руб.)')
ax.set_ylabel('Количество объявлений')
ax.set_title('Распределение цен на квартиры')

# Показать сетку
ax.grid(True, axis='y', alpha=0.75)

# Отображение графика
plt.show()
