import matplotlib.pyplot as plt

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.4)

model = KNeighborsClassifier(n_neighbors = 3)
model.fit(x_train, y_train)
predictions = model.predict(x_test)

#Матрица ошибок
print(confusion_matrix(y_test, predictions))
#Отчёт по классификиции
print(classification_report(y_test, predictions))

print('Точность обучающей выборки:', model.score(x_train, y_train))
print('Точность тестовой выборки:', accuracy_score(y_test, predictions))

###
# Классификация методом k-ближайших соседей. 
# Точность модели - 77 процентов, классы определеяет с равной точностью.
###