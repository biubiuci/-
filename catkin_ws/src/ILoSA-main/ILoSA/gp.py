import numpy as np
import matplotlib.pyplot as plt
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF

# 生成一些示例轨迹数据
np.random.seed(0)
X = np.sort(5 * np.random.rand(80, 1), axis=0)
y = np.sin(X).ravel()
print(X,y)
# 创建高斯过程回归模型
kernel = 1.0 * RBF(length_scale=1.0)
gp = GaussianProcessRegressor(kernel=kernel, n_restarts_optimizer=10)

# 训练高斯过程模型
gp.fit(X, y)

# 生成新的输入位置以复现轨迹
X_new = np.linspace(0, 5, 1000)[:, np.newaxis]

# 预测轨迹
y_pred, sigma = gp.predict(X_new, return_std=True)

# 可视化原始数据和复现的轨迹
plt.figure(figsize=(10, 5))
#plt.scatter(X, y, c='r', s=20, zorder=10, edgecolors=(0, 0, 0))
plt.plot(X_new, y_pred, 'b-')
plt.fill_between(X_new[:, 0], y_pred - 1.96 * sigma, y_pred + 1.96 * sigma, alpha=0.2)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Highway Trajectory Prediction with Gaussian Process")
#plt.plot(X,y)
plt.show()



