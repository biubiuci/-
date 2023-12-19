import numpy as np
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF
import matplotlib.pyplot as plt

# 生成示例数据
# 假设您有一个多维轨迹，每一维度的数据作为一个特征
X = np.random.rand(100, 2)  # 这里创建一个示例的2维轨迹，您需要根据实际情况提供您的数据
y = np.sin(X[:, 0]) + np.cos(X[:, 1])  # 示例的目标值

# 创建高斯过程回归模型
kernel = RBF()  # 选择RBF核函数，可以根据问题选择不同的核函数
model = GaussianProcessRegressor(kernel=kernel, n_restarts_optimizer=10)

# 拟合模型
model.fit(X, y)

# 生成用于复现轨迹的数据点
x_pred = np.random.rand(100, 2)  # 这里创建要复现轨迹的数据点

# 进行轨迹复现
y_pred, sigma = model.predict(x_pred, return_std=True)

# 可视化原始轨迹和复现轨迹
plt.figure()
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis', marker='o', label='Original Trajectory')
plt.scatter(x_pred[:, 0], x_pred[:, 1], c=y_pred, cmap='viridis', marker='x', label='Reconstructed Trajectory')
plt.colorbar()
plt.legend()
plt.title('Original vs. Reconstructed Trajectory')
plt.show()
