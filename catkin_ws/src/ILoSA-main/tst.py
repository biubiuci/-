import matplotlib.pyplot as plt
import numpy as np

# 假设有关节角度矩阵和时间向量
# 这里的数据仅为示例，请替换为你实际的数据
joint_angles = np.random.rand(100, 6)  # 100个时间步，每个时间步有6个关节
time_vector = np.linspace(0, 10, 100)  # 从0到10秒的时间向量

# 逐个关节显示角度随时间变化
for joint in range(joint_angles.shape[1]):
    # 创建新的图像
    plt.figure()

    # 绘制关节角度随时间变化的曲线
    plt.plot(time_vector, joint_angles[:, joint], label=f'Joint {joint + 1}', color='blue')

    # 标记每个关节运动的时间点
    for i, time_point in enumerate(time_vector):
        plt.text(time_point, joint_angles[i, joint], f'{i}', fontsize=8, color='red', ha='center', va='bottom')

    # 设置图像属性
    plt.title(f'Joint {joint + 1} Angle over Time')
    plt.xlabel('Time (s)')
    plt.ylabel('Joint Angle (rad)')
    plt.legend()

    # 显示图像
    plt.show()
