import matplotlib.pyplot as plt
import numpy as np

# 模拟机械臂的五个关节角度和轨迹
# 这里使用简单的示例数据，实际应用中需要根据您的具体情况获取数据
num_points = 100
time = np.linspace(0, 2*np.pi, num_points)

# 五个关节的角度
joint1_angles = np.sin(time)
joint2_angles = np.cos(time)
joint3_angles = np.sin(2*time)
joint4_angles = np.cos(2*time)
joint5_angles = np.sin(3*time)

# 计算末端路径
end_effector_path = np.column_stack(
    (np.cos(time), np.sin(time), np.zeros_like(time)))  # 假设 z 轴保持不变

# 绘制关节角度
plt.figure(figsize=(12, 8))
for i, joint_angles in enumerate([joint1_angles, joint2_angles, joint3_angles, joint4_angles, joint5_angles]):
    plt.subplot(5, 1, i+1)
    plt.plot(time, joint_angles, label=f'Joint {i+1}')
    plt.title(f'Joint {i+1} Angle over Time')
    plt.xlabel('Time')
    plt.ylabel('Angle (radians)')
    plt.legend()

# 绘制机械臂末端路径
plt.figure(figsize=(8, 8))
plt.plot(end_effector_path[:, 0], end_effector_path[:, 1], label='End Effector Path')
plt.title('End Effector Path')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()

# 显示图形
plt.tight_layout()
plt.show()
