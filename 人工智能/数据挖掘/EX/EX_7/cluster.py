# 导入必要的库
from sklearn.cluster import KMeans, AgglomerativeClustering, Birch
from sklearn.datasets import make_blobs, make_moons, make_circles
import matplotlib.pyplot as plt
import numpy as np

# 生成实验数据
np.random.seed(0)
n_samples = 1500
random_state = 170
X_linedata, y_linedata = make_blobs(n_samples=n_samples, random_state=random_state) #生成线型数据
X_moons, y_moons = make_moons(n_samples=n_samples, noise=0.05) #生成 月亮型数据
X_circle, y_circle = make_circles(n_samples=n_samples, factor=0.5, noise=0.05) #圆形数据

# 定义K-means聚类
kmeans = KMeans(n_clusters=3, random_state=random_state)

# 定义层次聚类
agglo = AgglomerativeClustering(n_clusters=3)

# 定义BIRCH聚类
birch = Birch(n_clusters=3)

# K-means聚类
y_pred = kmeans.fit_predict(X_linedata)
plt.scatter(X_linedata[:, 0], X_linedata[:, 1], c=y_pred)
plt.title("KMeans on linedata")
plt.savefig('/Users/luyao/Desktop/课内/DM/EX/EX_7/KMeans on linedata.png')
plt.clf()

y_pred = kmeans.fit_predict(X_moons)
plt.scatter(X_moons[:, 0], X_moons[:, 1], c=y_pred)
plt.title("KMeans on moons")
plt.savefig('/Users/luyao/Desktop/课内/DM/EX/EX_7/KMeans on moons.png')
plt.clf()

y_pred = kmeans.fit_predict(X_circle)
plt.scatter(X_circle[:, 0], X_circle[:, 1], c=y_pred)
plt.title("KMeans on circle")
plt.savefig('/Users/luyao/Desktop/课内/DM/EX/EX_7/KMeans on circle.png')
plt.clf()

# AgglomerativeClustering聚类
y_pred = agglo.fit_predict(X_linedata)
plt.scatter(X_linedata[:, 0], X_linedata[:, 1], c=y_pred)
plt.title("AgglomerativeClustering on linedata")
plt.savefig('/Users/luyao/Desktop/课内/DM/EX/EX_7/AgglomerativeClustering on linedata.png')
plt.clf()

y_pred = agglo.fit_predict(X_moons)
plt.scatter(X_moons[:, 0], X_moons[:, 1], c=y_pred)
plt.title("AgglomerativeClustering on moons")
plt.savefig('/Users/luyao/Desktop/课内/DM/EX/EX_7/AgglomerativeClustering on moons.png')
plt.clf()

y_pred = agglo.fit_predict(X_circle)
plt.scatter(X_circle[:, 0], X_circle[:, 1], c=y_pred)
plt.title("AgglomerativeClustering on circle")
plt.savefig('/Users/luyao/Desktop/课内/DM/EX/EX_7/AgglomerativeClustering on circle.png')
plt.clf()

# BIRCH聚类
y_pred = birch.fit_predict(X_linedata)
plt.scatter(X_linedata[:, 0], X_linedata[:, 1], c=y_pred)
plt.title("BIRCH on linedata")
plt.savefig('/Users/luyao/Desktop/课内/DM/EX/EX_7/BIRCH on linedata.png')
plt.clf()

y_pred = birch.fit_predict(X_moons)
plt.scatter(X_moons[:, 0], X_moons[:, 1], c=y_pred)
plt.title("BIRCH on moons")
plt.savefig('/Users/luyao/Desktop/课内/DM/EX/EX_7/BIRCH on moons.png')
plt.clf()

y_pred = birch.fit_predict(X_circle)
plt.scatter(X_circle[:, 0], X_circle[:, 1], c=y_pred)
plt.title("BIRCH on circle")
plt.savefig('/Users/luyao/Desktop/课内/DM/EX/EX_7/BIRCH on circle.png')
plt.clf()
