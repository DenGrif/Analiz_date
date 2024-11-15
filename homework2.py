# Задача 2: Диаграмма рассеяния для двух наборов случайных данных,
# сгенерированных с помощью функции numpy.random.rand
import numpy as np
import matplotlib.pyplot as plt

# Генерация двух наборов случайных данных
x_data = np.random.rand(50)
y_data = np.random.rand(50)

# Построение диаграммы рассеяния
plt.figure(figsize=(10, 6))
plt.scatter(x_data, y_data, marker='o', c='b')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Диаграмма рассеяния')
plt.grid(True)
plt.show()

