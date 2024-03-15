import matplotlib.pyplot as plt
import seaborn as sns

from mpl_toolkits.mplot3d import Axes3D

def plot2D(x, y, labels, x_label, y_label):
    fig = plt.figure(figsize=(20,7))
    ax = fig.add_subplot()

    scatter = ax.scatter(x, y, c = labels, cmap="Dark2", linewidths = 0.1)
    ax.legend(*scatter.legend_elements())

    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()

from sklearn.cluster import KMeans

def kmeans(df, n_clusters):
    kmeans = KMeans(n_clusters = n_clusters)
    kmeans.fit(df)

    return model, kmeans.labels_

model, labels = kmeans(x, 2)

plot2D(x['САД'], x['ЛПР'], labels, 'САД', 'ЛПР')
plot2D(x['САД'], x['ИМТ'], labels, 'САД', 'ИМТ')
plot2D(x['ЛПР'], x['ИМТ'], labels, 'ЛПР', 'ИМТ')
plot2D(x['Табак'], x['Стрессоустойчивость'], labels, 'Табак', 'Стрессоустойчивость')
plot2D(x['Алкоголь'], x['Стрессоустойчивость'], labels, 'Алкоголь', 'Стрессоустойчивость')
plot2D(x['Табак'], x['Алкоголь'], labels, 'Табак', 'Алкоголь')