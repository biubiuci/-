import pandas as pd
import matplotlib.pyplot as plt

# 读取 CSV 文件，假设文件名为 'joint_angles.csv'
file_path = 'joint-p-p.csv'
df = pd.read_csv(file_path)

# 获取唯一的关节列表
joints = df.iloc[:, 0].unique()

# 创建一个颜色列表，可以根据需要扩展
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

# 绘制关节角度随时间的变化图
plt.figure(figsize=(10, 6))

for i, joint in enumerate(joints):
    joint_data = df[df.iloc[:, 0] == joint]
    angles = joint_data.iloc[:, 2]  # 假设角度数据在第三列
    movement_count = len(angles)
    
    # 选择颜色
    color = colors[i % len(colors)]

    # 绘制关节运动轨迹
    plt.plot(range(1, movement_count + 1), angles, marker='o', linestyle='-', color=color, label=f'joint {joint}')

plt.title('Changes in joint angles:Teaching trajectory')
plt.xlabel('Exercise frequency')
plt.ylabel('Joint angle (degrees)')
plt.legend()
plt.grid(True)
plt.show()
