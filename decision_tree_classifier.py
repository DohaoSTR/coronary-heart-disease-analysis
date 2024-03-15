import pandas as pd
import graphviz
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import precision_score

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz

x_training, x_test, y_training, y_test = train_test_split(x, y, test_size = 0.4)

model = DecisionTreeClassifier(criterion="entropy", max_depth=4)
model.fit(x_training, y_training)
y_pred = model.predict(x_test)

print(confusion_matrix(y_test, predictions))

print(classification_report(y_test, y_pred))
print('Точность обучающей выборки:', model.score(x_training, y_training))
print('Точность тестовой выборки:', accuracy_score(y_test, y_pred))

dot_data = export_graphviz(model, out_file=None, class_names=['Был', 'Не был'], 
                           feature_names=dataset.drop("ИБС", axis=1).columns, impurity=False, filled=True)
graph = graphviz.Source(dot_data)
graph.render('tree')

graph