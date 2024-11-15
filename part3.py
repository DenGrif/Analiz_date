from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

# Указываем путь до драйвера Chrome
#PATH = 'path_to_your_chrome_driver/chromedriver.exe'

# Запускаем браузер
driver = webdriver.Chrome()

# Открываем страницу с объявлениями о сдаче квартир
url = 'https://www.cian.ru/snyat-kvartiru-1-komn-ili-2-komn/'
driver.get(url)

# Ждем несколько секунд, чтобы страница загрузилась полностью
time.sleep(20)

# Находим все элементы, содержащие цены
prices_elements = driver.find_elements(By.XPATH, "//span[@data-mark='MainPrice']/span")

# Создаем список для хранения цен
prices = []

# Извлекаем тексты цен и добавляем их в список
for price_element in prices_elements:
    prices.append(price_element.text)

# Сохраняем результаты в CSV-файле
with open('cian_prices.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Добавляем заголовок
    writer.writerow(['Цена'])

    for price in prices:
        writer.writerow([price])

# Закрываем браузер после завершения работы
driver.quit()
