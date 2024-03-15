import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import scale

from imblearn.over_sampling import SMOTE

dataset = pd.read_excel('dataset.xlsx')

# Нормализовали данные
scaler = StandardScaler(copy=True, with_mean=True, with_std=True)
scaler.fit(dataset.drop('ИБС', axis=1))
scaled_features = scaler.transform(dataset.drop('ИБС', axis=1))
scaled_data = pd.DataFrame(scaled_features, columns = dataset.drop('ИБС', axis=1).columns)

#x = scaled_data
#y = dataset['ИБС']

x = dataset.drop('ИБС', axis=1)
y = dataset['ИБС']

# Уравняли количество строк с разными классами
sm = SMOTE(random_state=42, k_neighbors=4)
x, y = sm.fit_resample(x, y)

print("Кол-во строк каждого класса:")
print(dataset['ИБС'].value_counts())

print("\nНормализованный набор данных.")
print(x)

###
# Нормализация данных. 
# Кол-во строк где ИБС = 1 в два раза меньше где ИБС = 0, 
# с помощью SMOTE уравнял количество строк.
###