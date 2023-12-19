import csv

# 假设你有一个包含数据的列表，例如：
data = [
    [1, 45.6, 78.2],
    [2, 36.8, 92.5],
    [3, 50.2, 64.7],
    # ... 可以继续添加数据
]

# 假设你要保存的 CSV 文件名为 'output.csv'
csv_file_path = 'output.csv'

# 使用 csv 模块将数据写入 CSV 文件
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    # 写入数据
    writer.writerows(data)

print(f'Data has been successfully written to {csv_file_path}.')
