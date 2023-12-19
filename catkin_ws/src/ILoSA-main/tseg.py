import numpy as np
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, ConstantKernel as C
import matplotlib.pyplot as plt

# 生成示例专家轨迹数据（关节角度）
expert_states = np.random.rand(100, 3)  # 100个时间步，3个关节
expert_actions = np.sin(expert_states) + 0.1 * np.random.randn(100, 3)

# 使用高斯过程回归拟合专家轨迹数据
kernel = C(1.0, (1e-3, 1e3)) * RBF(1.0, (1e-2, 1e2))
gp = GaussianProcessRegressor(kernel=kernel, n_restarts_optimizer=10)
gp.fit(expert_states, expert_actions)

# 在状态空间中生成代理的动作预测
test_states = np.random.rand(10, 3)  # 测试状态
predicted_actions, _ = gp.predict(test_states, return_std=True)

# 在机械臂上执行代理预测的动作（这里仅作为示例，实际中需要与机械臂控制器交互）
# execute_actions(predicted_actions)

# 可视化结果（仅适用于3维关节角度的情况）
fig = plt.figure(figsize=(12, 6))

for i in range(3):
    plt.subplot(2, 3, i + 1)
    plt.scatter(expert_states[:, i], expert_actions[:, i], c='r', marker='x', label='Expert Trajectory')
    plt.plot(test_states[:, i], predicted_actions[:, i], label='Predicted Trajectory')
    plt.xlabel(f'Joint {i+1} Angle')
    plt.ylabel(f'Joint {i+1} Action')
    plt.legend()

plt.tight_layout()
plt.show()
