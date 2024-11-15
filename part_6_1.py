from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

# Запускаем браузер
driver = webdriver.Chrome()

# Открываем страницу с объявлениями о продаже
url = 'https://divan.ru/category/divany-i-kresla'
driver.get(url)

# Ждем несколько секунд, чтобы страница загрузилась полностью
time.sleep(60)

# Находим все элементы, содержащие цены
prices_elements = driver.find_elements(By.CSS_SELECTOR, 'span[data-testid="price"]')


# Создаем список для хранения цен
prices = []

# Извлекаем тексты цен и добавляем их в список
for price_element in prices_elements:
    prices.append(price_element.text)

# Сохраняем результаты в CSV-файле
with open('divany_prices05.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Добавляем заголовок
    writer.writerow(['Цена'])

    for price in prices:
        writer.writerow([price])

# Закрываем браузер после завершения работы
driver.quit()
