import matplotlib.pyplot as plt 
import numpy as np 

from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
from sklearn.metrics import confusion_matrix

iris = load_iris()
X = iris.data 

kmeans = KMeans(n_clusters = 3, random_state = 42)

kmeans.fit(X)

labels = kmeans.labels_

centroid = kmeans.cluster_centers_

plt.figure(figsize=(6,8))
plt.scatter(X[:,0],X[:,1], c=labels, label="Data Points")
plt.scatter(centroid[:,0],centroid[:,1], c='red',s=200,marker='X',label="Centroid")
plt.xlabel('')
plt.ylabel('')
plt.title("KMean Clustering (DV06AI00020)")
plt.legend()
plt.show()

