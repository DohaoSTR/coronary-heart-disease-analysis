from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

import numpy as np

import matplotlib.pyplot as plt

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.4)

def get_depth():
    depth = range(1, 30)
    accuracy = []
    for i in depth:
        new_model = DecisionTreeClassifier(criterion="entropy", max_depth=i)
        new_model.fit(x_train, y_train)
        
        new_predictions = new_model.predict(x_test)

        accuracy.append(np.mean(new_predictions != y_test))

    plt.plot(accuracy)

get_depth()

###
# Определение глубины дерева: 4 оптимальное значение.
###