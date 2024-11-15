# Необходимо спарсить цены на диваны с сайта divan.ru в csv файл
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv

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
    with open("divany_prices01.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Цена"])  # Заголовок
        for price in prices:
            writer.writerow([price])

    print(f"Успешно сохранены {len(prices)} цен в файл 'divany_prices01.csv'")

finally:
    # Закрываем браузер
    driver.quit()
# РАБОЧИЙ КОД