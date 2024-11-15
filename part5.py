from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Указываем путь до драйвера Chrome
# PATH = 'path_to_your_chrome_driver/chromedriver.exe'

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
for price_element01 in prices_elements:
    prices.append(price_element01.text)

# Сохраняем результаты в текстовом файле
with open('cian_prices.txt', mode='w', encoding='utf-8') as file:
    for price in prices:
        file.write(f'{price}\n')

# Закрываем браузер после завершения работы
driver.quit()

# РАБОЧИЙ КОД