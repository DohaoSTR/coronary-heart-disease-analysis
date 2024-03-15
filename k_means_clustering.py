from sklearn.cluster import KMeans
import numpy as np

import matplotlib.pyplot as plt

inertia = []
for k in range(1, 8):
    kmeans = KMeans(n_clusters=k, random_state=1).fit(x)
    inertia.append(np.sqrt(kmeans.inertia_))

plt.plot(range(1, 8), inertia, marker='s')
plt.xlabel('$k$')
plt.ylabel('$J(C_k)$')

wcss= []
for i in range (1,20):
    kmeans_object= KMeans(i)
    kmeans_object.fit(x)
    wcss.append(kmeans_object.inertia_)

plt.figure(figsize=(10,5))
plt.plot(range(1,20), wcss, marker= 'o')
plt.xlabel('Number of Clusters')
plt.ylabel('wcss')
plt.show()