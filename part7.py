# обработать данные, найти среднюю цену и вывести ее, а также сделать гистограмму цен на диваны
import pandas as pd
import matplotlib.pyplot as plt

# Чтение данных из CSV-файла
df = pd.read_csv('divany_prices01.csv')

# Очистка данных от лишних символов и приведение к числовому формату
df['Цена'] = df['Цена'].str.replace(r'\s+', '', regex=True).str.replace('руб.', '').astype(float)

# Вычисление средней цены
average_price = df['Цена'].mean()
print(f"Средняя цена на диван: {average_price:.2f} руб.")

# Построение гистограммы цен на диваны
plt.figure(figsize=(10, 6))
plt.hist(df['Цена'], bins=20, color='skyblue', edgecolor='black')
plt.xlabel('Цена (руб.)')
plt.ylabel('Количество диванов')
plt.title('Распределение цен на диваны')
plt.grid(True, axis='y', alpha=0.75)
plt.show()
