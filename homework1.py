# Задача 1: Гистограмма для случайных данных, сгенерированных с помощью функции numpy.random.normal
import numpy as np
import matplotlib.pyplot as plt

# Параметры нормального распределения
mean = 0       # Среднее значение
std_dev = 1    # Стандартное отклонение
num_samples = 1000  # Количество образцов

# Генерация случайных чисел, распределенных по нормальному распределению
data = np.random.normal(mean, std_dev, num_samples)

# Построение гистограммы
plt.figure(figsize=(10, 6))
plt.hist(data, bins=30, density=True, color='skyblue', edgecolor='black')
plt.xlabel('Значение')
plt.ylabel('Частота')
plt.title('Нормальное распределение')
plt.grid(True, axis='y', alpha=0.75)
plt.show()
