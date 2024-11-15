from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv
import pandas as pd
import matplotlib.pyplot as plt

# Настройки для Selenium
options = Options()
options.add_argument("--headless")  # Для работы без отображения браузера
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")

# Запуск браузера
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    # Открываем страницу
    url = "https://www.divan.ru/samara/category/divany-i-kresla"
    driver.get(url)

    # Ждем загрузки страницы
    time.sleep(5)

    # Ищем элементы с ценами
    prices_elements = driver.find_elements(By.CSS_SELECTOR, 'span[data-testid="price"]')

    # Сохраняем цены в список
    prices = [price_element.text for price_element in prices_elements]

    # Сохраняем данные в CSV
    with open("divany_prices.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Цена"])  # Заголовок
        for price in prices:
            writer.writerow([price])

    print(f"Успешно сохранены {len(prices)} цен в файл 'divany_prices.csv'")

finally:
    # Закрываем браузер
    driver.quit()


# Чтение данных из CSV-файла
df = pd.read_csv('divany_prices.csv')

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

# РАБОЧИЙ КОД