import matplotlib.pyplot as plt
import numpy as np

# 读取virial.out文件
data = np.loadtxt('virial_test.out')

legend_names = ['xx', 'yy', 'zz', 'xy', 'yz', 'zx']

# 提取NEP模型计算的维里分量和目标维里分量数据
nep_data = data[:, :6]
target_data = data[:, 6:12]

# 绘制六张图表
fig, axs = plt.subplots(2, 3, figsize=(12, 8))

for i in range(3):
    row = i // 3
    col = i % 3

    ax = axs[row, col]

    # 绘制NEP分量和目标分量的散点图
    ax.plot(target_data[:, i], nep_data[:, i], '.', markersize=5)
    ax.plot(np.linspace(0, 1), np.linspace(0, 1), '-')

    # 设置图表标题和坐标轴标签
    ax.set_title(f'Virial Component {i+1}')
    ax.set_xlabel('Target Virial (eV/atom)')
    ax.set_ylabel('NEP Virial (eV/atom)')

for i in range(3,6):
    row = i // 3
    col = i % 3

    ax = axs[row, col]

    # 绘制NEP分量和目标分量的散点图
    ax.plot(target_data[:, i], nep_data[:, i], '.', markersize=5)
    ax.plot(np.linspace(-0.2, 0.2), np.linspace(-0.2, 0.2), '-')

    # 设置图表标题和坐标轴标签
    ax.set_title(f'Virial Component {i+1}')
    ax.set_xlabel('Target Virial (eV/atom)')
    ax.set_ylabel('NEP Virial (eV/atom)')

# 调整子图之间的间距和整体布局
plt.tight_layout()

# 保存图像
plt.savefig('virial.png')
