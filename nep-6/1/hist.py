import matplotlib.pyplot as plt
import numpy as np

# 文件名
filename = 'nep.restart'

# 读取数据并提取第一列数据 para_list
with open(filename, 'r') as file:
    lines = file.readlines()
    para_list = [float(line.split()[0]) for line in lines]

# 计算对数绝对值 log_abs_para
log_abs_para = np.log10(np.abs(para_list))

# 绘制直方图
plt.hist(log_abs_para, bins=50)
plt.xlabel('log(abs(para))')
plt.ylabel('Frequency')
plt.title('Histogram of log(abs(para))')

# 显示图像
plt.savefig("histogram.png")
