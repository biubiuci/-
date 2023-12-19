import threading
import time

# 假设你的机械臂转动函数
def rotate_arm(item):
    # 模拟机械臂转动，这里可以是任何耗时的操作
    time.sleep(2)
    print(f"Arm rotated for item: {item}")

# 假设有一个列表需要迭代
my_list = [1, 2, 3, 4, 5]

# 定义一个锁，用于同步线程
lock = threading.Lock()

# 在 for 循环中执行机械臂转动函数并等待它完成
for item in my_list:
    # 启动一个线程执行机械臂转动函数
    thread = threading.Thread(target=rotate_arm, args=(item,))
    thread.start()

    # 等待线程执行完成
    thread.join()

    print("Waiting for the arm rotation to complete...")

print("All arm rotations completed.")

