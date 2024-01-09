import faiss

# 创建随机数据集作为示例
import numpy as np
d = 64  # 特征维度
nb = 100000  # 数据库中的向量数量
np.random.seed(0)
xb = np.random.random((nb, d)).astype('float32')

# 初始化Faiss索引
index = faiss.IndexFlatL2(d)  # 使用L2距离度量创建一个Flat索引

# 向索引中添加数据
index.add(xb)

# 查询向量
k = 4  # 返回的最近邻居数量
xq = np.random.random((1, d)).astype('float32')  # 随机查询向量
D, I = index.search(xq, k)  # 执行查询

print("查询向量:", xq)
print("最近的", k, "个邻居的距离:", D)
print("最近的", k, "个邻居的索引:", I)
