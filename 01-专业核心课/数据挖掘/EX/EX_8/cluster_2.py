# 导入必要的库
from sklearn.cluster import DBSCAN, OPTICS
from sklearn.datasets import make_blobs, make_moons, make_circles
import matplotlib.pyplot as plt
import numpy as np

# 设置随机种子
np.random.seed(0)

# 生成实验数据
n_samples = 1500
random_state = 170
X_linedata, _ = make_blobs(n_samples=n_samples, random_state=random_state)  # 生成线型数据
X_moons, _ = make_moons(n_samples=n_samples, noise=0.05)  # 生成月亮型数据
X_circles, _ = make_circles(n_samples=n_samples, factor=0.5, noise=0.05)  # 生成圆形数据

# 定义DBSCAN聚类
dbscan = DBSCAN(eps=0.3, min_samples=10)

# 定义OPTICS聚类
optics = OPTICS(min_samples=10, xi=0.05, min_cluster_size=0.1)

# 准备画布
plt.figure(figsize=(12, 8))

# DBSCAN聚类
# plt.subplot(231)
y_pred_dbscan = dbscan.fit_predict(X_linedata)
plt.scatter(X_linedata[:, 0], X_linedata[:, 1], c=y_pred_dbscan)
plt.title("DBSCAN on linedata")
plt.savefig("/Users/luyao/Desktop/课内/DM/EX/EX_8/DBSCAN on linedata.png")
plt.clf()

# plt.subplot(232)
y_pred_dbscan = dbscan.fit_predict(X_moons)
plt.scatter(X_moons[:, 0], X_moons[:, 1], c=y_pred_dbscan)
plt.title("DBSCAN on moons")
plt.savefig("/Users/luyao/Desktop/课内/DM/EX/EX_8/DBSCAN on moons.png")
plt.clf()

# plt.subplot(233)
y_pred_dbscan = dbscan.fit_predict(X_circles)
plt.scatter(X_circles[:, 0], X_circles[:, 1], c=y_pred_dbscan)
plt.title("DBSCAN on circles")
plt.savefig("/Users/luyao/Desktop/课内/DM/EX/EX_8/DBSCAN on circles.png")
plt.clf()

# OPTICS聚类
# plt.subplot(234)
y_pred_optics = optics.fit_predict(X_linedata)
plt.scatter(X_linedata[:, 0], X_linedata[:, 1], c=y_pred_optics)
plt.title("OPTICS on linedata")
plt.savefig("/Users/luyao/Desktop/课内/DM/EX/EX_8/OPTICS on linedata.png")
plt.clf()

# plt.subplot(235)
y_pred_optics = optics.fit_predict(X_moons)
plt.scatter(X_moons[:, 0], X_moons[:, 1], c=y_pred_optics)
plt.title("OPTICS on moons")
plt.savefig("/Users/luyao/Desktop/课内/DM/EX/EX_8/OPTICS on moons.png")
plt.clf()

# plt.subplot(236)
y_pred_optics = optics.fit_predict(X_circles)
plt.scatter(X_circles[:, 0], X_circles[:, 1], c=y_pred_optics)
plt.title("OPTICS on circles")
plt.savefig("/Users/luyao/Desktop/课内/DM/EX/EX_8/OPTICS on circles.png")
plt.clf()

# 显示图形
# plt.tight_layout()
# plt.show()

