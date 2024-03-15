import matplotlib.pyplot as plt

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.4)

accuracy_train = []
accuracy_test = []

neighbors=range(1, 10)
for i in neighbors:
    new_model = KNeighborsClassifier(n_neighbors = i)
    new_model.fit(x_train, y_train)
    new_predictions = new_model.predict(x_test)
    accuracy_train.append(new_model.score(x_train, y_train))
    accuracy_test.append(new_model.score(x_test, y_test))

plt.plot(neighbors, accuracy_train, marker='o')
plt.title('На тренеровочной выборке')
plt.xticks(neighbors)
plt.xlabel('Количество соседей')
plt.ylabel('Точность')
plt.show()

plt.plot(neighbors, accuracy_test, marker='o')
plt.title('На тестовой выборке')
plt.xticks(neighbors)
plt.xlabel('Количество соседей')
plt.ylabel('Точность')
plt.show()

###
# Поиск оптимального значения k (кол-во соседей). 
# Максимальная точность при k = 1, чем больше соседей тем точность меньше.
###