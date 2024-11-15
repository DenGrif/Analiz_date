import pandas as pd

# Чтение данных из CSV-файла
df = pd.read_csv('cian_prices.csv')

# Функция очистки данных
def clean_price(price_str):
    # Удаляем пробелы, ₽/мес., и заменяем запятую на точку
    cleaned_str = price_str.replace(' ', '').replace('₽/мес.', '').replace(',', '.')
    return int(cleaned_str)

# Применение функции очистки ко всем значениям в колонке 'Цена'
df['Цена'] = df['Цена'].apply(clean_price)

# Сохранение обработанных данных обратно в CSV-файл
df.to_csv('cleaned_cian_prices1.csv', index=False)

